'''
Akond Rahman
Lint engine for code smell detection
'''
import subprocess
import os
import numpy as np
import csc712_constants as constants
import impl_aggr
## Puppeteer stuff
from SmellDetector import SmellDectector


def getImplSmells(path2file):
    if(path2file.endswith(constants.PP_EXT)):
        lintToolCmd = constants.PP_LINT_TOOL
        try:
           command2exec = lintToolCmd + ' ' + path2file + ' ' + constants.REDIRECT_APP + ' ' + constants.OUTPUT_TMP_LOG
           subprocess.check_output([constants.BASH_CMD, constants.BASH_FLAG, command2exec])
        except subprocess.CalledProcessError as e_:
           print constants.EXCEPTION + str(e_)


def runLinter(full_path_file):
    #1. get implementation smells
    getImplSmells(full_path_file)
    #2. parse output
    impl_smel_for_file = impl_aggr.getImplSmellCount()
    #3. get Design Smells
    desi_smel_for_file = SmellDectector.getSmellsFromFile(full_path_file)
    #4. delete temp file
    os.remove(constants.OUTPUT_TMP_LOG)
    os.remove(constants.TMP_DES_TXT)
    ## returns a tuple of lists : first is implementation, second is line design
    all_smells = impl_smel_for_file + desi_smel_for_file
    return all_smells
