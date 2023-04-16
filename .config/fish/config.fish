alias mv='mv -i'
alias rm='rm -i'
alias cp='cp -i'
alias ls='exa -la'
alias em='emacs -nw'

# DNF5 instead of DNF4 (will not be needed in F39)
alias dnf="sudo dnf5"

# Nix Package Manager
alias nix-in="nix-env -iA"
alias nix-rm="nix-env -e"
alias nix-ls="nix-env -q"
alias nix-up="nix-env -uA"
alias nix-se="nix-env -qaP"

export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/lib64"
export EDITOR=vim
export VISUAL=vim
export BAT_THEME="Catppuccin-mocha"
export XCURSOR_PATH="$HOME/.icons:$HOME/.nix-profile/share/icons/:$XCURSOR_PATH"

export PATH="$HOME/.emacs.d/bin:$PATH"
export PATH="$HOME/.config:$PATH"
export PATH="$HOME/.npm-global/bin:$PATH"
export PATH="$HOME/.local/bin:$PATH"
export PATH="$HOME/.cargo/bin:$PATH"
export PATH="$HOME/.dotfiles/bin:$PATH"

set -U fish_greeting

starship init fish | source

fastfetch
