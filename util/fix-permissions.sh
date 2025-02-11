#!/bin/bash
user=$1
if [ -z "$user" ]; then
    user=$USER
fi

chown -R $user:$user vendordeps/sdk
