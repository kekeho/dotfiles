#!/usr/bin/env bash
mv -f init.coffee snippets.cson config.cson keymap.cson styles.less ~/.atom/
apm install --packages-file atomPackages.list

