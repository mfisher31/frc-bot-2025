#!/bin/sh

set -e

meson install --destdir=stage --quiet

export SRCROOT=`dirname "$0"`
export SRCROOT=`dirname ${SRCROOT}`

export HALSIM_EXTENSIONS="halsim_gui" 
export LD_LIBRARY_PATH="src:$HOME/wpilib/2025/luabot/lib/linuxx86-64:stage/lib/x86_64-linux-gnu"

export LUA_PATH="stage/share/luajit-2.1/?.lua;subprojects/luabot/bindings/lua/?.lua;stage/share/lua/5.1/?.lua;$SRCROOT/robot/?.lua"
export LUA_CPATH="stage/lib/lua/5.1/?.so"
subprojects/luabot/luabot "$SRCROOT/robot/simulate.lua"
