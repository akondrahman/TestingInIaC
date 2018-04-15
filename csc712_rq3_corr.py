'''
Akond Rahman
April 15, 2018
Correlating defect count and smell count
'''
import pandas as pd

def getCorrelation(dataset, smells):
    

if __name__=='__main__':
   ds_file_name = ''
   smell_names = ['MISS_DFLT', 'INCO_NAME',	'CPLX_EXPR', 'DUPL_ENTI', 'MSPL_ATTR', 'IMPR_ALIG',
                  'INVA_PROP',	'INCO_TASK', 'DEPE_STMT', 'IMPR_QUOT' 'LONG_STMT', 'INCO_COND',
                  'UNGU_VARI',	'MULT_ABST', 'UNNE_ABST', 'MISS_ABST', 'IMPE_ABST',	'INSU_MODU',
                  'DEFI_ENCA',	'TOTA']
   ds_ = pd.read_csv(ds_file_name)
   getCorrelation(ds_, smell_names)
