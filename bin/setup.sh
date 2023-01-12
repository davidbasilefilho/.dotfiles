#!/bin/bash
sudo echo "Welcome to the Setup Script!"

echo " "
echo "Run this if you make a change in the following files: picom.conf picom.desktop and the Latte layout"
echo "These files need to be placed in other directories for them to work correctly."

echo " "
echo "Making a symlink of picom.conf in /etc/xdg/"
path=$HOME/.dotfiles/.config/picom.conf
sudo ln -sf $path /etc/xdg/picom.conf

echo " "
echo "Done! Making a symlink of picom.desktop in /usr/share/applications/"
path=$HOME/.dotfiles/.config/autostart/picom.desktop
sudo ln -sf $path /usr/share/applications/picom.desktop

echo " "
echo "Done! Making a copy of MyLayout.layout.latte"
path=$HOME/.dotfiles/.config/latte/MyLayout.layout.latte
userDir=$HOME
# get rid of the symlink stow made
sudo rm $userDir/.config/latte/MyLayout.layout.latte
sudo cp $path $HOME/.config/latte/MyLayout.layout.latte

echo " "
echo "Done! Enjoy your new desktop!"
