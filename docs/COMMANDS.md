# Command reference

Every command used in weeks 0–1 of the ED Roster learning project, grouped by tool. Add to it as you go.

## Shell (zsh) and files

| Command | What it does |
| --- | --- |
| `pwd` | Print the current folder. Relative paths resolve from here |
| `ls`, `ls -a` | List the folder; `-a` includes dot-files (`.venv`, `.git`, `.env`) |
| `cd <path>` | Change folder. `~` = home, `..` = up one, `.` = here |
| `mkdir -p a/b` | Make folders, parents included |
| `touch <file>` | Create an empty file (or update its timestamp) |
| `cat <file>` | Print a file |
| `echo "text" >> <file>` | Append a line. Single `>` overwrites |
| `rm -rf <folder>` | Delete, recursively, no confirmation. Used only on `.venv` |
| `mv a b` | Move or rename |
| `source ~/.zshrc` | Re-read the shell config after editing it |
| `lsof -i :8000` | Which process holds port 8000 |
| `kill <PID>` (`-9` to force) | Stop a process by id |
| `curl -v <url>` | Make an HTTP request and show the request and response headers |
| `q` (inside `less`) | Quit the pager; Space / `b` page, `/` searches |
| `Ctrl+C` | Stop the foreground process (a server) |
| `cmd1 && cmd2` | Run `cmd2` only if `cmd1` succeeded |
| `<<'EOF' … EOF` | Heredoc: feed several lines to a command, untouched by the shell |
| `code .` / `code <file>` | Open in VS Code (after installing the shell command) |

## uv (Python environments)

| Command | What it does |
| --- | --- |
| `uv init --python 3.12` | New project: `pyproject.toml`, `.python-version`, `.gitignore`, `git init` |
| `uv venv --python 3.12` | Create `.venv` with that Python. Run it in the project folder |
| `uv add fastapi uvicorn` | Add runtime dependencies to `pyproject.toml`, update `uv.lock`, install |
| `uv add --dev pytest ruff httpx` | Same, into the `dev` group (not shipped to production) |
| `uv remove --dev httpx` | The reverse |
| `uv sync` | Install exactly what `uv.lock` says. CI uses this |
| `uv pip install -r requirements-dev.txt` | pip-style install, for the answer key which has no lockfile |
| `uv run <cmd>` | Run a command inside the project venv without activating it |
| `uv run uvicorn app.main:app --reload` | Start the dev server; `module:variable`; `--reload` restarts on file save; `--port 8001` to change port |
| `uv run pytest -q` | Run tests, quiet output |
| `uv run ruff check .` | Lint the whole project |
| `uv run python -m app.seed --demo` | Run a module as a script (answer key's seed) |

## git (local history)

| Command | What it does |
| --- | --- |
| `git status` | What's changed, staged, untracked; which branch; ahead/behind |
| `git add <file>` / `git add .` / `git add -A` | Stage a file / everything here / everything incl. deletions |
| `git commit -m "msg"` | Snapshot the staged changes with a message |
| `git log --oneline` | History, one line per commit |
| `git log --oneline origin/main..main` | Commits on local `main` that GitHub doesn't have |
| `git diff`, `git diff --stat`, `git diff origin/main -- <file>` | Unstaged changes / summary / compare a file against GitHub |
| `git switch main` | Move to a branch |
| `git switch -c <name>` | Create a branch and move to it |
| `git branch -m master main` | Rename a branch |
| `git branch -d <name>` | Delete a merged branch |
| `git pull` | Fetch from GitHub and merge into the current branch |
| `git fetch` | Fetch only; update what git knows about GitHub without touching your files |
| `git push` | Send the current branch's commits to GitHub |
| `git push -u origin <branch>` | First push of a new branch; `-u` links it so plain `git push` works later |
| `git push origin --delete <branch>` | Delete a branch on GitHub |
| `git reset --soft HEAD~1` | Undo the last commit, keep the changes staged |
| `git reset --hard origin/main` | Make local match GitHub exactly. Discards local commits and edits |
| `git config --global core.editor "code --wait"` | Use VS Code for commit messages |

## gh (GitHub from the terminal)

| Command | What it does |
| --- | --- |
| `gh auth login` | Sign the CLI in to GitHub |
| `gh repo create <name> --public --source=. --push` | Create the GitHub repo from the current folder and push |
| `gh repo edit --default-branch main` | Set the default branch |
| `gh pr create --fill` | Open a PR for the current branch, title and body from the commits |
| `gh pr checks --watch` | Wait for CI on the current PR and report |
| `gh pr status` / `gh pr view --web` | Your PRs at a glance / open this branch's PR in the browser |
| `gh pr merge --squash --delete-branch` | Merge as one commit, delete the branch, switch to `main` and pull |
| `gh pr close --delete-branch` | Close without merging |
| `gh run watch` / `gh run view --log-failed` | Stream a workflow run / show only the failing step's log |
| `gh api -X PUT <endpoint> --input -` | Call the GitHub API directly; body from stdin |

## Claude Code

| Command or key | What it does |
| --- | --- |
| `claude` | Start a session in the current repo; reads `CLAUDE.md` |
| `Shift+Tab` | Cycle permission modes: plan (read-only) → manual → accept edits |
| `/model`, `/config`, `/clear` | Switch model; settings; start a fresh context |
| `Cmd+Esc` (VS Code) | Quick-launch Claude Code |
| `Cmd+Option+K` (VS Code) | Reference the open file or selection in your prompt |

## VS Code

| Key | What it does |
| --- | --- |
| `` Ctrl+` `` | Toggle the terminal panel; `` Ctrl+Shift+` `` opens a new one |
| `Cmd+S` / `Cmd+Option+S` | Save / save all |
| `F1` or View → Command Palette | Run any command by name (`Cmd+Shift+P` is taken by Perplexity on this Mac) |
| `Cmd+T` (Terminal.app) | New tab |

## Installs and one-offs

| Command | What it does |
| --- | --- |
| `brew install <pkg>` / `brew install --cask <app>` | Install a tool / an app |
| `brew install starship` + `eval "$(starship init zsh)"` in `.zshrc` | The prompt that shows folder, branch, status, venv |
| `setopt interactivecomments` in `.zshrc` | Let `#` start a comment at the prompt |
| Command Palette → Shell Command: Install 'code' command in PATH | Enables `code` in the terminal |

## The loop every change follows

```bash
git switch main && git pull          # start from the latest main
git switch -c <short-name>           # one branch per concern
# edit, test
git add -A && git commit -m "What and why"
git push -u origin <short-name>
gh pr create --fill
gh pr checks --watch
gh pr merge --squash --delete-branch # back on main, pulled, branch gone
```
