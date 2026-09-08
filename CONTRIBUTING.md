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

Release-please owns versioning and tagging. The only way to cut a release is to approve and merge release-please's own PR from `release-please--branches--main` with the `autorelease: pending` label. Never hand-author or recreate a release PR: release-please then fails to find the merged release PR and silently skips tagging and asset upload, as happened with 1.1.0. The marketplace serves the newest release's `planetscale-cursor-plugin.tar.gz`, so a version bump without a release changes nothing for users. If a release exists without its asset, or a tag was missed, run the Release workflow manually via `workflow_dispatch` with a `vMAJOR.MINOR.PATCH` tag; re-dispatching an existing tag rebuilds the archive from that tag, not from the selected ref.

## MCP packaging and Grok Bot validation

The plugin manifest embeds the MCP configuration using Cursor's supported
[inline `mcpServers` format](https://cursor.com/docs/reference/plugins).
This lets a manifest reader obtain the endpoint without resolving a separate
file from a release archive. Keep `.mcp.json` as the equivalent standalone
configuration and update both definitions together. Run:

```bash
python3 script/validate-mcp.py
python3 script/validate-mcp.py planetscale-cursor-plugin.tar.gz
```

The release workflow checks both the checkout and the archive before upload.

This packaging change is a proposed mitigation for Grok Bot installations that
load skills without registering the MCP server. It does not override Cursor's
marketplace metadata. At v1.3.0, plugin 741's MCP `sourceUrl` points to a GitHub
release page. Grok Bot 0.44.0's bundled public-config fallback only converts
GitHub `/blob/<ref>/<path>` URLs. Its active installation path delegates to
`InstallUserPlugin`, so the fallback limitation alone does not establish the
backend failure.

Before treating this as a confirmed fix, validate the candidate through the
marketplace: `GetPluginMcpConfig` must return the PlanetScale endpoint;
`GetAvailableMcpServers` must contain an enabled HTTP server after installation;
and Grok Bot must emit the Connect/Authorize card. If the config is still empty,
ask Cursor to resolve the release asset and `.mcp.json` path, or provide a direct
immutable `/blob/<commit>/.mcp.json` component source URL. The existing release
archive is still needed to distribute the skills from submodules.
