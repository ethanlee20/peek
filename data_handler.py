import pathlib as pl
import pandas as pd

from cut import Cut
from lib import spaces_to_underscores




    

class Data_Handler:

    def __init__(self, data_path):
        self.load(data_path)
        self.cut_history = []

    def load(self, path):
        path = pl.Path(path)
        if path.suffix == ".csv":
            open = pd.read_csv
        elif path.suffix == ".pkl":
            open = pd.read_pickle
        self.original_data = open(path)
        self.original_data = self.fix_column_names(self.original_data)
        self.data = self.original_data.copy()
    
    def refresh(self):
        self.cut_history = []
        self.data = self.original_data.copy()

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

    def fix_column_names(self, df):
        original_column_names = df.columns.tolist()
        df_renamed = df.rename(spaces_to_underscores, axis='columns')
        new_column_names = df_renamed.columns.tolist()
        if new_column_names != original_column_names:
            print("Changed spaces in column names to underscores.\n")
        return df_renamed
    
    def _redo_cuts(self):
        cuts = self.cut_history.copy()
        self.refresh()
        for cut in cuts:
            self.cut_data(cut)

    def undo_cuts(self, cut_indicies:list[int]):
        print(f"Undoing cuts: {' and '.join([self.cut_history[i] for i in cut_indicies])}")
        cut_indicies.sort(reverse=True)
        for i in cut_indicies:
            del self.cut_history[i]
        self._redo_cuts()


