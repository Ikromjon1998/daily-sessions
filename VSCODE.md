# VS Code Cheatsheet — Python / Exercism

macOS shortcuts. `⌘` = Cmd, `⌥` = Option, `⇧` = Shift, `⌃` = Ctrl.

## 1. Setup (once)

```bash
cd ~/dev/personal/exercism/python/daily-sessions
code .
```

1. Install the recommended extensions: `⌘⇧P` → **Extensions: Show Recommended Extensions** → Install all.
   (Python, Pylance, Ruff, Mypy, GitLens, Error Lens, Exercism.)
2. Select the interpreter: `⌘⇧P` → **Python: Select Interpreter** → `./.venv/bin/python`.
   Bottom-right status bar must show the `.venv` interpreter (currently Python 3.14).
3. Open a new terminal (`` ⌃` ``) — the venv activates automatically.
4. `⌘⇧P` → **Test: Refresh Tests** → the flask icon (Testing sidebar) lists every exercise.

`.vscode/settings.json` already does the rest: interpreter, pytest discovery, and
**practice mode** — see §1a.

## 1a. Practice mode (why nothing autocompletes)

`.vscode/settings.json` deliberately turns off, for this workspace only:

| Off | Setting | Why |
|-----|---------|-----|
| Copilot ghost text | `github.copilot.enable: {"*": false}`, `editor.inlineSuggest.enabled: false` | Copilot is **built into VS Code 1.99+** — nothing to uninstall. It writes the whole exercise for you. |
| Autocomplete popup | `editor.quickSuggestions`, `suggestOnTriggerCharacters`, `wordBasedSuggestions`, `tabCompletion`, `acceptSuggestionOnEnter` | Finishing your line for you is the thing you are here to learn. |
| Format on save | `editor.formatOnSave`, `editor.codeActionsOnSave: {}`, `files.trimTrailingWhitespace` | Keeps the downloaded Exercism stub byte-for-byte as shipped. |
| Strict squiggles | `python.analysis.typeCheckingMode: "basic"`, inlay hints off | An untouched stub full of `pass` shouldn't look broken. |

Still available on demand:

- `⌃Space` — force the completion popup open when you genuinely want a lookup.
- `⌥⇧F` — format the current file once.
- `make check` — `ruff format` + `ruff check --fix` + `mypy` + `pytest`. Run it
  **after** the tests go green, before `exercism submit`.

Using **Cursor** instead of VS Code? Cursor Tab is not controlled by these keys —
turn it off in *Cursor Settings → Tab*, or add
`"cursor.cpp.disabledLanguages": ["python"]`.

## 2. Daily loop inside VS Code

| Step | How |
|------|-----|
| Download exercise | terminal: `exercism download --track=python --exercise=<name>` |
| Open stub + tests side by side | `⌘P` → type `two_fer` → open `.py`, then `⌘\` to split, open `_test.py` in the other pane |
| Run one test file | click ▶ in the gutter next to the test class, or `⌘;` `⌘A` (run all) |
| Run tests on save (watch mode) | Testing sidebar → ⋯ → **Run tests on save** — or `pytest --lf -q` in terminal |
| Debug a failing test | click the 🐞 next to the test; set breakpoint with `F9`; step `F10` / into `F11` |
| Format / lint / imports | manual only: `⌥⇧F`, or `make check` before submitting (see §1a) |
| See problems | `⌘⇧M` (Problems panel) — Error Lens also shows them inline |
| Submit | terminal: `cd python/<name> && exercism submit` — full flow in [README § Submitting](README.md#submitting) |
| Commit | `⌃⇧G` → stage → message → `⌘Enter` |

## 3. Shortcuts worth memorising

Navigation
- `⌘P` quick open file · `⌘⇧O` jump to symbol in file · `⌘T` symbol in workspace
- `F12` go to definition · `⌥F12` peek definition · `⇧F12` find references
- `⌘⇧E` explorer · `⌘⇧F` search in files · `⌘B` toggle sidebar · `⌘J` toggle panel

Editing
- `F2` rename symbol everywhere (safe refactor)
- `⌘.` quick fix / code action (add import, add type hint, Ruff auto-fix)
- `⌥↑` / `⌥↓` move line · `⌥⇧↓` duplicate line · `⌘⇧K` delete line
- `⌘D` select next occurrence · `⌘⇧L` select all occurrences (multi-cursor)
- `⌘/` toggle comment · `⌘K ⌘F` format selection
- `⌃Space` trigger completion · `⌘⇧Space` parameter hints

Testing / running
- `⌘; ⌘A` run all tests · `⌘; ⌘F` run tests in current file · `⌘; ⌘L` re-run last run
- `⌘; ⌘E` run failed tests · `⌘; ⌘D` debug last run
- `F5` debug current file · `⇧⌘⏎`… (see Run and Debug)

Terminal
- `` ⌃` `` toggle terminal · `` ⌃⇧` `` new terminal · `⌘\` split terminal

## 4. Python best practices — with VS Code doing the work

**Types everywhere.** Hover a symbol to see its inferred type; inlay hints show
return/variable types greyed out. If Pylance shows `Unknown`, add a hint.
Strict mode will flag missing annotations — treat every yellow squiggle as a TODO.

**Let Ruff teach you.** Hover a squiggle → read the rule (e.g. `UP032`, `SIM108`),
press `⌘.` → **Fix**. The rule codes map to Python idioms:
- `UP*` → modern syntax (f-strings, `list[int]`, `X | None`, `match`)
- `SIM*` → simplify (`if x: return True else: return False` → `return x`)
- `B*` → bug-prone patterns (mutable default args, `except:` bare)
- `N*` → naming (snake_case funcs, PascalCase classes, UPPER constants)
- `D*` → docstrings (one-liner is fine; `"""Return the greeting for name."""`)

**Read the test before the stub.** Open `_test.py` first, fold everything (`⌘K ⌘0`),
unfold one test at a time (`⌘K ⌘J` unfolds all). Write code for one test, run it
(gutter ▶), move on.

**Use the debugger instead of print.** Breakpoint (`F9`) → 🐞 on the test →
inspect variables in the left panel, evaluate expressions in the Debug Console.

**Refactor after green.** Tests pass → `F2` to rename to better names, `⌘.` to
extract, convert loops to comprehensions. Re-run tests. Then submit.

**Snippets.** Type `def` → `Tab` for a function template; `class` → `Tab`;
`if __name__` → `Tab`. Add your own in `⌘⇧P` → **Snippets: Configure Snippets → python**.

**Docstring on demand.** Type `"""` under a `def` and press `Enter` — Pylance
generates the skeleton.

## 5. Handy commands (`⌘⇧P`)

- **Python: Select Interpreter** — fix "module not found" 90% of the time
- **Python: Configure Tests** — re-run if Test Explorer is empty
- **Developer: Reload Window** — when Pylance gets confused
- **Ruff: Fix all auto-fixable problems**
- **Ruff: Format document**
- **View: Toggle Zen Mode** (`⌘K Z`) — one exercise, no distractions

## 6. Troubleshooting

| Symptom | Fix |
|---------|-----|
| Tests not discovered | interpreter is `.venv`? → **Test: Refresh Tests**; check `python.testing.pytestArgs` points at `python` |
| Terminal doesn't show `(.venv)` | close terminal, open a new one after selecting interpreter |
| Every docstring line underlined red | Ruff had no docstring convention set, so the numpy rules (`D406`/`D407`/`D413`) fought Exercism's Google-style stubs. Fixed by `[tool.ruff.lint.pydocstyle] convention = "google"` in `pyproject.toml` |
| Red "Function is missing a type annotation" on an untouched stub | Mypy strict, downgraded to blue Info in `.vscode/settings.json`. Real verdict: `make type` |
| Ruff not formatting | expected — format on save is off (§1a). Use `⌥⇧F` or `make fmt` |
| Autocomplete/AI still suggesting | reload window; check `⌘⇧P` → **Preferences: Open User Settings (JSON)** isn't re-enabling `editor.inlineSuggest.enabled` (user settings lose to workspace, but a *profile* can differ) |
| Pylance too strict for a quick hack | line-level: `# type: ignore[code]`; never lower `typeCheckingMode` globally |
| `exercism` not found in terminal | `brew install exercism`; restart terminal |
