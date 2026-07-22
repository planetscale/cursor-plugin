# PlanetScale Cursor Plugin

Plugin for installing the [PlanetScale MCP server](https://planetscale.com/docs/connect/mcp), [Database Skills](https://db-skills.com/), and PlanetScale skills into Cursor.

## Prerequisites

- Cursor with access to the Cursor Marketplace
- A PlanetScale account for authenticated MCP features

## Install from the Cursor Marketplace

Search for **PlanetScale** in the [Cursor Marketplace](https://cursor.com/marketplace) and install the plugin.

### Verify it loaded

Open Cursor Settings and check the MCP section to confirm the `planetscale` MCP server is listed and connected.

## Skills Source and Sync

This plugin pulls in skills from upstream PlanetScale repositories via Git submodules.

- Source repo: `https://github.com/planetscale/database-skills`
- Submodule path: `database-skills`
- Skills path: `database-skills/skills`
- Tracked branch: `main`

- Source repo: `https://github.com/planetscale/skills`
- Submodule path: `skills`
- Skills path: `skills`
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
git submodule update --init --remote database-skills skills
```

Commit the resulting submodule pointer changes in this repository.

### Automated weekly updates

GitHub Actions runs `.github/workflows/update-skills.yml` weekly and also supports manual runs (`workflow_dispatch`).

When either upstream repository has new commits, the workflow opens or updates a PR that contains only:

- The changed skills submodule pointer updates
- `.gitmodules` (if submodule metadata changed)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and pull request guidance.

## License

This project is licensed under the [Apache License 2.0](LICENSE).
