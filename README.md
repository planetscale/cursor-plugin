# PlanetScale Cursor Plugin

Install the hosted [PlanetScale MCP server](https://planetscale.com/docs/connect/mcp), [Database Skills](https://db-skills.com/), and PlanetScale operational skills in Cursor from one plugin.

The MCP server provides authenticated access to PlanetScale organizations, databases, branches, schema, and Insights data. The two skill packs add database guidance and PlanetScale-specific operating workflows.

## Prerequisites

- Cursor with access to the Cursor Marketplace
- A PlanetScale account for authenticated MCP features

## Install from the Cursor Marketplace

Search for **PlanetScale** in the [Cursor Marketplace](https://cursor.com/marketplace) and install the plugin.

### Verify it loaded

Open Cursor Settings and check the MCP section to confirm the `PlanetScale` MCP server is listed and connected. Confirm that skills from both `database-skills/skills` and `skills` are available to the agent.

## Skills source and sync

This plugin tracks two upstream PlanetScale repositories as Git submodules:

| Source | Submodule path | Skills path | Branch |
| --- | --- | --- | --- |
| [`planetscale/database-skills`](https://github.com/planetscale/database-skills) | `database-skills` | `database-skills/skills` | `main` |
| [`planetscale/skills`](https://github.com/planetscale/skills) | `skills` | `skills` | `main` |

### Local bootstrap

Clone with submodules:

```bash
git clone --recurse-submodules https://github.com/planetscale/cursor-plugin.git
cd cursor-plugin
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

GitHub Actions runs `.github/workflows/update-skills.yml` weekly and also supports manual runs (`workflow_dispatch`). When either upstream repository changes, the workflow opens or updates a focused pull request containing the changed submodule pointers.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and pull request guidance. Submit changes to skill content in its upstream repository rather than editing a submodule here.

## License

The plugin wrapper and configuration are licensed under the [Apache License 2.0](LICENSE). The bundled skill repositories retain their MIT licenses; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
