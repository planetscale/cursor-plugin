# PlanetScale Cursor Plugin

Plugin for installing the [PlanetScale MCP server](https://planetscale.com/docs/connect/mcp) and [Database Skills](https://db-skills.com/) into Cursor.

## Install from the Cursor Marketplace

Search for **PlanetScale** in the [Cursor Marketplace](https://cursor.com/marketplace) and install the plugin.

### Verify it loaded

Open Cursor Settings and check the MCP section to confirm the `planetscale` MCP server is listed and connected.

## Skills Source and Sync

This plugin pulls in skills from the upstream `planetscale/database-skills` repository via the `database-skills` Git submodule.

- Source repo: `https://github.com/planetscale/database-skills`
- Submodule path: `database-skills`
- Tracked branch: `main`

### Local bootstrap

Clone with submodules:

```bash
git clone --recurse-submodules https://github.com/planetscale/cursor-plugin.git
```

If you already cloned without submodules:

```bash
git submodule update --init --recursive
```

### Manual one-off update

To pull the latest upstream skills into this repository:

```bash
git submodule sync --recursive
git submodule update --init --remote database-skills
```

Commit the resulting submodule pointer change in this repository.

### Automated weekly updates

GitHub Actions runs `.github/workflows/update-skills.yml` weekly and also supports manual runs (`workflow_dispatch`).

When `database-skills` has new commits, the workflow opens or updates a PR that contains only:

- The `database-skills` submodule pointer update
- `.gitmodules` (if submodule metadata changed)
