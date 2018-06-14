'''
Puppet lint aggregator
Reff: https://github.com/tushartushar/Puppeteer/blob/master/Puppet-lint_aggregator/Aggregator.py
'''
# Puppeteer stuff
import PLConstants as CONSTS
import os
# my stuff
import csc712_constants as constants

def getImplSmellCount():
    rule1_count  = 0
    rule2_count  = 0
    rule3_count  = 0
    rule4_count  = 0
    rule5_count  = 0
    rule6_count  = 0
    rule7_count  = 0
    rule8_count  = 0
    rule9_count  = 0
    rule10_count = 0
    rule11_count = 0
    rule12_count = 0
    rule13_count = 0

    if os.path.exists(constants.OUTPUT_TMP_LOG):
        with open(constants.OUTPUT_TMP_LOG, constants.FILE_OPEN_MODE) as curFile:
            for line in curFile:
                rule1_count = getrule1_count(rule1_count, line)
                rule2_count = getrule2_count(rule2_count, line)
                rule3_count = getrule3_count(rule3_count, line)
                rule4_count = getrule4_count(rule4_count, line)
                rule5_count = getrule5_count(rule5_count, line)
                rule6_count = getrule6_count(rule6_count, line)
                rule7_count = getrule7_count(rule7_count, line)
                rule8_count = getrule8_count(rule8_count, line)
                rule9_count = getrule9_count(rule9_count, line)
                rule10_count = getrule10_count(rule10_count, line)
                rule11_count = getrule11_count(rule11_count, line)
                rule12_count = getrule12_count(rule12_count, line)
                rule13_count = getrule13_count(rule13_count, line)

    return [rule1_count, rule2_count, rule3_count, rule4_count, rule5_count, rule6_count, rule7_count,
            rule8_count, rule9_count, rule10_count, rule11_count, rule12_count, rule13_count
           ]

def getrule1_count(count, line):
    index = line.find(CONSTS.RULE1_1)
    if index >= 0:
        count += 1
    return count

def getrule2_count(count, line):
    index = line.find(CONSTS.RULE2_1)
    if index >= 0:
        count += 1

    index = line.find(CONSTS.RULE2_2)
    if index >= 0:
        count += 1
    return count

def getrule3_count(count, line):
    index = line.find(CONSTS.RULE3_1)
    if index >= 0:
        count += 1
    return count

def getrule4_count(count, line):
    index = line.find(CONSTS.RULE4_1)
    if index >= 0:
        count += 1
    return count

def getrule5_count(count, line):
    index = line.find(CONSTS.RULE5_1)
    if index >= 0:
        count += 1
    index = line.find(CONSTS.RULE5_2)
    if index >= 0:
        count += 1
    return count

def getrule6_count(count, line):
    index = line.find(CONSTS.RULE6_1)
    if index >= 0:
        count += 1
    index = line.find(CONSTS.RULE6_2)
    if index >= 0:
        count += 1
    index = line.find(CONSTS.RULE6_3)
    if index >= 0:
        count += 1
    index = line.find(CONSTS.RULE6_4)
    if index >= 0:
        count += 1
    return count

def getrule7_count(count, line):
    index = line.find(CONSTS.RULE7_1)
    if index >= 0:
        count += 1
    index = line.find(CONSTS.RULE7_2)
    if index >= 0:
        count += 1
    index = line.find(CONSTS.RULE7_3)
    if index >= 0:
        count += 1
    return count

def getrule8_count(count, line):
    index = line.find(CONSTS.RULE8_1)
    if index >= 0:
        count += 1
    return count

def getrule9_count(count, line):
    index = line.find(CONSTS.RULE9_1)
    if index >= 0:
        count += 1
    return count

def getrule10_count(count, line):
    index = line.find(CONSTS.RULE10_1)
    if index >= 0:
        count += 1
    index = line.find(CONSTS.RULE10_2)
    if index >= 0:
        count += 1
    index = line.find(CONSTS.RULE10_3)
    if index >= 0:
        count += 1
    index = line.find(CONSTS.RULE10_4)
    if index >= 0:
        count += 1
    index = line.find(CONSTS.RULE10_5)
    if index >= 0:
        count += 1
    index = line.find(CONSTS.RULE10_6)
    if index >= 0:
        count += 1
    return count

def getrule11_count(count, line):
    index = line.find(CONSTS.RULE11_1)
    if index >= 0:
        count += 1
    return count

def getrule12_count(count, line):
    index = line.find(CONSTS.RULE12_1)
    if index >= 0:
        count += 1
    return count

def getrule13_count(count, line):
    index = line.find(CONSTS.RULE13_1)
    if index >= 0:
        count += 1
    return count


'''
Van der Bent Metrics: Warning Only
'''
def getrule1_vdb(count, line):
    index = line.find(CONSTS.VDB1)
    if index >= 0:
        count += 1
    return count

def getrule2_vdb(count, line):
    index = line.find(CONSTS.VDB2)
    if index >= 0:
        count += 1
    return count
def getrule3_vdb(count, line):
    index = line.find(CONSTS.VDB3)
    if index >= 0:
        count += 1
    return count

def getrule4_vdb(count, line):
    index = line.find(CONSTS.VDB4)
    if index >= 0:
        count += 1
    return count

def getrule5_vdb(count, line):
    index = line.find(CONSTS.VDB5)
    if index >= 0:
        count += 1
    return count

def getrule6_vdb(count, line):
    index = line.find(CONSTS.VDB6)
    if index >= 0:
        count += 1
    return count

def getrule7_vdb(count, line):
    index = line.find(CONSTS.VDB7)
    if index >= 0:
        count += 1
    return count
def getrule8_vdb(count, line):
    index = line.find(CONSTS.VDB8)
    if index >= 0:
        count += 1
    return count

def getrule9_vdb(count, line):
    index = line.find(CONSTS.VDB9)
    if index >= 0:
        count += 1
    return count

def getrule10_vdb(count, line):
    index = line.find(CONSTS.VDB10)
    if index >= 0:
        count += 1
    return count

def getrule11_vdb(count, line):
    index = line.find(CONSTS.VDB11)
    if index >= 0:
        count += 1
    return count

def getrule12_vdb(count, line):
    index = line.find(CONSTS.VDB12)
    if index >= 0:
        count += 1
    return count
def getrule13_vdb(count, line):
    index = line.find(CONSTS.VDB13)
    if index >= 0:
        count += 1
    return count

def getrule14_vdb(count, line):
    index = line.find(CONSTS.VDB14)
    if index >= 0:
        count += 1
    return count

def getrule15_vdb(count, line):
    index = line.find(CONSTS.VDB15)
    if index >= 0:
        count += 1
    return count


def getVanDerBentWarningCount():
    rule1_count  = 0
    rule2_count  = 0
    rule3_count  = 0
    rule4_count  = 0
    rule5_count  = 0
    rule6_count  = 0
    rule7_count  = 0
    rule8_count  = 0
    rule9_count  = 0
    rule10_count = 0
    rule11_count = 0
    rule12_count = 0
    rule13_count = 0
    rule14_count = 0  ### rule14 has two of the documentation warnings included

    if os.path.exists(constants.OUTPUT_TMP_LOG):
        with open(constants.OUTPUT_TMP_LOG, constants.FILE_OPEN_MODE) as curFile:
            for line in curFile:
                rule1_count = getrule1_vdb(rule1_count, line)
                rule2_count = getrule2_vdb(rule2_count, line)
                rule3_count = getrule3_vdb(rule3_count, line)
                rule4_count = getrule4_vdb(rule4_count, line)
                rule5_count = getrule5_vdb(rule5_count, line)

                rule6_count = getrule1_vdb(rule6_count, line)
                rule7_count = getrule2_vdb(rule7_count, line)
                rule8_count = getrule3_vdb(rule8_count, line)
                rule9_count = getrule4_vdb(rule9_count, line)
                rule10_count= getrule5_vdb(rule10_count, line)

                rule11_count = getrule1_vdb(rule11_count, line)
                rule12_count = getrule2_vdb(rule12_count, line)
                rule13_count = getrule3_vdb(rule13_count, line)
                rule14_count = getrule4_vdb(rule14_count, line)

    return [rule1_count, rule2_count, rule3_count, rule4_count, rule5_count, rule6_count, rule7_count,
            rule8_count, rule9_count, rule10_count, rule11_count, rule12_count, rule13_count, rule14_count
           ]
