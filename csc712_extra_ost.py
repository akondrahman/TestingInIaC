'''
Extra work to get month data for OST website
'''
import csv
import pandas as pd
import os

def getTimeInfo(id_param, repo_param):
    dict2see = {}
    if repo_param.endswith('/'):
       repo_param = repo_param
    else:
       repo_param = repo_param + '/'
    file2read = repo_param + 'fullThrottle_msg_file_map.csv'
    with open(file2read, 'rU') as f:
         reader_ = csv.reader(f)
         for row in reader_:
             id_       = row[0]
             ts_    = row[2]
             dict2see[id_] = ts_
    return dict2see[id_param]

def getAllMonthsFromDataset(categ_file_param):
       str2write = ''
       df_list = []
       '''
       dicionary to hold files for each month
       '''
       month_file_dict, defect_file_dict, repo_file_dict = {}, {}, {}
       with open(categ_file_param, 'rU') as f:
         reader_ = csv.reader(f)
         next(reader_, None)
         for row in reader_:
             id_       = row[0]
             repo_     = row[1]
             categ_    = row[2]
             filepath_ = row[3]
             size_     = row[4]
             loc_      = row[5]
             authors_  = row[6]
             time_ = getTimeInfo(id_, repo_)
             time2write = time_.split(' ')[0]
             msg_       = 'DUMMY' # dummy variable
             df_list.append((id_, repo_, msg_, categ_, filepath_, time2write, size_, loc_, authors_))
       month_df = pd.DataFrame([x for x in df_list], columns=['msgid','repo', 'msgtxt', 'categ','filepath','date','size','loc','authorCount'])
       print month_df.head()



if __name__=='__main__':
    categ_file_ = '/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/Openstack.Categ.For.DB.csv'
    getAllMonthsFromDataset(categ_file_)
