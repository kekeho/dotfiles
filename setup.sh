#!/usr/bin/env bash
wget https://github.com/kekeho/dotfiles/archive/master.zip
cd dotfiles-master/
mv -f init.coffee snippets.cson config.cson keymap.cson styles.less ~/.atom/
apm install --packages-file atomPackages.list
cd ../
rm -r dotfiles-master

