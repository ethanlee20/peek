
def quit(args, kwargs):
    kwargs['peek'].quit()
    print()

def refresh(args, kwargs):
    kwargs["data_handler"].refresh()
    print("Data refreshed.\n")

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
    for index, cut in enumerate(cut_history): print(f'{index}. {cut}')
    print()

def undo_cut(args, kwargs):
    cut_indicies = [int(arg) for arg in args]
    kwargs['data_handler'].undo_cuts(cut_indicies)
    print()
