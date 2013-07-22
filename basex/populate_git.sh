#!/bin/bash

# First argument is the path to ISO files

# Second argument is the string to process...
# all (everything... slow)
# ndbc
# hads
# storet
# etc.

cd ..
git checkout master
git pull origin master
cd basex

python populate_update.py $1 $2
