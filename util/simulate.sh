#!/bin/sh

export SRCROOT=`dirname "$0"`
export SRCROOT=`dirname ${SRCROOT}`

export HALSIM_EXTENSIONS="halsim_gui" 
export LD_LIBRARY_PATH="$HOME/wpilib/2025/luabot/lib/linuxx86-64"
export DYLD_LIBRARY_PATH="$LD_LIBRARY_PATH"

exec "src/frcUserProgram" "$@"
