#!/bin/sh

export SRCROOT=`dirname "$0"`
export SRCROOT=`dirname ${SRCROOT}`

export HALSIM_EXTENSIONS="halsim_gui" 
export LD_LIBRARY_PATH="${SRCROOT}/build/install/frcUserProgram/linuxx86-64/release/lib"
export DYLD_LIBRARY_PATH="${SRCROOT}/build/install/frcUserProgram/osxuniversal/release/lib"

exec "$SRCROOT/build-meson/src/frcUserProgram" "$@"
