import nibabel as nib
import numpy as np
import pandas as pd

manual_nib = nib.load(snakemake.input.manual)
auto_nib = nib.load(snakemake.input.auto)


manual_vols = manual_nib.get_fdata()
auto_vols = auto_nib.get_fdata()

#print(f'manual seg shape: {manual_vols.shape}')
#print(f'auto seg shape: {auto_vols.shape}')

#for whatever reason, manual seg can have wrong # of vols -- not sure what has happened here..

out_dict={'id':[],'sensitivity':[],'specificity':[],'precision':[],'dice':[],'slice':[]}

scanname=snakemake.params.scanname

for i_time in range(auto_vols.shape[3]):

    for i_slice in range(auto_vols.shape[2]):

        manual_2d = manual_vols[:,:,i_slice,i_time]
        auto_2d = auto_vols[:,:,i_slice,i_time]

        #if manual_seg and auto seg not in this slice:
        if ((manual_2d>0).sum() == 0) and ((auto_2d>0).sum() == 0):
            #leave it out
            continue
 
        tp=np.logical_and(manual_2d>0,auto_2d>0).sum()
        tn=np.logical_and(manual_2d==0,auto_2d==0).sum()
        fp=np.logical_and(manual_2d==0,auto_2d>0).sum()
        fn=np.logical_and(manual_2d>0,auto_2d==0).sum()

        avg_p = 0.5*((manual_2d>0).sum()+(auto_2d>0).sum())
    
       
        out_dict['dice'].append(tp/avg_p)
        out_dict['sensitivity'].append(tp/(tp+fn))
        out_dict['precision'].append(tp/(tp+fp))
        out_dict['specificity'].append(tn/(tn+fp))
        out_dict['slice'].append(i_slice)
        out_dict['id'].append(f'{scanname}-{i_time}')

        #print('confusion_matrix:')
        #print(f'{tn} {fn}')
        #print(f'{fp} {tp}')

df = pd.DataFrame(out_dict)

df.to_csv(snakemake.output.csv,index=False)
