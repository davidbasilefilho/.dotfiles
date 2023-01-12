sudo chmod +x bin/delete-kde-configuration-files.fish

/usr/bin/env fish bin/delete-kde-configuration-files.fish

# make sure you are in the dotfiles directory:
cd ~/.dotfiles/

# make sure you have the permissions for it
sudo chmod +x bin/sync-dotfiles.sh

# run it
./bin/sync-dotfiles

systemctl --user enable emacs.service --now
