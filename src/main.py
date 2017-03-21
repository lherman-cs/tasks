#!/usr/bin/python3

from argparse import ArgumentParser
from os.path import realpath, join, exists, dirname
import os
import pickle
from task import Task
from sys import stderr
import settings
import re

tasks_path = settings.TASKS_PATH
log_path = settings.LOG_PATH
margin = settings.MARGIN

os.makedirs(dirname(log_path), exist_ok=True)
stderr = open(log_path, 'a')

def save(tasks):
    with open(tasks_path, 'wb') as file:
        print("Saving to {}".format(tasks_path), file=stderr, flush=True)
        pickle.dump(tasks, file)
        print("Saved!", file=stderr, flush=True)

def load():
    # Check if the file exists. If it doesn't, it'll create an empty queue
    if exists(tasks_path):
        with open(tasks_path, 'rb') as file:
            print("Loading from {}".format(tasks_path), file=stderr, flush=True)
            tasks = pickle.load(file)
            print("Loaded!", file=stderr, flush=True)

    else:
        print("Can't find any existing tasks", file=stderr, flush=True)
        tasks = []

    return tasks

def print_tasks():
    tasks = load()
    print()
    print(' Tasks '.center(margin, '='))

    index = 1
    for task in tasks:
        print('\t{}. {}'.format(index, task.get_info()))
        index += 1

def add(task):
    tasks = load()
    print('Adding {}'.format(task))
    tasks.append(Task(task))
    save(tasks)

# Set the completion percertange on task_n
def set(task_n=1):
    tasks = load()
    if tasks:
        # Make sure the tasks_n is in range
        if 1 <= task_n <= len(tasks):
            task = tasks[task_n-1]
            print(' Setting a new completion percetange for {} '.format(task.get_info())\
                   .center(margin, '='))

            # Make sure the input value is valid
            pattern = re.compile('^\d+')
            completion = input("Input a new value: ")
            if not pattern.match(completion):
                completion = input("Please give a valid value")

            # Make sure the completion percentage is in range
            completion = float(completion)
            if completion >= 100:
                task.completion = completion
                print("Congratulation you've finished your task")
                print("{}".format(task.get_info()))
                tasks.pop(task_n-1)
            else:
                task.completion = 0 if completion < 0 else completion
                print("Task #{} has been set a new completion percentage!".format(task_n))
                print(task.get_info())
        else:
            print('Please give a valid index')
    else:
        print('No tasks at this time')
    save(tasks)

def main():
    parser = ArgumentParser()
    gparser = parser.add_argument_group()
    gparser.add_argument('-a', '--add', dest='task', help='Add a task', \
                          type=str)
    gparser.add_argument('-s', '--set', dest='task_n', type=int, \
                          help="Set completion to task_n in percentage")


    args = parser.parse_args()

    if args.task is not None:
        add(args.task)
    elif args.task_n:
        set(args.task_n)
    else:
        print_tasks()

if __name__ == '__main__':
    main()
