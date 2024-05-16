
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
```
:-) head
   Number  Digimon Stage  Type Attribute  Memory  Equip_Slots  Lv_50_HP  Lv50_SP  Lv50_Atk  Lv50_Def  Lv50_Int  Lv50_Spd
0       1  Kuramon  Baby  Free   Neutral       2            0       590       77        79        69        68        95
1       2  Pabumon  Baby  Free   Neutral       2            0       950       62        76        76        69        68
2       3  Punimon  Baby  Free   Neutral       2            0       870       50        97        87        50        75
3       4  Botamon  Baby  Free   Neutral       2            0       690       68        77        95        76        61
4       5  Poyomon  Baby  Free   Neutral       2            0       540       98        54        59        95        86
```

3. To cut (filter) for digimon in the mega stage, run `cut Stage==Mega` (try running `head` again to see if this worked). Note that spaces in the cut string (i.e. `Stage == Mega`) will break Peek.
```
:-) head
     Number            Digimon Stage     Type Attribute  Memory  Equip_Slots  Lv_50_HP  Lv50_SP  Lv50_Atk  Lv50_Def  Lv50_Int  Lv50_Spd
166     167           Alphamon  Mega  Vaccine   Neutral      22            1      1390      128       158       183       158       130
167     168   UlforceVeedramon  Mega  Vaccine      Wind      22            1      1680      129       188       109       104       198
168     169             Ebemon  Mega    Virus  Electric      16            3      1230      178        74       114       198       129
169     170  Imperialdramon DM  Mega     Free      Fire      20            2      1730      143       139       139       139       148
170     171  Imperialdramon FM  Mega     Free   Neutral      20            2      1780      114       198       124       114       153
```

4. To further cut for mega digimon with a level 50 HP greater than 1500, run `cut Lv_50_HP>1500`.
```
:-) head
     Number            Digimon Stage     Type Attribute  Memory  Equip_Slots  Lv_50_HP  Lv50_SP  Lv50_Atk  Lv50_Def  Lv50_Int  Lv50_Spd
167     168   UlforceVeedramon  Mega  Vaccine      Wind      22            1      1680      129       188       109       104       198
169     170  Imperialdramon DM  Mega     Free      Fire      20            2      1730      143       139       139       139       148
170     171  Imperialdramon FM  Mega     Free   Neutral      20            2      1780      114       198       124       114       153
171     172            Vikemon  Mega     Free     Water      18            3      1780      105       158       143       129       133
172     173     VenomMyotismon  Mega    Virus      Dark      20            2      1540      120       193       104       148       138
```

5. To list the applied cuts, run `list_cuts`.
```
:-) list_cuts
0. Stage==Mega
1. Lv_50_HP>1500
```

6. To remove the mega stage cut, run `undo_cut 0` where `0` is the index of the mega stage cut. Multiple cuts can be removed by specifying multiple arguments.
```
:-) undo_cut 0
Undoing cuts: Stage==Mega

:-) head
     Number       Digimon     Stage     Type Attribute  Memory  Equip_Slots  Lv_50_HP  Lv50_SP  Lv50_Atk  Lv50_Def  Lv50_Int  Lv50_Spd
121     122    GrapLeomon  Ultimate  Vaccine  Electric      12            2      1580       89       163        99        79       143
123     124    Shakkoumon  Ultimate     Free     Light      14            1      1530      135        84       158       139        92
124     125     Cherrymon  Ultimate    Virus     Plant      12            2      1630      108       113       133       114       100
128     129       Zudomon  Ultimate  Vaccine     Water      12            2      1630       84       150       128       104       102
132     133  SkullMeramon  Ultimate     Data      Fire      12            2      1530       79       183       133        70       113
```

7. Run `quit` to quit peek.



