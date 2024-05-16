
from dataclasses import dataclass

@dataclass
class Token:
    index: int
    content: str

def is_kw(t:Token):
    if t.content[0] == "-":
        return True
    return False

class Token_List(list):
    def __init__(self, l:list[Token]):
        super().__init__(l)
    def find(self, index):
        try: return [t for t in self if t.index == index][0]
        except: raise IndexError
    def content(self):
        return [t.content for t in self]

def tokenize(string):
    splits = string.split()
    tokens = Token_List([Token(i[0], i[1]) for i in enumerate(splits)])
    return tokens

def _match_kwargs(kws:Token_List, kw_args:Token_List):
    matched = {}
    for kw in kws:
        try: arg = kw_args.find(kw.index+1).content
        except IndexError: arg = True
        matched |= {kw.content[1:]: arg}
    return matched

def parse(s:str) -> tuple[str, list[str], dict]:
    tokens = tokenize(s)
    try: command = tokens[0].content
    except IndexError: command = ""
    kws = Token_List([t for t in tokens if is_kw(t)])
    try: index_first_kw = kws[0].index
    except IndexError: index_first_kw = None
    kw_args = Token_List([t for t in tokens[index_first_kw:] if ~is_kw(t)])
    pos_args = Token_List(tokens[1:index_first_kw]).content()
    matched_kwargs = _match_kwargs(kws, kw_args) 
    return command, pos_args, matched_kwargs


