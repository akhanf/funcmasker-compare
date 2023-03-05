import nibabel as nib
import numpy as np
import pandas as pd

manual_nib = nib.load(snakemake.input.manual)
auto_nib = nib.load(snakemake.input.auto)


manual_vols = manual_nib.get_fdata()
auto_vols = auto_nib.get_fdata()

print(f'manual seg shape: {manual_vols.shape}')
print(f'auto seg shape: {auto_vols.shape}')

#for whatever reason, manual seg can have wrong # of vols -- not sure what has happened here..

out_dict={'id':[],'sensitivity':[],'specificity':[]}

scanname=snakemake.params.scanname

for i in range(auto_vols.shape[3]):
    manual_3d = manual_vols[:,:,:,i]
    auto_3d = auto_vols[:,:,:,i]

    tp=np.logical_and(manual_3d>0,auto_3d>0).sum()
    tn=np.logical_and(manual_3d==0,auto_3d==0).sum()
    fp=np.logical_and(manual_3d==0,auto_3d>0).sum()
    fn=np.logical_and(manual_3d>0,auto_3d==0).sum()

    
    out_dict['sensitivity'].append(tp/(tp+fn))
    out_dict['specificity'].append(tn/(tn+fp))
    out_dict['id'].append(f'{scanname}-{i}')

print(out_dict)
df = pd.DataFrame(out_dict)

df.to_csv(snakemake.output.csv,index=False)
