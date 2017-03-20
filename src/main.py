#!/usr/bin/python3

from argparse import ArgumentParser
from os.path import realpath, join, exists, dirname
import pickle
from task import Task
from sys import stderr
import settings

tasks_path = settings.TASKS_PATH
log_path = settings.LOG_PATH
margin = settings.MARGIN

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
        print('\t{}. {}'.format(index, task.task))
        index += 1

def add(task):
    tasks = load()
    print('Adding {}'.format(task))
    tasks.append(Task(task))
    save(tasks)

def done(task_n=1):
    tasks = load()
    if tasks:
        if 1 <= task_n <= len(tasks):
            print('{} - Done'.format(tasks.pop(task_n-1).task))
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
    gparser.add_argument('-d', '--done', help="Remove the first task", \
                          action='store_true')
    gparser.add_argument('-f', '--finish', help="Remove the task_n", \
                          type=int, dest='task_n')


    args = parser.parse_args()

    if args.task is not None:
        add(args.task)
    elif args.done:
        done()
    elif args.task_n:
        done(args.task_n)
    else:
        print_tasks()

if __name__ == '__main__':
    main()
