# CLAUDE.md

Read at the start of every session. Keep it short: only what should shape
decisions in every session. Replace the parts in <angle brackets>, and add a
line whenever the agent gets something wrong twice.

## Project
<mypackage: one or two sentences on what it computes, and for what.>
Spec, theory and validation documents live in docs/ (Quarto).
<Priorities, e.g. "Correctness first, then speed.">

## Done means
- `pixi run check` passes (ruff, mypy, pytest)
- `pixi run docs` renders without errors
- New behaviour has a test; new physics has a validation document in docs/validation/

## Conventions
- <Units, e.g. "Atomic units internally; convert only at input and output">
- <Array layouts, e.g. "Positions have shape (n_atoms, 3)">
- Type-annotate all functions
- One commit per logical change; the message says why
- Add dependencies with `pixi add --pypi <package>` so they go in pyproject.toml

## Never
- Tune a constant or tolerance to make a test pass. Stop and report the discrepancy.
- Skip, delete or weaken a failing test
- Silence a ruff or mypy error with an ignore comment without saying why

## Stop and ask
- After three failed attempts at the same fix
- If the spec in docs/ looks wrong or incomplete
- Before changing a public function's signature
