alias ..='cd ..'
alias mv='mv -i'
alias rm='rm -i'
alias cp='cp -i'
alias ls='exa -la'
alias ttpt='tt --words pt'
alias em='emacs -nw'
alias cat="bat"

alias emacsclient="emacsclient -c -a 'emacs'"
alias spt="python3 ~/dev/python/spotify-tui-script/spt.py"

export EDITOR=vim
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/lib64"

export PATH="$HOME/.emacs.d/bin:$PATH"
export PATH="$HOME/.config:$PATH"
export PATH="$HOME/.npm-global/bin:$PATH"
export PATH="$HOME/.local/bin:$PATH"
export PATH="$HOME/.cargo/bin:$PATH"
export PATH="$HOME/.dotfiles/bin:$PATH"
export PATH="$HOME/.spicetify:$PATH"
export NVM_DIR="$HOME/.nvm"

set -U fish_greeting

fastfetch
