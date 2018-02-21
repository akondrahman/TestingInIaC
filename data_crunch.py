'''
Akond Rahman
Feb 15, 2018
Data Cruncher
'''
import cPickle as pickle
import pandas as pd
import numpy as np
from collections import Counter

def giveTimeStamp():
    import time, datetime
    tsObj = time.time()
    strToret = datetime.datetime.fromtimestamp(tsObj).strftime('%Y-%m-%d %H:%M:%S')
    return strToret

def getAllChangeReq(df_pa):
    # print df_pa.head()
    all_cng_req = df_pa['chng_requ'].tolist()
    print "Total change requests (unique):", len(np.unique(all_cng_req))

def printCounterVals(stage_size_pa):
    all_val_list = stage_size_pa.values()
    # print all_val_list
    all_val_cnt = sum(all_val_list)
    print 'ALL ENTRIES:', all_val_cnt
    for key_, val_ in stage_size_pa.iteritems():
        print 'KEY:{}, PERC:{}'.format(key_, (float(val_)/float(all_val_cnt)*100))
        print '-'*25

def getElbaumTable(df_pa):
    dict_ = {}
    # print df_pa.head()
    stages = np.unique(df_pa['stag'].tolist())
    for stage_ in stages:
        # print stage_
        size_for_stage = df_pa[df_pa['stag']==stage_]['size'].tolist()
        # print size_for_stage
        per_stage_sizes = dict(Counter(size_for_stage))
        print per_stage_sizes
        for k_, v_ in per_stage_sizes.iteritems():
            the_key = stage_ + '_' + k_
            dict_[the_key] = v_
        # print per_stage_sizes
    # print dict_
    printCounterVals(dict_)



def getLangStat(df_p):
    all_langs = np.unique(df_p['lang'].tolist())
    print 'Languages:', all_langs
    print '-'*100
    for lang_ in all_langs:
        lang_df_status = df_p[df_p['lang']==lang_]['stat'].tolist()
        status_dict = Counter(lang_df_status)
        print 'Language:', lang_
        print status_dict
        print '-'*50

def getDF(file_to_an):
    df_ = pd.read_csv(file_to_an)
    df_.columns = ['test_suit', 'chng_requ', 'stag', 'stat', 'laun_time', 'exec_time', 'size', 'shar_numb', 'run_num', 'lang']
    return df_

if __name__=='__main__':
   # file_path = '/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/project-materials/csc712_test_data/sample_test_suite.csv'
   ### full dataset
   # file_path = '/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/project-materials/csc712_test_data/testSuiteDataset.csv'
   ### pared daatset
   # file_path = '/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/project-materials/csc712_test_data/paredDatasetOptimized.csv'

   ### full pickle file: by default use this
   file_path = '/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/project-materials/csc712_test_data/FULL_TEST_DATA.PKL'

   print 'Started at:', giveTimeStamp()
   print '-'*100
   if '.csv' in file_path:
      df2ana = getDF(file_path)
      # df2ana.to_pickle('/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/project-materials/csc712_test_data/FULL_TEST_DATA.PKL')
   else:
      df2ana = pickle.load( open( file_path, "rb" ) )
   print '-'*100
   print df2ana.tail()
   print '-'*100
   print 'Dataset size:', df2ana.shape
   print '-'*100
   # getLangStat(df2ana)
   # print '-'*100
   # Workshop tasks
   getAllChangeReq(df2ana)
   print '-'*100
   getElbaumTable(df2ana)
   print '-'*100
   print 'Ended at:', giveTimeStamp()
   print '-'*100
