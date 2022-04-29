#!/bin/bash

#this uses http://github.com/akhanf/fetal-code (fork with minor update for running locally)

for f in `ls -d /localscratch/proc_rutherford/funcmasker_output_uwodata/results/sub-*/ses-*/func/sub-*_ses-*_task-*_desc-cleanorient_bold`
do
    out_folder=${f%desc-cleanorient_bold}desc-rutherford_mask
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
        fi
        fslorient -deleteorient ${out_folder}/${fname}
    done


    echo fslmerge -t ${out_mask_4d} ${out_folder}/*.nii.gz
    fslmerge -t ${out_mask_4d} ${out_folder}/*.nii.gz
    break
done  
