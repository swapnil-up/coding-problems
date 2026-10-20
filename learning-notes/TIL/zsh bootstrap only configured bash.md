# zsh bootstrap only configured bash

Date: 2026-07-07 22:35

---

A dotfiles bootstrap that writes `.bashrc`/`.profile` does nothing in zsh. Two separate shadows:

- Bash login shells read `~/.bash_profile` first; a stale one prevents the stowed `~/.profile` from loading. Make it `source ~/.profile`.
- zsh reads `~/.zshrc` for interactive shells and `~/.zprofile` for login shells. If only `.zprofile` exists (e.g. one `PATH` export), the shell is otherwise bare.

Bridge the existing bash config and add zsh-native tool init:

```zsh
# ~/.zshrc
source ~/.bashrc 2>/dev/null
eval "$(starship init zsh)"
eval "$(zoxide init zsh)"

HISTSIZE=10000
SAVEHIST=10000
setopt share_history
```

`source ~/.bashrc` will emit harmless warnings for bash-only builtins (`shopt`, `bind`); redirect stderr if they are noisy. Check `echo $SHELL` and `ps -p $$` before editing bash files.
