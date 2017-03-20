#!/bin/bash

home="$(pwd)"
python3 $home/bin/tasks $* 2> $home/log/log.txt

