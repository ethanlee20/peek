
Warning: Unstable.

Peek is a small interactive program to peek into tabular datafiles. 
The program loads the content of the file as a pandas dataframe and comes with various functions such as viewing the first few rows and filtering. 
Further functionality can be added by editing the `user_commands.py` file. More instructions will be added (possibly).


## Getting Started

1. Download the repository.
2. Run using `python path/to/peek.py path/to/datafile.csv`
3. Try the `head` command (type `head` and press `Enter`) to view the first few rows.

## Example Usage

Let's try running Peek on the file `DigiDB_digimonlist.csv` (found [here](https://www.kaggle.com/datasets/rtatman/digidb)), which contains Digimon data.

1. To open the file in Peek, run `python path/to/peek.py path/to/DigiDB_digimonlist.csv`.
2. To view the first few digimon, run `head`.
3. To cut (filter) for digimon in the mega stage, run `cut Stage==Mega` (try running `head` again to see if this worked). Note that spaces in the cut string (i.e. `Stage == Mega`) will break Peek.
4. To further cut for mega digimon with a level 50 HP greater than 1500, run `cut Lv_50_HP>1500`.
5. To list the applied cuts, run `list_cuts`.
6. To remove the mega stage cut, run `undo_cut 0` where `0` is the index of the mega stage cut. Multiple cuts can be removed by specifying multiple arguments.
7. Run `quit` to quit peek.



