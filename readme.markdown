Mastercode Processing Tools
===========================


Configuration
-------------

All files that you should need to edit are in `config/`

    + `files.py`:  here we define  input files, and their attributes, to be used in both recalculations and histogram generation
    + `file_dict.py`: define which set of files in `files.py` we use in the program
    + `plot_list.py`: define which histograms to make (for both best fit and contribution analyses), also define the standard variable names and indices

Executables
-----------
    `EntryHistos.py` fill and save histograms that contain the entry numbers corresponding to the best points in each of the spaces specified in `plot_list.py`
    `DataHistos.py` create histograms containing the &Chi;^2/ p(&Chi;^2,ndof) / &Delta;&Chi;^2 / Contribution data
    `Point.py` finds the best point in entry histogram given inputs e.g. `./Point.py "m0=500" "m12=1000"`
