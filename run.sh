#!/bin/bash

HOMEDIR="/home/xxx"
SCRIPTSDIR="scripts"
VENVDIR="hdmi_keepalive/venv"
EXECDIR="$HOMEDIR/$SCRIPTSDIR/$VENVDIR"

source $EXECDIR/bin/activate


python3 hdmi_keepalive.py "$@" 
