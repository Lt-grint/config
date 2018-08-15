#!usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import os
import re
import platform

from subprocess import call
from filecmp import cmp
from shutil import copy
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# git root path for files to push to remote
DIR_FOR_GIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# save config files directory name, relative to the DIR_FOR_GIT path
TARGET_DIR_NAME = "configs"
# save config files path, absolute path
TARGET_DIR_PATH = os.path.join(DIR_FOR_GIT, TARGET_DIR_NAME)

# files and directory to synchronize
SYNC_FILE_LIST = []


def read_file():
    with open(os.path.join(DIR_FOR_GIT, "file_list.txt"), "r") as f:
        try:
            for line in f.readlines():
                line = line.strip().replace('\\', '/')
                if os.path.exists(line):
                    SYNC_FILE_LIST.append(line)
                else:
                    print('file ' + line + ' is not exists')
        except Exception as e:
            raise e


def sync(src_file_path, target_file_path):
    print('src_file_path:' + src_file_path)
    print('target_file_path:' + target_file_path)
    if not os.path.exists(target_file_path):
        os.mkdir(target_file_path)
    if cmp(src_file_path, target_file_path):
        print('the file %s is same ' % target_file_path)
    else:
        copy(src_file_path, target_file_path)
        print('copy file from ' + src_file_path + ' to ' + target_file_path)


class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        src_file_path = event.src_path.replace('\\', '/')
        sync(src_file_path, TARGET_DIR_PATH)

        os.chdir(DIR_FOR_GIT)
        git_add_cmd = "git add -A"
        git_commit_cmd = "git commit -m " + re.escape("Update " + os.path.basename(src_path))
        if platform.system() == "Windows":
            git_commit_cmd = "git commit -m Update."
        git_pull_cmd = "git pull origin master"
        git_push_cmd = "git push origin master"
        call(
            git_add_cmd + "&&" +
            git_commit_cmd + "&&" +
            git_pull_cmd + "&&" +
            git_push_cmd,
            shell=True
        )


if __name__ == "__main__":
    read_file()
    observer = Observer()
    event_handler = FileChangeHandler()

    for file_path in SYNC_FILE_LIST:
        sync(file_path, TARGET_DIR_PATH)

    observer.schedule(event_handler, path=os.path.dirname(os.path.realpath(file_path)), recursive=False)

    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
