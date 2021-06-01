#!/bin/bash

function set_volume()
{
    amixer -c 1 set Speaker $1 >/dev/null
}

vol=50
echo "Set volume: $vol"
set_volume $vol
