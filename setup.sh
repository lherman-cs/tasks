#!/bin/bash

INSTL_PATH="$(pwd)"
SRC_PATH="${INSTL_PATH}/src"
LOG_PATH="${INSTL_PATH}/log"

# Generate settings.py
echo "TASKS_PATH = '${LOG_PATH}/tasks.pkl'" >> ${SRC_PATH}/settings.py 
echo "MARGIN = 80" >> ${SRC_PATH}/settings.py 

# Create an alias in .bash_profile
echo "Creating a new alias"
echo "alias tasks='cd ${INSTL_PATH} && ./run.sh'" >> $HOME/.bash_profile
source $HOME/.bash_profile

echo "Done!"

echo
echo "Now try to use the command: tasks"
