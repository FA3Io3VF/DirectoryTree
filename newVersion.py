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


class DirectoryValidator:
    def __init__(self, path: str):
        self.path = path

    def is_valid(self) -> bool:
        return os.path.isdir(self.path)


class InputHandler:
    def __init__(self, args: List[str]):
        self.args = args

    def get_input(self) -> str:
        if len(self.args) > 1:
            return self.args[1]
        else:
            return input("Starting path: ")


if __name__ == '__main__':
    input_handler = InputHandler(sys.argv)
    dir_path = input_handler.get_input()

    validator = DirectoryValidator(dir_path)
    if validator.is_valid():
        tree = DirectoryTree(dir_path)
        tree.build_tree()
    else:
        print("\nInsert a valid directory\n")
