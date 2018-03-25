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
                    month_str      = getMonthData(full_p_file, dir_p)
                    impl_smells    = lint_engine.runLinter(full_p_file)
                    orig_file_name = processFileName(full_p_file)
                    print '*'*50

ds_dir = '/Users/akond/SECU_REPOS/test-pupp/'
if __name__=='__main__':
    t1 = time.time()
    print 'Started at:', giveTimeStamp()
    print '*'*100

    getData(ds_dir)

    print 'Ended at:', giveTimeStamp()
    print '*'*100
    t2 = time.time()
    diff = (t2 - t1 ) / 60
    print "Duration: {} minutes".format(diff)
    print '*'*100
