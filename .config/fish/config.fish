alias ..='cd ..'
alias mv='mv -i'
alias rm='rm -i'
alias cp='cp -i'
alias ls='exa'
alias la='exa -a'
alias lsa='exa -la'
alias ttpt='tt --words pt'
alias em='emacs -nw'

alias emacsclient="emacsclient -c -a 'emacs'"
alias spt="python3 ~/dev/python/spotify-tui-script/spt.py"

export EDITOR=nvim
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/lib64"

export PATH="$HOME/.emacs.d/bin:$PATH"
export PATH="$HOME/.config:$PATH"
export PATH="$HOME/.npm-global/bin:$PATH"
export PATH="$HOME/.local/bin:$PATH"
export PATH="$HOME/.cargo/bin:$PATH"
export PATH="$HOME/.dotfiles/bin:$PATH"

set -U fish_greeting

oh-my-posh init fish --config /home/basile/.config/oh-my-posh/star.omp.json | source
fastfetch
