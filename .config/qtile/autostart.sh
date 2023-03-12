#!/usr/bin/env bash
picom --experimental-backends --config $HOME/.config/picom/picom.conf &
/usr/bin/emacs --daemon &
variety &
#conky -c $HOME/.config/conky/qtile/doom-one-01.conkyrc
#volumeicon & nm-applet &
