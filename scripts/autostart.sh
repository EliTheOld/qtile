#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}



#starting utility applications at boot time
lxsession &
run nm-applet &
run pamac-tray &
numlockx on &
# blueman-applet &
picom --config .config/picom/picom.conf &
dunst &
#starting user applications at boot time
run volumeicon &
variety &
