
Warning: Unstable.

Peek is a small interactive program to peek into files containing pandas dataframes. The program loads a dataframe 
into memory and comes with various functions such as viewing the first few rows and filtering. Further 
functionality can be added by editing the `user_commands.py` file. More instructions will be added (possibly).


## Getting Started

1. Download the repository.
2. Run using `python path/to/peek.py path/of/datafile.csv`
3. Try the `head` command (type `head` and press `Enter`) to view the first few rows of the dataframe.

## Example Usage

Let's try running `peek` on the file `DigiDB_digimonlist.csv`, which contains a dataframe of digimon and their attributes.

1. To open the file in peek run `python path/to/peek.py path/to/DigiDB_digimonlist.csv`.
2. To view the first few rows run `head`.
3. To filter for digimon in the mega stage, run `cut Stage==Mega` (try running `head` again to see if this worked).
4. To further filter the previous results for mega digimon with a level 50 HP greater than 1500, run `cut Lv_50_HP>1500`.
5. To list the applied cuts (filters), run `list_cuts`.
6. To remove the mega stage cut, run 'undo_cut 0' where `0` is the index of the mega stage cut.

In this way, we can view various aspects of our data.

7. Run `quit` to quit peek.



