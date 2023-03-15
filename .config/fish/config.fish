alias ..='cd ..'
alias mv='mv -i'
alias rm='rm -i'
alias cp='cp -i'
alias ls='exa -la'
alias em='emacs -nw'

export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/lib64"
export EDITOR=vim
export VISUAL=vim
export BAT_THEME="Catppuccin-mocha"

export PATH="$HOME/.emacs.d/bin:$PATH"
export PATH="$HOME/.config:$PATH"
export PATH="$HOME/.npm-global/bin:$PATH"
export PATH="$HOME/.local/bin:$PATH"
export PATH="$HOME/.cargo/bin:$PATH"
export PATH="$HOME/.dotfiles/bin:$PATH"

set -U fish_greeting

starship init fish | source

fastfetch
