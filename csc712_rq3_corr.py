'''
Akond Rahman
April 15, 2018
Correlating defect count and smell count
'''
import pandas as pd
from scipy import stats
import numpy as np

def getCorrelation(dataset, smells):
    # print dataset.head()
    all_sme_list = []
    for smell_ in smell_names:
        all_mon = dataset['MONTH'].tolist()
        for mon_ in all_mon:
            mon_dat = dataset[dataset['MONTH']==mon_]
            mon_def = mon_dat['DEFECT'].tolist()
            mon_sme = mon_dat[smell_].tolist()
            mon_cor = stats.spearmanr(mon_def, mon_sme)
            all_sme_list.append((smell_, mon_, mon_cor[0], mon_cor[1]))
    df_to_ret = pd.DataFrame(all_sme_list, columns=['SMELL', 'MONTH', 'SPEAR_CORR', 'SPEAR_P'])
    df_to_ret = df_to_ret.fillna(0)
    df_to_ret = df_to_ret[ (df_to_ret['SPEAR_CORR'] >= 0.0) & (df_to_ret['SPEAR_P'] > 0) ]
    print df_to_ret.tail()
    print '='*50
    return df_to_ret

if __name__=='__main__':
   ds_file_name  = '/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/output/WIK_RQ2_RQ3_DAT.csv'
   out_file_name = '/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/output/WIK_RQ3_OUT.csv'


   smell_names = ['MISS_DFLT', 'INCO_NAME',	'CPLX_EXPR', 'DUPL_ENTI', 'MSPL_ATTR', 'IMPR_ALIG',
                  'INVA_PROP',	'INCO_TASK', 'DEPE_STMT', 'IMPR_QUOT', 'LONG_STMT', 'INCO_COND',
                  'UNGU_VARI',	'MULT_ABST', 'UNNE_ABST', 'MISS_ABST', 'IMPE_ABST',	'INSU_MODU',
                  'DEFI_ENCA',	'TOTA']
   ds_ = pd.read_csv(ds_file_name)
   the_df = getCorrelation(ds_, smell_names)
   the_df.to_csv(out_file_name)
