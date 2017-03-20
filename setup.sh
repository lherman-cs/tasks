#!/bin/bash

INSTL_PATH="$(pwd)"
SRC_PATH="${INSTL_PATH}/src"
LOG_PATH="${INSTL_PATH}/log"

# Generate settings.py
echo "TASKS_PATH = '${LOG_PATH}/tasks.pkl'" > ${SRC_PATH}/settings.py 
echo "LOG_PATH = '${LOG_PATH}/log.txt'" >> ${SRC_PATH}/settings.py 
echo "MARGIN = 80" >> ${SRC_PATH}/settings.py 

# Create an alias in .bash_profile
echo "Exporting PATH"
echo "export PATH=\$PATH:$INSTL_PATH/bin" >> $HOME/.bash_profile
source $HOME/.bash_profile

# Create an alias in .bashrc
echo "export PATH=\$PATH:$INSTL_PATH/bin" >> $HOME/.bashrc
source $HOME/.bashrc

echo "Done!"

echo
echo "Now try to use the command: tasks"
