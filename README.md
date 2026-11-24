# Agentic package template

A starting point for a scientific Python package developed with an AI agent
such as Claude Code. Tests, linting and type checking are configured, so the
agent and you get the same pass/fail signal after every change, and a Quarto
site in `docs/` holds the spec and the validation documents.

| Tool | What it checks | Run it with |
|---|---|---|
| [pytest](https://docs.pytest.org) + [hypothesis](https://hypothesis.readthedocs.io) | Does the code do what the tests say? | `pixi run test` |
| [ruff](https://docs.astral.sh/ruff) | Common mistakes and formatting | `pixi run lint` |
| [mypy](https://mypy.readthedocs.io) | Type annotations and interfaces | `pixi run typecheck` |
| [Quarto](https://quarto.org) | Validation documents run on real examples | `pixi run docs` |

`pixi run check` runs the first three. CI runs it, and renders `docs/`, on
every push.

## Getting started

1. Click **Use this template** on GitHub to make your own copy, and clone it.
   Install [pixi](https://pixi.sh) if you don't have it.
2. Rename the package from `mypackage` to your own name:
   - the folder `src/mypackage/`
   - `name` under `[project]`, and the `mypackage = { path = ".", ... }` line,
     in `pyproject.toml`
   - the imports in `tests/` and `docs/`, and the title in `docs/_quarto.yml`

   Or ask Claude Code to do it.
3. Run `pixi run check` and `pixi run docs`. Both should pass.
4. Fill in `CLAUDE.md`: what the project is, and your conventions (units,
   array shapes). Replace the parts in `<angle brackets>`.
5. Delete the example code (`src/mypackage/units.py`, `tests/test_units.py`,
   `docs/validation/units.qmd`) once you have your own.

## Layout

```
pyproject.toml   package metadata, pixi environment and tasks, tool configuration
CLAUDE.md        instructions Claude Code reads at the start of every session
src/mypackage/   the package
tests/           pytest tests
docs/            Quarto site: spec, theory, validation documents
```

## Adding dependencies

```bash
pixi add --pypi scipy            # a dependency of the package (goes in [project])
pixi add --pypi --feature dev pytest-cov   # a development tool
pixi add some-conda-package      # from conda-forge, e.g. compilers or non-Python libraries
```

## Using uv instead of pixi

The `[project]` table is standard, so `uv sync` and `uv run pytest` also work.
You don't get the pixi tasks or Quarto, so install Quarto yourself.

## Claude Code skills

`.claude/settings.json` enables the group's
[git plugin](https://github.com/tolborg-group/group-skills). Run
`pixi run setup-claude` once to install it, then `pixi run sync` to commit,
pull and push with Claude's help.
