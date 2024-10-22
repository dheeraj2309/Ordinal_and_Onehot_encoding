import pandas as pd
import numpy as np

def OneHotEncoder(filename):
    read_file=pd.read_csv(filename,index_col=0)
    s=(read_file.dtypes=="object")
    categorical_cols=list(s[s].index)
    for col in categorical_cols:
        unique=sorted(read_file[col].unique())
        for i in range(len(unique)):
            read_file[unique[i]+'_hotencoded']=read_file[col].apply(lambda x: 1 if x==unique[i] else 0)
        read_file.drop(col, axis=1,inplace=True)
    return read_file
