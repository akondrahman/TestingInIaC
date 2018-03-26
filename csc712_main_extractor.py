'''
Akond Rahman
Mar 25, 2018
Script to extract all code smells using Puppeteer
'''
import csc712_constants as constants
import os
import csc712_lint_engine as lint_engine
import time
import datetime
import csv
import numpy as np

def giveTimeStamp():
  tsObj = time.time()
  strToret = datetime.datetime.fromtimestamp(tsObj).strftime('%Y-%m-%d %H:%M:%S')
  return strToret


def checkValidity(file_path):
    # skip files that are in hidden directories, and in spec folders
    flag2ret = False
    if ((file_path.count(constants.DOT) == 1) and (constants.TEST_DIR_SPEC not in file_path) and (constants.TEST_DIR_ACCE not in file_path)):
        flag2ret  = True
    return flag2ret

def processFileName(single_file_name):
    splitted_dir_name = single_file_name.split('/')[5]
    year  = splitted_dir_name.split('-')[-2]
    month = splitted_dir_name.split('-')[-1]
    str2del = '-' + year + '-' + month
    str2ret = single_file_name.replace(str2del, '')
    return str2ret

def getMonthData(file_p, dir_p):
    temp_     = file_p.replace(dir_p, '')
    time_dir  = temp_.split('/')[0]
    time_list = time_dir.split('-')
    month2ret = time_list[-2] + '-' + time_list[-1] + ','
    return month2ret

def getData(dir_p):
    counter = 0
    for root_, dirs, files_ in os.walk(dir_p):
       for file_ in files_:
           if (file_.endswith(constants.PP_EXT) or file_.endswith(constants.CH_EXT)):
                 full_p_file = os.path.join(root_, file_)
                 if (os.path.exists(full_p_file) and checkValidity(full_p_file) and (full_p_file.endswith(constants.CH_EXT)==False)):
                    counter += 1
                    print 'Analyzing:{},Index:{}'.format(full_p_file, counter)
                    month_str  = getMonthData(full_p_file, dir_p)
                    all_smells = lint_engine.runLinter(full_p_file)
                    print all_smells
                    orig_file_name = processFileName(full_p_file)
                    print '*'*50

def getMonthFromCategData(mon_str):
    mon_ = constants.INV_MON_CON
    if '/' in mon_str:
        only_mon = mon_str.split('/')[0]
        if (len(only_mon)==1):
            only_mon = '0' + only_mon
        mon_ = '20' + mon_str.split('/')[-1] + '-' + only_mon
    return mon_

def getPuppetFileDetails(theCompleteCategFile, root_dirp):
    mon_lis = []
    with open(theCompleteCategFile, constants.FILE_OPEN_MODE) as file_:
      reader_ = csv.reader(file_)
      next(reader_, None)
      for row_ in reader_:
        repo_of_file       = row_[1]
        categ_of_file      = row_[3]
        full_path_of_file  = row_[4]
        time_of_file       = row_[5]
        month_of_file      = getMonthFromCategData(time_of_file)
        if (month_of_file != constants.INV_MON_CON):
           if repo_of_file.endswith('/'):
              repo2look = repo_of_file.split('/')[-2]
           else:
              repo2look = repo_of_file.split('/')[-1]
           # print repo2look
           sub_path = full_path_of_file.replace(repo_of_file, '')
           preamble = root_dir + repo2look + '-' + month_of_file
           # print preamble
           # print sub_path
           if (preamble.endswith('/')==False):
             preamble = preamble + '/'
           path_to_analyze = preamble  + sub_path
           path_to_analyze = path_to_analyze.replace('//', '/')
           if (os.path.exists(path_to_analyze)):
              print path_to_analyze
              all_sme_for_fil = lint_engine.runLinter(path_to_analyze)
              print all_sme_for_fil
              print '='*50




# cat_fil  = '/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/project-materials/rq_dataset/MOZ.csv'
# root_dir = '/Users/akond/SECU_REPOS/mozi-pupp/'

# cat_fil  = '/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/project-materials/rq_dataset/OST.csv'
# root_dir = '/Users/akond/SECU_REPOS/ostk-pupp/'

cat_fil  = '/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/project-materials/rq_dataset/WIK.csv'
root_dir = '/Users/akond/SECU_REPOS/wiki-pupp/'

if __name__=='__main__':
    t1 = time.time()
    print 'Started at:', giveTimeStamp()
    print '*'*100

    # getData(ds_dir)
    getPuppetFileDetails(cat_fil, root_dir)


    print 'Ended at:', giveTimeStamp()
    print '*'*100
    t2 = time.time()
    diff = (t2 - t1 ) / 60
    print "Duration: {} minutes".format(diff)
    print '*'*100
