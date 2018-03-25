'''
Akond Rahman
Lint engine for code smell detection
'''
import subprocess
import os
import numpy as np
import csc712_constants as constants

def generateOutput(path2file):
    ## Add rules to check automatically here
    if(path2file.endswith(constants.PP_EXT)):
        lintToolCmd = constants.PP_LINT_TOOL
        try:
           command2exec = lintToolCmd + ' ' + path2file + ' ' + constants.REDIRECT_APP + ' ' + constants.OUTPUT_TMP_LOG
           subprocess.check_output([constants.BASH_CMD, constants.BASH_FLAG, command2exec])
        except subprocess.CalledProcessError as e_:
           print constants.EXCEPTION + str(e_)
