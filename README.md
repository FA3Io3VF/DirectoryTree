# DirectoryTree

## Generate ascii art from a directory tree

import os
import os
import sys
from typing import List
from colorama import Fore, Style


class DirectoryTree:
    def __init__(self, dir_path: str):
        self.dir_path = dir_path
    
    def build_tree(self):
        self._build_tree_tool(self.dir_path, '', False)
        
    def _build_tree_tool(self, dir_path: str, prefix: str, is_last: bool):
        stem = f'{Fore.CYAN}|-- {Style.RESET_ALL}' if not prefix else f'{Fore.CYAN}|   {Style.RESET_ALL}'
        branch = f'{Fore.CYAN}`-- {Style.RESET_ALL}' if is_last else f'{Fore.CYAN}|-- {Style.RESET_ALL}'
        prefix += stem

        try:
            contents = os.listdir(dir_path)
        except FileNotFoundError:
            print(f"{dir_path}: Folder not found.")
            return

        directories = filter(lambda name: os.path.isdir(os.path.join(dir_path, name)), contents)
        directories = sorted(directories, key=str.lower)

        for i, directory in enumerate(directories):
            is_last = (i == len(directories) - 1)
            print(prefix + branch + f'{Fore.BLUE}{directory}{Style.RESET_ALL}')
            next_prefix = '    ' if is_last else '|   '
            self._build_tree_tool(os.path.join(dir_path, directory), prefix + next_prefix, is_last)


def is_directory(path: str) -> bool:
    return os.path.isdir(path)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        dir_path = sys.argv[1]
    else:
        dir_path = input("Starting path: ")

    if is_directory(dir_path):
	  tree = DirectoryTree(dir_path)
	  tree.build_tree()
    else:
        print("\nInsert a valid directory.\n")
