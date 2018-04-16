'''
Akond Rahman
April 15, 2018
Correlating defect count and smell count
'''
import pandas as pd
from scipy import stats
import numpy as np
import os
import cliffsDelta
import matplotlib.pyplot as plt

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
    df_to_ret = df_to_ret[ (df_to_ret['SPEAR_CORR'] >= 0.0) & (df_to_ret['SPEAR_P'] < 0.05) ]
    print df_to_ret.tail()
    print '='*50
    return df_to_ret

def makeBoxPlots(h_, l_, feature_param, output_dir_param):
    data_to_plot = [h_, l_]
    plt.grid()
    fig = plt.figure(1, figsize=(8, 6))
    ax = fig.add_subplot(111)
    bp = ax.boxplot(data_to_plot, showfliers=True, sym='r.')
    ax.set_xticklabels(['Defective:'+feature_param, 'Non-defective:'+feature_param])
    fig.savefig(output_dir_param+feature_param + '.png', bbox_inches='tight')
    plt.clf()
    plt.close()


def compareTwoGroups(h_group, l_group, feature_name, output_dir_param):
   '''
   summary time
   '''
   print '(DEFECTIVE:{}): (count:{}, median:{}, mean:{})'.format(feature_name,  len(h_group), np.median(h_group), np.mean(h_group))
   percentiles = [10, 20, 30, 40, 50, 60, 70, 80, 90]
   after_str = ''
   for percentile_ in percentiles:
       perc_val = np.percentile(h_group, percentile_)
       after_str = after_str + str(percentile_) + 'th: ' + str(perc_val) + ' '
   print '-'*25
   print after_str
   print '-'*25
   print '(NON-DEFECTIVE:{}): (count:{}, median:{}, mean:{})'.format(feature_name, len(l_group), np.median(l_group), np.mean(l_group))
   before_str = ''
   for percentile_ in percentiles:
       perc_val = np.percentile(l_group, percentile_)
       before_str = before_str + str(percentile_) + 'th: ' + str(perc_val) + ' '
   print '-'*25
   print before_str
   print '-'*25
   TS, p = stats.mannwhitneyu(h_group, l_group, alternative='greater')
   cliffs_delta = cliffsDelta.cliffsDelta(h_group, l_group)
   print 'Smell:{}, TS:{}, P:{}, Cliffs:{}'.format(feature_name, TS, p, cliffs_delta)
   print '-'*25
   makeBoxPlots(h_group, l_group, feature_name, output_dir_param)

def getComparison(datset, smells, outdir):
    if not os.path.exists(outdir):
       os.makedirs(outdir)
    for smell_ in smell_names:
        sme_def     = datset[datset['DEFECT']==1][smell_].tolist()
        sme_non_def = datset[datset['DEFECT']!=1][smell_].tolist()
        compareTwoGroups(sme_def, sme_non_def, smell_, outdir)

if __name__=='__main__':
   ds_file_name  = '/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/output/MOZ_RQ2_RQ3_DAT.csv'
   out_file_name = '/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/output/MOZ_RQ3_OUT.csv'
   stat_compa_dir = '/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/output/rq3_stat_compa_moz/'

   # ds_file_name  = '/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/output/OST_RQ2_RQ3_DAT.csv'
   # out_file_name = '/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/output/OST_RQ3_OUT.csv'
   # stat_compa_dir = '/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/output/rq3_stat_compa_ost/'

   # ds_file_name  = '/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/output/WIK_RQ2_RQ3_DAT.csv'
   # out_file_name = '/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/output/WIK_RQ3_OUT.csv'
   # stat_compa_dir = '/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/output/rq3_stat_compa_wik/'


   smell_names = ['MISS_DFLT', 'INCO_NAME',	'CPLX_EXPR', 'DUPL_ENTI', 'MSPL_ATTR', 'IMPR_ALIG',
                  'INVA_PROP',	'INCO_TASK', 'DEPE_STMT', 'IMPR_QUOT', 'LONG_STMT', 'INCO_COND',
                  'UNGU_VARI',	'MULT_ABST', 'UNNE_ABST', 'MISS_ABST', 'IMPE_ABST',	'INSU_MODU',
                  'DEFI_ENCA',	'TOTA']
   ds_ = pd.read_csv(ds_file_name)
   '''
   Spearman correlation
   '''
   the_df = getCorrelation(ds_, smell_names)
   the_df.to_csv(out_file_name)
   '''
   Statistical comparison
   '''
   getComparison(ds_, smell_names, stat_compa_dir)
