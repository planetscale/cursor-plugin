#!/usr/bin/env python3
"""Validate Cursor default MCP discovery in the checkout or a release archive."""

import json
from pathlib import Path
import sys
import tarfile


MANIFEST = ".cursor-plugin/plugin.json"
CONFIG = "mcp.json"


def validate(read_json):
    manifest = read_json(MANIFEST)
    config = read_json(CONFIG)
    if "mcpServers" in manifest:
        raise ValueError("Manifest must use default discovery of root mcp.json")
    servers = config.get("mcpServers", {})
    if set(servers) != {"PlanetScale"}:
        raise ValueError("Expected exactly one PlanetScale MCP server")
    if servers["PlanetScale"] != {"url": "https://mcp.pscale.dev/mcp/planetscale"}:
        raise ValueError("Unexpected PlanetScale MCP endpoint or configuration")


def main():
    if len(sys.argv) > 2:
        raise ValueError("Usage: python3 script/validate-mcp.py [release.tar.gz]")
    if len(sys.argv) == 2:
        with tarfile.open(sys.argv[1], "r:gz") as archive:
            def read_json(name):
                member = archive.getmember(name)
                if not member.isfile():
                    raise ValueError(f"Archive member must be a regular file: {name}")
                with archive.extractfile(member) as file:
                    return json.load(file)
            validate(read_json)
    else:
        root = Path(__file__).resolve().parent.parent
        validate(lambda name: json.loads((root / name).read_text()))
    print("MCP configuration validated")


if __name__ == "__main__":
    try:
        main()
    except (OSError, KeyError, ValueError, tarfile.TarError) as error:
        sys.exit(f"MCP validation failed: {error}")
