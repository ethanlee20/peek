from sys import argv
import traceback
import readline
import inspect

from parse import parse
from command_manager import Command, Command_Manager
from data_handler import Data_Handler


class Peek:
    def __init__(self, data_path) -> None:
        self.running = True
        self.data_handler = Data_Handler(data_path)
        self.command_manager = Command_Manager()
        self.run()
    
    def quit(self):
        print("Shutting down! Watch out!")
        self.running = False

    def run(self):
        while self.running:
            command, pos_args, kwargs = self._parse()
            kwargs |= self._system_kwargs()
            try: self.command_manager.run_command(command, pos_args, kwargs)
            except: 
                print("Something went wrong:")
                traceback.print_exc()
                 

    def _parse(self):
        user_input = input(":-) ")
        command, pos_args, kwargs = parse(user_input)
        # print("DEBUG - user inputs:", command, pos_args, kwargs)
        return command, pos_args, kwargs
        
    def _system_kwargs(self):
        system_kwargs = {
            'data': self.data_handler.data,
            'data_handler': self.data_handler,
            'peek': self
        }
        return system_kwargs
    

peek = Peek(argv[1])
    
