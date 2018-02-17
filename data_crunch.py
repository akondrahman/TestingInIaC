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
   getLangStat(df2ana)
   print '-'*100
   print 'Ended at:', giveTimeStamp()
   print '-'*100
