'''
Akond Rahman
Lint engine for code smell detection
'''
import subprocess
import os
import numpy as np
import csc712_constants as constants

def getImplSmells(path2file):
    if(path2file.endswith(constants.PP_EXT)):
        lintToolCmd = constants.PP_LINT_TOOL
        try:
           command2exec = lintToolCmd + ' ' + path2file + ' ' + constants.REDIRECT_APP + ' ' + constants.OUTPUT_TMP_LOG
           subprocess.check_output([constants.BASH_CMD, constants.BASH_FLAG, command2exec])
        except subprocess.CalledProcessError as e_:
           print constants.EXCEPTION + str(e_)


def runLinter(full_path_file):
    #1. run linter with custom rules
    getImplSmells(full_path_file)
    # 2. parse output
    # all_rul_cnt_out = parseOutput()
    #3. delete temp file
    # os.remove(constants.OUTPUT_TMP_LOG)
    ## returns a tuple: first is count, second is line string
    # return all_rul_cnt_out
