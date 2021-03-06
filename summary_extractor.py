'''
get summary stats from datasets
Akond Rahman
Nov 05, 2017
'''
from scipy import stats
import pandas as pd
import numpy as np
import cliffsDelta

mirantis_file  = '/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/dataset-icse19-tse/MIR_VDB.csv'
mozilla_file   = '/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/dataset-icse19-tse/MOZ_VDB.csv'
openstack_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/dataset-icse19-tse/OST_VDB.csv'
wikimedia_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/dataset-icse19-tse/WIK_VDB.csv'

def giveTimeStamp():
  import time, datetime
  tsObj = time.time()
  strToret = datetime.datetime.fromtimestamp(tsObj).strftime('%Y-%m-%d %H:%M:%S')
  return strToret

dataset_files = [mirantis_file, mozilla_file, openstack_file, wikimedia_file]

print "Started at:", giveTimeStamp()
for dataset_file in dataset_files:
    name = dataset_file.split('/')[-1]
    print "Dataset:", name
    df2read = pd.read_csv(dataset_file)

    features = df2read.columns
    dropcols = ['DEFECT', 'FILE']
    features2see = [x_ for x_ in features if x_ not in dropcols]
    for feature_ in features2see:
           #print feature_
           '''
           all data summary
           '''
           data_for_feature = df2read[feature_]
           median_, mean_, total_ = np.median(data_for_feature), np.mean(data_for_feature), sum(data_for_feature)
           print "Feature:{}, [ALL DATA] median:{}, mean:{}, sum:{}".format(feature_, median_, mean_, total_  )
           print '='*50
           defective_vals_for_feature     = df2read[df2read['DEFECT']==1][feature_]
           non_defective_vals_for_feature = df2read[df2read['DEFECT']==0][feature_]
           '''
           summary time
           '''
           print 'THE FEATURE IS:', feature_
           print '='*25
           #print "Defective values stats: \n", defective_vals_for_feature.describe()
           print "Defective values [MEDIAN]:{}, [MEAN]:{}".format(np.median(list(defective_vals_for_feature)), np.mean(list(defective_vals_for_feature)))
           #d_perc_90 = np.percentile(defective_vals_for_feature, 90)
           #print "Non defective values stats: \n", non_defective_vals_for_feature.describe()
           print "Non Defective values [MEDIAN]:{}, [MEAN]:{}".format(np.median(list(non_defective_vals_for_feature)), np.mean(list(non_defective_vals_for_feature)))
           #nd_perc_90 = np.percentile(non_defective_vals_for_feature, 90)
           TS, p = stats.mannwhitneyu(list(defective_vals_for_feature), list(non_defective_vals_for_feature), alternative='greater')
           cliffs_delta = cliffsDelta.cliffsDelta(list(defective_vals_for_feature), list(non_defective_vals_for_feature))
           print 'Feature:{}, pee value:{}, cliffs:{}'.format(feature_, p, cliffs_delta)
           print '='*50
    print '*'*100
print "Ended at:", giveTimeStamp()
