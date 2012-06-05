Mastercode Processing Tools
===========================


Configuration
-------------

All files that you should need to edit are in `config/`

- `files.py`:  here we define  input files, and their attributes, to be used in both recalculations and histogram generation
- `file_dict.py`: define which set of files in `files.py` we use in the program
- `plot_list.py`: define which histograms to make (for both best fit and contribution analyses), also define the standard variable names and indices


Executables
-----------
- `EntryHistos.py` fill and save histograms that contain the entry numbers corresponding to the best points in each of the spaces specified in `plot_list.py`
- `DataHistos.py` create histograms containing the &Chi;^2/ p(&Chi;^2,ndof) / &Delta;&Chi;^2 / Contribution data
- `Point.py` finds the best point in entry histogram given inputs e.g. `./Point.py "m0=500" "m12=1000"`
- `RecalculateChi2.py` recalculates the X^2 contributions for all the individual contraints as well as the total, for each point in parameter space. There are X^2 from 'constraints' and 'likelihood functions'. They values have to be modified in '/constraint_dict.py' and ['modules/lhood_dict.py' & 'reprocessing/lhoods/lookups/...' ] 
- `Test.py` provides the ability to test the chi2 contribution for individual points for a single likelihood/constraint.  Usage:
    - `./Test.py --constraint mtop_MC7 174.2`
    - `./Test.py --likelihood CMSalphaT1.6 100 100`

Development
-----------
Note, as much as reasonable we try to follow the [PEP 8 Style
Guide](http://www.python.org/dev/peps/pep-0008/).

The main exception to this is implementing ROOT interfaces where leading we use
their style of `AlternatingCase` for all member functions.
