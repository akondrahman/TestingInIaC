'''
Akond Rahman
Feb 15, 2018
Data Cruncher
'''
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
    # print all_langs
    for lang_ in all_langs:
        lang_df_status = df_p[df_p['lang']==lang_]['status'].tolist()
        status_dict = Counter(lang_df_status)
        print 'Language:', lang_
        print status_dict
        print '-'*100

def getDF(file_to_an):
    df_ = pd.read_csv(file_to_an)
    df_.columns = ['hash', 'dura', 'type', 'status', 'timestamp', 'noidea1', 'size', 'noidea1', 'noidea3', 'lang']
    # print df_.tail()
    print df_.shape
    return df_

if __name__=='__main__':
   # file_path = '/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/project-materials/csc712_test_data/sample_test_suite.csv'
   file_path = '/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/project-materials/csc712_test_data/testSuiteDataset.csv'
   print 'Started at:', giveTimeStamp()
   print '-'*100
   df2ana = getDF(file_path)
   getLangStat(df2ana)
   print '-'*100
   print 'Ended at:', giveTimeStamp()
   print '-'*100
