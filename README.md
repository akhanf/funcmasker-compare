# funcmasker-compare

This contains the masks and dice scores on ds003090 (Rutherford) test subjects.

The analysis notebook makes use of the csv data in this repository and can just be run on google colab. 

To re-generate the csv data, you would need to run the numbered shell scripts, which require:

- Funcmasker-flex from https://github.com/khanlab/funcmasker-flex

- Raw data (ds003090 from OpenNeuro), with the non-test subjects removed:
```
../raw_data/bids_rutherford_testonly
```

- UWO data (currently not available online)
```
../raw_data/bids_uwodata_matchheader
```

- Comparison method from http://github.com/akhanf/fetal-code (fork from Rutherford) installed in:
```
../fetal-code/
```

