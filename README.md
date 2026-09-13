# Daily Exercism Python Sessions

Local workspace for the [Exercism Python track](https://exercism.org/tracks/python).
Exercises live in `python/<exercise-name>/`.

## One-time setup

```bash
# 1. Exercism CLI (already configured – token + workspace)
exercism configure --workspace="$(pwd)"      # only if you move the repo

# 2. Python environment (one venv for the whole repo)
uv venv                                  # or: python3 -m venv .venv
source .venv/bin/activate
uv pip install -r requirements-dev.txt   # or: pip install -r requirements-dev.txt
```

Tool versions are pinned in `requirements-dev.txt` so that local and CI always
agree. To upgrade one, bump the pin, run `make check`, and commit the pin
together with any fixes the new version demands.

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
pytest        # run tests
make check    # format + lint + type-check + tests (from repo root or exercise dir)
```

Then submit — see below.

## Submitting

Submit only after `make check` is green. Run it from **inside the exercise
directory**:

```bash
cd python/black-jack
exercism submit                 # submits the exercise's solution file(s)
exercism submit black_jack.py   # or name the files explicitly
```

With no arguments the CLI submits the exercise's *default solution files* —
the list under `files.solution` in `.exercism/config.json`. For `black-jack`
that is exactly `black_jack.py`, so the bare form is what you want almost
every time.

Note what is **not** sent: the `_test.py` file, `README.md`, and `HINTS.md`
are Exercism's, not yours. Editing them locally is fine (they are overwritten
on re-download) but they never reach the server.

On success the CLI prints a URL to the submitted solution. Open it and:

1. **Mark as complete** — this unlocks the exercise's community solutions.
2. **Compare** two or three community solutions against yours. This is the
   part that actually teaches; skipping it wastes the exercise.
3. Add one line to `NOTES.md`: what you learned.
4. Commit: `git add python/<name> NOTES.md && git commit -m "solve <name>"`

Submitting again after a change creates a new iteration rather than replacing
the old one, so it is safe to submit, read community solutions, refactor, and
submit a second time.

### If submit fails

| Message | Cause |
|---------|-------|
| `no exercise found` | You are not inside the exercise directory, or the exercise was never downloaded. `cd python/<name>` first. |
| `not authenticated` / 401 | Token missing. `exercism configure --token=<token>` from [your settings page](https://exercism.org/settings/api_cli). |
| Submits to the wrong workspace | `exercism configure --workspace="$(pwd)"` from the repo root. Needed after moving or renaming this folder. |

## Tooling

| Command                 | What it does                                  |
|-------------------------|-----------------------------------------------|
| `pytest`                | run tests in current folder                   |
| `ruff format .`         | auto-format (Black style)                     |
| `ruff check --fix .`    | lint: bugs, naming, imports, modern syntax    |
| `mypy .`                | static type check (strict)                    |
| `make check`            | all of the above in one go                    |

Config lives in `pyproject.toml` at the repo root and applies to every exercise.

`make check` also runs in CI on every push and pull request
(`.github/workflows/check.yml`), against the pinned versions in
`requirements-dev.txt` and the same Python version as the local venv.

## Rules I follow

- Type hints and a one-line docstring on every function.
- After tests pass, spend 5 min making it Pythonic (comprehensions, `dataclass`,
  `enumerate`/`zip`, `pathlib`, `match`).
- One exercise per session, 20–30 min. Stop while it's still fun.
- Commit each solved exercise (see [Submitting](#submitting) for the full flow).

## Useful

```bash
deactivate                      # leave the venv
exercism configure              # show current CLI config
exercism troubleshoot           # CLI diagnostics
exercism download --track=python --exercise=<name> --force   # re-download / reset stub
```
