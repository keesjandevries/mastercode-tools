Mastercode Processing Tools
===========================


Configuration
-------------

All files that you should need to edit are in

- Define files, constraints, variables (relatively hard coded, in principle only add new info, dont modify)
    - `modules/variables.py`: list of all variables, modify if you want to define a new variable, e.g. 'mstau1 - mneu1'
    - `modules/lhood_dict.py`   : setup likelihood information, together with 'reprocessing/lhoods/lookups/...'
    - `modules/constraint_dict.py`: list of all gaussian constraints, modify if you want to add NEW constraints, e.g. Mh_2013
    - `models/*`: files that contain constraint lists, build up from the names in `modules/lhood_dict.py` and `modules/constraint_dict.py` 
    - `modules/file_dict.py`: here we define  input files, and their attributes, e.g. the model files in `models/*`,to be used in both recalculations and histogram generation
- Used at the level of execution (switches)
    - `config/files.py`     : define which set of files in `modules/file_dict.py` we use in EntryHistos.py, DataHistos.py, Point.py, SmoothSplines.py
    - `config/plots.py`     : define which histograms to make (for both best fit and contribution analyses), also define the standard variable names and indices
    -  `config/smooth_coordinates.py` : define which histogram from which file to smooth: specify range and number of smoothing


Executables
-----------
- `EntryHistos.py` fill and save histograms that contain the entry numbers corresponding to the best points in each of the spaces specified in `config/plots.py` for files specified in `histo_files()` in `config/files.py`.
- `DataHistos.py` create histograms containing the &Chi;^2/ p(&Chi;^2,ndof) / &Delta;&Chi;^2 / Contribution / Prediction data of the spaces specified in `config/plots.py` for files specified in `histo_files()` in `config/files.py`.
- `Point.py` get information of points
    - the best point in entry histogram given inputs:  `./Point.py -c "m0=500" "m12=1000"`,
    - the best fit point: `./Point.py -b`
    - the point corresponding to entry number `n`: `./Point.py -n 12345`
- `RecalculateChi2.py` recalculates the X^2 contributions for all the individual contraints as well as the total, for each point in parameter space. There are X^2 from 'constraints' and 'likelihood functions'. Their values have to be modified in 'modules/constraint_dict.py' and ['modules/lhood_dict.py' & 'reprocessing/lhoods/lookups/...' ] 
- `Test.py` provides the ability to test the chi2 contribution for individual points for a single likelihood/constraint.  Usage:
    - `./Test.py --constraint mtop_MC7 174.2`
    - `./Test.py --likelihood CMSalphaT1.6 100 100`
- `SmoothSplines.py` uses the ROOT functionality to smooth 1D histograms, given ranges and number of smoothing in `config/smooth_coordinates.py`. `histo_files()` in `config/files.py` specifies the file that is used, and `config/plots.py` which histograms are smoothed.  

Development
-----------
Note, as much as reasonable we try to follow the [PEP 8 Style
Guide](http://www.python.org/dev/peps/pep-0008/).

The main exception to this is implementing ROOT interfaces where leading we use
their style of `AlternatingCase` for all member functions.
