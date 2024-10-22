import numpy as np
import pandas as pd

def ordinalencoder(filename):
    read_file=pd.read_csv(filename,index_col=0)
    s=(read_file.dtypes=="object")
    categorical_cols=list(s[s].index)
    for col in categorical_cols:
        unique=sorted(read_file[col].unique())
        key={}
        for i in range(len(unique)):
            key[unique[i]]=i
        read_file[col+'_encoded']=read_file[col].map(key)
        read_file.drop(col,axis=1,inplace=True)
    return read_file

        
            


