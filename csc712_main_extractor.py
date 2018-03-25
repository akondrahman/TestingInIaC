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
                    month_str  = getMonthData(full_p_file, dir_p)
                    all_smells = lint_engine.runLinter(full_p_file)
                    print all_smells
                    orig_file_name = processFileName(full_p_file)
                    print '*'*50

# def getPuppetFileDetails(theCompleteCategFile):
#     dictOfAllFiles={}
#     dict2Ret={}
#     with open(theCompleteCategFile, 'rU') as file_:
#       reader_ = csv.reader(file_)
#       next(reader_, None)
#       for row_ in reader_:
#         repo_of_file       = row_[1]
#         categ_of_file      = row_[3]
#         full_path_of_file  = row_[4]
#         if full_path_of_file not in dictOfAllFiles:
#             dictOfAllFiles[full_path_of_file] = [[ categ_of_file ], repo_of_file]
#         else:
#             dictOfAllFiles[full_path_of_file][0] = dictOfAllFiles[full_path_of_file][0] + [ categ_of_file ]
#     for k_, v_ in dictOfAllFiles.items():
#        uniq = np.unique(v_[0])
#        if ((len(uniq)==1) and (uniq[0]=='N')):
#          dict2Ret[k_] = ('0', v_[1])
#        else:
#          dict2Ret[k_] = ('1', v_[1])
#     return dict2Ret


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
