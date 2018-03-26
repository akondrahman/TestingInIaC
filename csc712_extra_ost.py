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
       with open(categ_file_param, 'rU') as f:
         reader_ = csv.reader(f)
         next(reader_, None)
         for row in reader_:
             id_       = row[0]
             repo_     = row[1]
             if 'Openstack' in categ_file_param:
                 msg_       = 'DUMMY' # dummy variable
                 categ_    = row[2]
                 filepath_ = row[3]
                 size_     = row[4]
                 loc_      = row[5]
                 authors_  = row[6]
             else:
                 msg_      = row[2]
                 categ_    = row[3]
                 filepath_ = row[4]
                 size_     = row[6]
                 loc_      = row[7]
                 authors_  = row[8]
             time_ = getTimeInfo(id_, repo_)
             time2write = time_.split(' ')[0]

             df_list.append((id_, repo_, msg_, categ_, filepath_, time2write, size_, loc_, authors_))
       month_df = pd.DataFrame([x for x in df_list], columns=['msgid','repo', 'msgtxt', 'categ','filepath','date','size','loc','authorCount'])
       # print month_df.head()
       # month_df.to_csv('/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/Wikimedia.Categ.For.CSC712.csv')
       # month_df.to_csv('/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/Openstack.Categ.For.CSC712.csv')
       # month_df.to_csv('/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/Mozilla.Categ.For.CSC712.csv')


if __name__=='__main__':
    # categ_file_ = '/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/Mozilla.Final.Categ.csv'
    # categ_file_ = '/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/Openstack.Categ.For.DB.csv'
    # categ_file_ = '/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Defect-Categ-Project/output/Wikimedia.Final.Categ.csv'
    getAllMonthsFromDataset(categ_file_)
