#!/bin/bash

INSTL_PATH="$(pwd)"

# Create an alias in .bash_profile
echo "Creating a new alias"
echo "alias tasks='cd ${INSTL_PATH} && ./run.sh'" >> $HOME/.bash_profile
source $HOME/.bash_profile

echo "Done!"

echo
echo "Now try to use the command: tasks"
