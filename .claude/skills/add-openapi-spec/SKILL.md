---
name: add-openapi-spec
description: Add a healthcare-org service's OpenAPI spec to the Fern docs. Use when asked to add, wire up, or register a new service API from its GitHub repo.
---

Add one service's `openapi.yaml` from its `healthcare-org-app` repo to this Fern project.

Specs are **not** vendored here. Each is pulled from its service repo at generate time via a `git:` ref, so adding a service means adding one entry to one file.

## Layout

All service specs compose into a single API:

```
fern/apis/healthcare-org/generators.yml   # every spec, one namespace each
fern/docs.yml                              # one entry: api-name: healthcare-org
```

`docs.yml` does **not** change when you add a service. Per-service grouping in the sidebar comes from the `namespace`, not from navigation.

## Steps

### 1. Confirm the repo name

Service repos are `healthcare-<name>`, and the name is not always what you would guess — `healthcare-appointments` is plural, `healthcare-appointment` does not exist.

```bash
gh api repos/healthcare-org-app/healthcare-<name> --jq '.full_name, .visibility'
```

If that 404s, find the real name before going further:

```bash
gh repo list healthcare-org-app --limit 200 --json name --jq '.[].name' | grep <fragment>
```

### 2. Confirm the spec exists

Check with the **Contents API**, not `raw.githubusercontent.com`:

```bash
gh api repos/healthcare-org-app/healthcare-<name>/contents/openapi.yaml --jq '.size'
```

<!-- The raw CDN caches for 5 minutes (max-age=300) and serves a 404 for a spec
     that was just pushed, while the Contents API already returns it. A raw 404
     alone does not mean the spec is missing. -->

If there is no `openapi.yaml`, stop and report it — most of the 101 services do not have one yet. Do not invent a spec.

### 3. Pick a namespace

The namespace must **differ from every `x-fern-sdk-group-name` in the spec**, or the sidebar nests two identically-labelled levels (`appointments › appointments`).

Check what the spec uses:

```bash
gh api repos/healthcare-org-app/healthcare-<name>/contents/openapi.yaml \
  --jq '.content' | base64 -d | grep -o 'x-fern-sdk-group-name: .*' | sort -u
```

Convention here: use the full service name — `appointments-service`, `prescriptions-service`. Group names are the short form, so they never collide.

### 4. Add the entry

Append to `fern/apis/healthcare-org/generators.yml`, keeping entries alphabetical:

```yaml
    - openapi:
        git:
          repo: https://github.com/healthcare-org-app/healthcare-<name>
          ref: main
          path: openapi.yaml
      namespace: <name>-service
```

**`namespace` is mandatory.** Fern merges specs on raw path keys, so without it the `/health` and `/ready` pair that every service exposes collapses into one copy and the others are dropped. Silently — `fern check` stays green and the build succeeds.

### 5. Verify by counting pages, not by running check

`fern check` is necessary but not sufficient. It reports 0 errors on a merge that drops endpoints and on a `docs.yml` API entry that cannot resolve.

Record the endpoint count **before** your change:

```bash
fern generate --docs --preview 2>&1 | grep -o 'https://[^ )]*docs.buildwithfern.com' | head -1
# then, against that URL:
curl -s "$URL/sitemap.xml" | grep -c 'api-reference/healthcare-org'
```

Add the entry, regenerate, and count again. The delta must equal the number of operations in the new spec, **including its own `/health` and `/ready`**. If it is short by exactly 2 per service, the namespace is missing or colliding.

Also confirm the new pages carry the namespace prefix:

```bash
curl -s "$URL/sitemap.xml" | grep '<name>-service/'
```

### 6. Branch and PR

Never commit to `main`. One branch and one PR per change:

```bash
git checkout main && git pull
git checkout -b add-<name>-api
# edit, verify
git commit -am "Add <name> API definition"
gh pr create --base main
```

Wait for both checks. `preview-docs` posts a preview URL as a PR comment — verify the page count there too, since that build runs against the merge result rather than your branch alone.

## Adding several at once

Add all the entries in one pass, then verify with a single preview: the expected delta is the sum of all new operations. If it is short, bisect by removing entries rather than guessing which spec collided.

## What not to do

- Do not add an `origin:` key. This project uses the `git:` ref form; `origin` only writes back to a vendored local file, which this layout does not have.
- Do not add a `docs.yml` entry per service. There is one API; namespaces do the grouping.
- Do not trust a green `fern check` as evidence the docs render correctly. Count the pages.
