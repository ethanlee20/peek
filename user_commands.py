
def quit(args, kwargs):
    kwargs['peek'].quit()
    print()

def refresh(args, kwargs):
    kwargs["data_handler"].refresh()
    print()

def head(args, kwargs):
    try: num = int(kwargs['n'])
    except KeyError: num = 5
    print(kwargs['data'].head(num))
    print()


def cut(args, kwargs):
    cut_string = args[0]
    kwargs['data_handler'].cut_data(cut_string)
    print()

def list_cuts(args, kwargs):
    cut_history = kwargs['data_handler'].cut_history
    for cut in cut_history: print(cut)
    print()