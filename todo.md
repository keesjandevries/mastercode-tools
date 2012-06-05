ToDo
====

Current Development
-------------------
* Investigate using google protoBufs:
    * initial checks see small size gain and noticable speed gains (when using python module
    * **disadvantage**: we have to use `message.ParseFromString( f.read() )` and read the whole file in before doing anything
    * there maybe be a way around this using a small C++ module: use set size reads from an sstream object.  Keeps the handle open.
    * If we are going to use set read blocks for the messages this limits us when combining models with different numbers of parameters *or* we end up padding and having larger files and an upper limit in the future
    * store size of message before message? `message{ required int32 next_size }`
    * if we have differing sizes we cannot just "jump" ahead to a given point in the file: check ksamdev

Problems
--------
* Inconsistent style: clean up variable / function / class / module naming conventions for readability
* Debug problems with logx and logy not working 
    [ confirmed in spaces at least ]
    [ confirm it still actually happens ]

* Better (or at all) error reporting!!!!
* Need to add in "SMInputIndex" / "NuisanceParametersIndex" options to the MCFiles so we can get positions for DeltaAlphaHad etc. automatically, without doing backwards references
* "Inputs" in `modules/file_dicts.py`: need to check this is right, MC7 suggests 7,8 etc.  so we need to chekc how it is used (ModelInputs, NuisanceParams may fix this)

Functionality
-------------
* KJ: Point-tools. Print all (relevant) predictions/ X^2 breakdown; if a plane
    does not exist, make the missing plane;

Repo
----
* Move this todo, etc. into issues (where relevant)