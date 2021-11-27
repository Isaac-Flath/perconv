# AUTOGENERATED! DO NOT EDIT! File to edit: 05_splitting.ipynb (unless otherwise specified).

__all__ = ['bin_df', 'kfold_Stratified_df']

# Cell
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold

# Cell
def bin_df(df,col,bin_sz):
    for i in range(df[col].min(),df[col].max()+bin_sz,bin_sz):
        bin_min = i - (bin_sz-1)
        bin_max = i
        mask = (df[col] >= bin_min) & (df[col] <= bin_max)
        df.loc[mask,f'bin_{bin_sz}'] = f'{bin_min}-{bin_max}'
    return df

# Cell
def kfold_Stratified_df(df,col,folds):
    skf = StratifiedKFold(n_splits=folds)
    col_name = f'{folds}fold_{col}'
    f_num = 0
    for train_idxs, valid_idxs in skf.split(df.index,df[col]):
        df.loc[df.index.isin(valid_idxs),col_name] = int(f_num)
        f_num += 1
    return df