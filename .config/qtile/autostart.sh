#!/usr/bin/env bash
picom --config $HOME/.config/picom/picom.conf &
/usr/bin/emacs --daemon &
variety &
jamesdsp &
#conky -c $HOME/.config/conky/qtile/doom-one-01.conkyrc
#volumeicon & nm-applet &
