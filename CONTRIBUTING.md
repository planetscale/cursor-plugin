# Contributing

Thanks for helping improve the PlanetScale plugin.

## Before you begin

- Search the existing issues and pull requests before opening a new one.
- Use an issue for bug reports or proposed behavior changes.
- Keep pull requests focused on one change.

## Development setup

Clone the repository with its skill submodules:

```bash
git clone --recurse-submodules <repository-url>
cd <repository-directory>
```

If the repository is already cloned, initialize the submodules:

```bash
git submodule update --init --recursive
```

## Updating skills

The `database-skills` and `skills` directories are Git submodules. Do not edit their contents in this repository. Submit source changes upstream, then update the submodule pointers here:

```bash
git submodule sync --recursive
git submodule update --init --remote database-skills skills
```

## Pull requests

- Explain the user-facing reason for the change.
- Include validation steps and results.
- Update documentation when behavior or installation changes.
- Do not include credentials, access tokens, customer data, or other sensitive information.

By contributing, you agree that your contributions will be licensed under the Apache License 2.0.
