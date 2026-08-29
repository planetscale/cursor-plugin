# Contributing

Thanks for contributing to the PlanetScale plugin.

## Setup

Clone the repository with Git submodules, or initialize them in an existing checkout:

```bash
git submodule update --init --recursive
```

## Skill changes

Submit PlanetScale operating skill changes to [`planetscale/skills`](https://github.com/planetscale/skills) and database skill changes to [`planetscale/database-skills`](https://github.com/planetscale/database-skills). This repository should only update the corresponding submodule references.

## Pull requests

- Keep changes focused.
- Describe the change and the validation performed.
- Update documentation when installation or behavior changes.
- Do not include credentials, tokens, customer data, or other sensitive information.

## Releases

Release-please owns versioning and tagging. The only way to cut a release is to approve and merge release-please's own PR from `release-please--branches--main` with the `autorelease: pending` label. Never hand-author or recreate a release PR: release-please then fails to find the merged release PR and silently skips tagging and asset upload, as happened with 1.1.0. The marketplace serves the newest release's `planetscale-cursor-plugin.tar.gz`, so a version bump without a release changes nothing for users. If a release exists without its asset, or a tag was missed, run the Release workflow manually via `workflow_dispatch` with the tag.
