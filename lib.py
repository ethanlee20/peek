
def odd(a:int):
    return (a % 2) == 1


def remove_all(a, l):
    """Remove all occurances of a from list l."""
    while True:
        try: l.remove(a)
        except ValueError: return l


def flatten2d(l):
    """Flatten a 2d array to 1d."""
    i = []
    for a in l:
        for b in a:
            i.append(b)
    return i


def split_and_strip(s, sep):
    """
    Split string s on the given separator(s)
    and clean the result of spaces and empty strings.
    """
    if type(s) != list:
        s = [s]
    if type(sep) != list:
        sep = [sep]
    for p in sep:
        s_presplit = s.copy()
        s = [i.split(p) for i in s]
        s = flatten2d(s)
        if s == s_presplit: raise ValueError(f'{sep} not in string.')
    s = [i.strip() for i in s]
    s = remove_all('', s)
    return s


def last_index(l:list):
    return len(l) - 1


def spaces_to_underscores(string):
    splits = string.split()
    # [splits.insert(i, "_") for i in range(last_index(splits), 0, -1)]
    new_string = "_".join(splits)
    return new_string


def input_type(string):
    try:
        int(string)
        return int
    except ValueError: pass
    
    try: 
        float(string)
        return float
    except ValueError: pass
    
    return str
