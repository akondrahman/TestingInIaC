'''
Mining Van Der Bent Metrics
Akond Rahman
Jun 13, 2018
'''
import csv
from SmellDetector import SmellDectector
import csc712_lint_engine as linter
import os

def getFiles(categ_file_name):
    file_list = []
    with open(categ_file_name, 'rU') as file_:
      reader_ = csv.reader(file_)
      next(reader_, None)
      for row_ in reader_:
        full_path_of_file       = row_[1]
        defect_status_of_file   = row_[-1]
        if os.path.exists(full_path_of_file):
           file_list.append((full_path_of_file, defect_status_of_file))
    return file_list

def dumpContentIntoFile(strP, fileP):
    fileToWrite = open( fileP, 'w')
    fileToWrite.write(strP )
    fileToWrite.close()
    return str(os.stat(fileP).st_size)

if __name__=='__main__':
   all_file_str = ''

   # dataset_file  = "/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Tree/dataset/phase11-icse19-tse/PHASE11_MIR_FULL_DATASET.csv"
   # out_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/dataset-icse19-tse/MIR_VDB.csv'

   # dataset_file  = "/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Tree/dataset/phase11-icse19-tse/PHASE11_MOZ_FULL_DATASET.csv"
   # out_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/dataset-icse19-tse/MOZ_VDB.csv'

   # dataset_file  = "/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Tree/dataset/phase11-icse19-tse/PHASE11_OST_FULL_DATASET.csv"
   # out_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/dataset-icse19-tse/OST_VDB.csv'

   # dataset_file  = "/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Tree/dataset/phase11-icse19-tse/PHASE11_WIK_FULL_DATASET.csv"
   # out_file = '/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/dataset-icse19-tse/WIK_VDB.csv'

   all_fil_nam = getFiles(dataset_file)

   for file_tupl in all_fil_nam:
       # file_ = '/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/TestingInIaC/vanderbent/lol.pp'
       file_ = file_tupl[0]
       defect_status_of_file = file_tupl[1]
       non_lint_metrics = SmellDectector.getVanDerBentMetrics(file_)
       sum_lint_metrics = sum(linter.getLintMetrics(file_))
       vdb_met = non_lint_metrics + str(sum_lint_metrics)
       print file_, vdb_met, defect_status_of_file
       all_file_str = all_file_str + file_ + ',' + vdb_met + ',' + str(defect_status_of_file) + '\n'
       print '*'*50
   all_file_str = 'FILE,SLOC,COMPLEXITY,EXEC,PARAMS,DEPENDENCY,WARNINGS,DEFECT' + '\n' + all_file_str
   dump_status = dumpContentIntoFile(all_file_str, out_file)
   print 'Dumped a file of {} bytes'.format(dump_status)
   print '='*100
