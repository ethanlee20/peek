
from dataclasses import dataclass

import argparse
import inspect
import user_commands


@dataclass
class Command:
    name: str
    fn: callable


class Command_Manager:
    def __init__(self) -> None:
        self.known_commands = []
        self._add_user_commands()

    def add_command(self, fn:callable):
        command = Command(fn.__name__, fn)
        self.known_commands.append(command)

    def _add_user_commands(self):
        commands = inspect.getmembers(user_commands, inspect.isfunction)
        commands = [Command(i[0], i[1]) for i in commands]
        self.known_commands += commands

    def _get_command(self, name):
        names, fns = zip(*[(c.name, c.fn) for c in self.known_commands])
        try: 
            ind = names.index(name)
            return fns[ind]
        except ValueError: raise ValueError("Unknown command.") 
    
    def run_command(self, name, args, kwargs):
        fn = self._get_command(name)
        fn(args, kwargs)
