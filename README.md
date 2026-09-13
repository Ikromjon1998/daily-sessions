# Daily Exercism Python Sessions

Local workspace for the [Exercism Python track](https://exercism.org/tracks/python).
Exercises live in `python/<exercise-name>/`.

## One-time setup

```bash
# 1. Exercism CLI (already configured – token + workspace)
exercism configure --workspace="$(pwd)"      # only if you move the repo

# 2. Python environment (one venv for the whole repo)
python3 -m venv .venv          # or: uv venv
source .venv/bin/activate
pip install pytest ruff mypy   # or: uv pip install pytest ruff mypy
```

Check it works: `pytest --version && ruff --version`.

## Every session

```bash
cd ~/dev/personal/exercism/python/daily-sessions
source .venv/bin/activate                       # activate env (prompt shows "(.venv)")

exercism download --track=python --exercise=<name>   # e.g. two-fer
cd python/<name>
cat <name>.py <name>_test.py                    # read stub + tests first
```

Write the solution in `<name>.py`, then:

```bash
pytest                      # run tests
make check                  # format + lint + type-check + tests (from repo root or exercise dir)
exercism submit <name>.py   # upload solution
```

Or `exercism submit` with no args submits every solution file in the current exercise.

After submitting, open the exercise on exercism.org, compare with community
solutions, and add one line to `NOTES.md`: what you learned.

## Tooling

| Command                 | What it does                                  |
|-------------------------|-----------------------------------------------|
| `pytest`                | run tests in current folder                   |
| `ruff format .`         | auto-format (Black style)                     |
| `ruff check --fix .`    | lint: bugs, naming, imports, modern syntax    |
| `mypy .`                | static type check (strict)                    |
| `make check`            | all of the above in one go                    |

Config lives in `pyproject.toml` at the repo root and applies to every exercise.

## Rules I follow

- Type hints and a one-line docstring on every function.
- After tests pass, spend 5 min making it Pythonic (comprehensions, `dataclass`,
  `enumerate`/`zip`, `pathlib`, `match`).
- One exercise per session, 20–30 min. Stop while it's still fun.
- Commit each solved exercise: `git add python/<name> NOTES.md && git commit -m "solve <name>"`.

## Useful

```bash
deactivate                      # leave the venv
exercism configure              # show current CLI config
exercism troubleshoot           # CLI diagnostics
exercism download --track=python --exercise=<name> --force   # re-download / reset stub
```
