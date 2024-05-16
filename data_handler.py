
import pandas as pd

from cut import Cut


class Data_Handler:

    def __init__(self, data_path):
        self.load(data_path)
        self.cut_history = []

    def load(self, path):
        self.original_data = pd.read_csv(path)
        self.data = self.original_data.copy()
    
    def refresh(self):
        self.cut_history = []
        self.data = self.original_data.copy()
        print("Data refreshed.")

    def cut_data(self, cut_string:str):
        cut = Cut(cut_string)
        code = "self.data["
        for index, comparison in enumerate(cut.comparisons):
            code += f"(self.data['{comparison.var}'] {comparison.sym} {comparison.val})"
            try: code += cut.logic_syms[index]
            except IndexError: continue
        code += ']'

        # print("DEBUG - Cut code:", code)
        self.data = eval(code)
        self.cut_history.append(cut.cut_string)
        
    def list_cuts(self):
        for cut in self.cut_history:
            print(cut)