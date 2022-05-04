#!/bin/bash

#this uses http://github.com/akhanf/fetal-code (fork with minor update for running locally)

source ../fetal-code/venv/bin/activate


for f in `ls -d /localscratch/funcmasker-compare/funcmasker_output_uwodata/results/sub-*/ses-*/func/sub-*_ses-*_task-*_desc-conform_bold`
do
    out_folder=${f%desc-conform_bold}desc-rutherford_mask
    out_mask_4d=$out_folder.nii.gz

    echo $out_folder
    mkdir -p $out_folder
    for im in `ls $f/*.nii.gz`
    do
        fname=${im##*/}
        if [ ! -e ${out_folder}/${fname} ]
        then
        pushd ../fetal-code/code
        python createMasks.py ${im} ${out_folder}/${fname}
        popd
        fslorient -deleteorient ${out_folder}/${fname}
        fi
    done

    if [ ! -e ${out_mask_4d} ]
    then
    echo fslmerge -t ${out_mask_4d} ${out_folder}/*.nii.gz
    fslmerge -t ${out_mask_4d} ${out_folder}/*.nii.gz
    fi
done  

deactivate
