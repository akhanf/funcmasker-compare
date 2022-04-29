# funcmasker-compare

This contains the masks and dice scores on ds003090 (Rutherford) test subjects.

To re-generate these, run the three shell scripts, which require:


- Funcmasker-flex from https://github.com/khanlab/funcmasker-flex

- Raw data (ds003090 from OpenNeuro), with only the test subjects:
```
../raw_data/bids_rutherford_testonly
```

- Comparison method from http://github.com/akhanf/fetal-code (fork from Rutherford) installed in:
```
../fetal-code/
```
