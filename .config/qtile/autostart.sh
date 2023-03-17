#!/usr/bin/env bash
picom --experimental-backends --config $HOME/.config/picom/picom.conf &
emacs --daemon & # emacs daemon for emacsclient
nitrogen --restore & # wallpaper setter
setxkbmap -option ctrl:swapcaps &
lxsession & # polkit
sleep 5 && xmodmap ~/.Xmodmap &
