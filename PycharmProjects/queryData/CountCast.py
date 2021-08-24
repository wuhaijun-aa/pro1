import os
import sys
import re
def getDataInfo():
    path1 = "D:\\pct"
    data1 = []
    twofilelist = os.listdir(path1)
    print(twofilelist)

    for file1 in twofilelist:
        twofilepath = os.path.join(path1, file1)
        if os.path.isdir(twofilepath):
            threefilelist = os.listdir(twofilepath)
            print(threefilelist)
            if len(threefilelist) > 0:
                for i in range(len(threefilelist)):
                    threefilepath = os.path.join(twofilepath,threefilelist[i])
                    if os.path.isdir(threefilepath):
                        data1.append(threefilelist[i])

    print(data1)
    count1 = 0
    TC_22_1_1PASS = 0
    TC_22_1_1FAIL = 0
    TC_22_1_1Unknow = 0
    TC_22_2_8PASS = 0
    TC_22_2_8FAIL = 0
    TC_22_2_8Unknow = 0
    TC_22_3_1_1PASS = 0
    TC_22_3_1_1FAIL = 0
    TC_22_3_1_1Unknow = 0
    TC_22_3_1_2PASS = 0
    TC_22_3_1_2FAIL = 0
    TC_22_3_1_2Unknow = 0
    TC_22_3_1_3PASS = 0
    TC_22_3_1_3FAIL = 0
    TC_22_3_1_3Unknow = 0

    TC_22_3_1_4PASS = 0
    TC_22_3_1_4FAIL = 0
    TC_22_3_1_4Unknow = 0
    TC_22_3_1_5PASS = 0
    TC_22_3_1_5FAIL = 0
    TC_22_3_1_5Unknow = 0
    TC_22_3_1_6PASS = 0
    TC_22_3_1_6FAIL = 0
    TC_22_3_1_6Unknow = 0
    TC_22_3_1_6aPASS = 0
    TC_22_3_1_6aFAIL = 0
    TC_22_3_1_6aUnknow = 0
    TC_22_3_1_7PASS = 0
    TC_22_3_1_7FAIL = 0
    TC_22_3_1_7Unknow = 0
    TC_22_3_1_9PASS = 0
    TC_22_3_1_9FAIL = 0
    TC_22_3_1_9Unknow = 0
    TC_22_3_2_1PASS = 0
    TC_22_3_2_1FAIL = 0
    TC_22_3_2_1Unknow = 0
    TC_22_3_2_2PASS = 0
    TC_22_3_2_2FAIL = 0
    TC_22_3_2_2Unknow = 0
    TC_22_3_2_3PASS = 0
    TC_22_3_2_3FAIL = 0
    TC_22_3_2_3Unknow = 0
    TC_22_3_2_4PASS = 0
    TC_22_3_2_4FAIL = 0
    TC_22_3_2_4Unknow = 0
    TC_22_3_2_5PASS = 0
    TC_22_3_2_5FAIL = 0
    TC_22_3_2_5Unknow = 0
    TC_22_3_2_7PASS = 0
    TC_22_3_2_7FAIL = 0
    TC_22_3_2_7Unknow = 0
    TC_22_3_2_8PASS = 0
    TC_22_3_2_8FAIL = 0
    TC_22_3_2_8Unknow = 0
    TC_22_3_3_1PASS = 0
    TC_22_3_3_1FAIL = 0
    TC_22_3_3_1Unknow = 0
    TC_22_3_3_2PASS = 0
    TC_22_3_3_2FAIL = 0
    TC_22_3_3_2Unknow = 0
    TC_22_3_3_3PASS = 0
    TC_22_3_3_3FAIL = 0
    TC_22_3_3_3Unknow = 0
    TC_22_3_3_4PASS = 0
    TC_22_3_3_4FAIL = 0
    TC_22_3_3_4Unknow = 0
    TC_22_3_3_5PASS = 0
    TC_22_3_3_5FAIL = 0
    TC_22_3_3_5Unknow = 0
    TC_22_3_3_6PASS = 0
    TC_22_3_3_6FAIL = 0
    TC_22_3_3_6Unknow = 0
    TC_22_4_1PASS = 0
    TC_22_4_1FAIL = 0
    TC_22_4_1Unknow = 0
    TC_22_4_11PASS = 0
    TC_22_4_11FAIL = 0
    TC_22_4_11Unknow = 0
    TC_22_4_12PASS = 0
    TC_22_4_12FAIL = 0
    TC_22_4_12Unknow = 0
    TC_22_4_13PASS = 0
    TC_22_4_13FAIL = 0
    TC_22_4_13Unknow = 0
    TC_22_4_14PASS = 0
    TC_22_4_14FAIL = 0
    TC_22_4_14Unknow = 0
    TC_22_4_15PASS = 0
    TC_22_4_15FAIL = 0
    TC_22_4_15Unknow = 0
    TC_22_4_16PASS = 0
    TC_22_4_16FAIL = 0
    TC_22_4_16Unknow = 0
    TC_22_4_18PASS = 0
    TC_22_4_18FAIL = 0
    TC_22_4_18Unknow = 0
    TC_22_4_19aPASS = 0
    TC_22_4_19aFAIL = 0
    TC_22_4_19aUnknow = 0
    TC_22_4_2PASS = 0
    TC_22_4_2FAIL = 0
    TC_22_4_2Unknow = 0
    TC_22_4_20PASS = 0
    TC_22_4_20FAIL = 0
    TC_22_4_20Unknow = 0
    TC_22_4_2aPASS = 0
    TC_22_4_2aFAIL = 0
    TC_22_4_2aUnknow = 0
    TC_22_4_21PASS = 0
    TC_22_4_21FAIL = 0
    TC_22_4_21Unknow = 0
    TC_22_4_22PASS = 0
    TC_22_4_22FAIL = 0
    TC_22_4_22Unknow = 0
    TC_22_4_23PASS = 0
    TC_22_4_23FAIL = 0
    TC_22_4_23Unknow = 0
    TC_22_4_6PASS = 0
    TC_22_4_6FAIL = 0
    TC_22_4_6Unknow = 0
    TC_22_4_7PASS = 0
    TC_22_4_7FAIL = 0
    TC_22_4_7Unknow = 0
    TC_22_5_1PASS = 0
    TC_22_5_1FAIL = 0
    TC_22_5_1Unknow = 0
    TC_22_5_10PASS = 0
    TC_22_5_10FAIL = 0
    TC_22_5_10Unknow = 0
    TC_22_5_11PASS = 0
    TC_22_5_11FAIL = 0
    TC_22_5_11Unknow = 0
    TC_22_5_12PASS = 0
    TC_22_5_12FAIL = 0
    TC_22_5_12Unknow = 0
    TC_22_5_15PASS = 0
    TC_22_5_15FAIL = 0
    TC_22_5_15Unknow = 0


    TC_22_5_17PASS = 0
    TC_22_5_17FAIL = 0
    TC_22_5_17Unknow = 0

    TC_22_5_18PASS = 0
    TC_22_5_18FAIL = 0
    TC_22_5_18Unknow = 0

    TC_22_5_2PASS = 0
    TC_22_5_2FAIL = 0
    TC_22_5_2Unknow = 0

    TC_22_5_20PASS = 0
    TC_22_5_20FAIL = 0
    TC_22_5_20Unknow = 0

    TC_22_5_3PASS = 0
    TC_22_5_3FAIL = 0
    TC_22_5_3Unknow = 0

    TC_22_5_4PASS = 0
    TC_22_5_4FAIL = 0
    TC_22_5_4Unknow = 0

    TC_22_5_6PASS = 0
    TC_22_5_6FAIL = 0
    TC_22_5_6Unknow = 0

    TC_22_5_9PASS = 0
    TC_22_5_9FAIL = 0
    TC_22_5_9Unknow = 0
    TC_22_6_1PASS = 0
    TC_22_6_1FAIL = 0
    TC_22_6_1Unknow = 0
    TC_22_6_1aPASS = 0
    TC_22_6_1aFAIL = 0
    TC_22_6_1aUnknow = 0

    TC_22_6_2PASS = 0
    TC_22_6_2FAIL = 0
    TC_22_6_2Unknow = 0

    TC_22_6_3PASS = 0
    TC_22_6_3FAIL = 0
    TC_22_6_3Unknow = 0

    TC_22_6_5PASS = 0
    TC_22_6_5FAIL = 0
    TC_22_6_5Unknow = 0

    if len(data1) > 0:
        for i in  range(len(data1)):
            if "test3-2" in  data1[i]:
                count1 +=1
            if "TC_22_1_1" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_1_1PASS +=1
                if "FAIL" in data1[i]:
                    TC_22_1_1FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_1_1Unknow += 1
            if "TC_22_2_8" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_2_8PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_2_8FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_2_8Unknow += 1
            if "TC_22_3_1_10" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_3_1_1PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_3_1_1FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_3_1_1Unknow += 1
            if "TC_22_3_1_2" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_3_1_2PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_3_1_2FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_3_1_2Unknow += 1
            if "TC_22_3_1_3" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_3_1_3PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_3_1_3FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_3_1_3Unknow += 1
            if "TC_22_3_1_4" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_3_1_4PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_3_1_4FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_3_1_4Unknow += 1
            if "TC_22_3_1_5" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_3_1_5PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_3_1_5FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_3_1_5Unknow += 1
            if "TC_22_3_1_6" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_3_1_6PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_3_1_6FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_3_1_6Unknow += 1
            if "TC_22_3_1_6a" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_3_1_6aPASS += 1
                if "FAIL" in data1[i]:
                    TC_22_3_1_6aFAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_3_1_6aUnknow += 1

            if "TC_22_3_1_7" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_3_1_7PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_3_1_7FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_3_1_7Unknow += 1
            if "TC_22_3_1_9" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_3_1_9PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_3_1_9FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_3_1_9Unknow += 1
            if "TC_22_3_2_1" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_3_2_1PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_3_2_1FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_3_2_1Unknow += 1
            if "TC_22_3_2_2" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_3_2_2PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_3_2_2FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_3_2_2Unknow += 1
            if "TC_22_3_2_3" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_3_2_3PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_3_2_3FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_3_2_3Unknow += 1
            if "TC_22_3_2_4" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_3_2_4PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_3_2_4FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_3_2_4Unknow += 1
            if "TC_22_3_2_5" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_3_2_5PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_3_2_5FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_3_2_5Unknow += 1
            if "TC_22_3_2_7" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_3_2_7PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_3_2_7FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_3_2_7Unknow += 1
            if "TC_22_3_2_8" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_3_2_8PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_3_2_8FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_3_2_8Unknow += 1
            if "TC_22_3_3_1" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_3_3_1PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_3_3_1FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_3_3_1Unknow += 1
            if "TC_22_3_3_2" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_3_3_2PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_3_3_2FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_3_3_2Unknow += 1
            if "TC_22_3_3_3" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_3_3_3PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_3_3_3FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_3_3_3Unknow += 1
            if "TC_22_3_3_4" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_3_3_4PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_3_3_4FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_3_3_4Unknow += 1
            if "TC_22_3_3_5" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_3_3_5PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_3_3_5FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_3_3_5Unknow += 1
            if "TC_22_3_3_6" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_3_3_6PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_3_3_6FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_3_3_6Unknow += 1
            if "TC_22_4_1" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_4_1PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_4_1FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_4_1Unknow += 1

            if "TC_22_4_11" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_4_11PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_4_11FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_4_11Unknow += 1
            if "TC_22_4_12" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_4_12PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_4_12FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_4_12Unknow += 1
            if "TC_22_4_13" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_4_13PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_4_13FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_4_13Unknow += 1
            if "TC_22_4_14" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_4_14PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_4_14FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_4_14Unknow += 1
            if "TC_22_4_15" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_4_15PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_4_15FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_4_15Unknow += 1
            if "TC_22_4_16" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_4_16PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_4_16FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_4_16Unknow += 1
            if "TC_22_4_18" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_4_18PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_4_18FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_4_18Unknow += 1
            if "TC_22_4_19a" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_4_19aPASS += 1
                if "FAIL" in data1[i]:
                    TC_22_4_19aFAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_4_19aUnknow += 1
            if "TC_22_4_2" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_4_2PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_4_2FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_4_2Unknow += 1
            if "TC_22_4_20" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_4_20PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_4_20FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_4_20Unknow += 1
            if "TC_22_4_20a" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_4_2aPASS += 1
                if "FAIL" in data1[i]:
                    TC_22_4_2aFAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_4_2aUnknow += 1
            if "TC_22_4_21" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_4_21PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_4_21FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_4_21Unknow += 1

            if "TC_22_4_22" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_4_22PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_4_22FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_4_22Unknow += 1
            if "TC_22_4_23" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_4_23PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_4_23FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_4_23Unknow += 1
            if "TC_22_4_6" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_4_6PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_4_6FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_4_6Unknow += 1
            if "TC_22_4_7" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_4_7PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_4_7FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_4_7Unknow += 1
            if "TC_22_5_1" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_5_1PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_5_1FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_5_1Unknow += 1
            if "TC_22_5_10" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_5_10PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_5_10FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_5_10Unknow += 1

            if "TC_22_5_11" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_5_11PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_5_11FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_5_11Unknow += 1
            if "TC_22_5_12" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_5_12PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_5_12FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_5_12Unknow += 1

            if "TC_22_5_15" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_5_15PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_5_15FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_5_15Unknow += 1

            if "TC_22_5_17" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_5_17PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_5_17FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_5_17Unknow += 1

            if "TC_22_5_18" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_5_18PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_5_18FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_5_18Unknow += 1
            if "TC_22_5_2" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_5_2PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_5_2FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_5_2Unknow += 1
            if "TC_22_5_20" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_5_20PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_5_20FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_5_20Unknow += 1
            if "TC_22_5_3" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_5_3PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_5_3FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_5_3Unknow += 1

            if "TC_22_5_4" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_5_4PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_5_4FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_5_4Unknow += 1
            if "TC_22_5_6" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_5_6PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_5_6FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_5_6Unknow += 1
            if "TC_22_5_9" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_5_9PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_5_9FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_5_9Unknow += 1
            if "TC_22_6_1" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_6_1PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_6_1FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_6_1Unknow += 1
            if "TC_22_6_1a" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_6_1aPASS += 1
                if "FAIL" in data1[i]:
                    TC_22_6_1aFAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_6_1aUnknow += 1
            if "TC_22_6_2" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_6_2PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_6_2FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_6_2Unknow += 1
            if "TC_22_6_5" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_6_5PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_6_5FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_6_5Unknow += 1
            if "TC_22_6_3" in data1[i]:
                if "PASS" in data1[i]:
                    TC_22_6_3PASS += 1
                if "FAIL" in data1[i]:
                    TC_22_6_3FAIL += 1
                if "Unknow" or "INCONCLUSIVE" in data1[i]:
                    TC_22_6_3Unknow += 1
    print(count1)
    print("{},{},{},{}".format(count1,count1,count1,count1))

    print("TC_22_1_1执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_1_1PASS+TC_22_1_1FAIL+TC_22_1_1Unknow), TC_22_1_1PASS, TC_22_1_1FAIL, TC_22_1_1Unknow))
    print("TC_22_2_8执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_2_8PASS+TC_22_2_8FAIL+TC_22_2_8Unknow), TC_22_2_8PASS, TC_22_2_8FAIL, TC_22_2_8Unknow))
    print("TC_22_3_1_1执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_3_1_1PASS+TC_22_3_1_1FAIL+TC_22_3_1_1Unknow), TC_22_3_1_1PASS, TC_22_3_1_1FAIL, TC_22_3_1_1Unknow))
    print("TC_22_3_1_2执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_3_1_2PASS+TC_22_3_1_2FAIL+TC_22_3_1_2Unknow), TC_22_3_1_2PASS, TC_22_3_1_2FAIL, TC_22_3_1_2Unknow))
    print("TC_22_3_1_3执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_3_1_3PASS+TC_22_3_1_3FAIL+TC_22_3_1_3Unknow), TC_22_3_1_3PASS, TC_22_3_1_3FAIL, TC_22_3_1_3Unknow))
    print("TC_22_3_1_4执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_3_1_4PASS+TC_22_3_1_4FAIL+TC_22_3_1_4Unknow), TC_22_3_1_4PASS, TC_22_3_1_4FAIL, TC_22_3_1_4Unknow))
    print("TC_22_3_1_5执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_3_1_5PASS+TC_22_3_1_5FAIL+TC_22_3_1_5Unknow), TC_22_3_1_5PASS, TC_22_3_1_5FAIL, TC_22_3_1_5Unknow))
    print("TC_22_3_1_6执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_3_1_6PASS+TC_22_3_1_6FAIL+TC_22_3_1_6Unknow), TC_22_3_1_6PASS, TC_22_3_1_6FAIL, TC_22_3_1_6Unknow))
    print("TC_22_3_1_6a执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_3_1_6aPASS+TC_22_3_1_6aFAIL+TC_22_3_1_6aUnknow), TC_22_3_1_6aPASS, TC_22_3_1_6aFAIL, TC_22_3_1_6aUnknow))
    print("TC_22_3_1_7执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_3_1_7PASS+TC_22_3_1_7FAIL+TC_22_3_1_7Unknow), TC_22_3_1_7PASS, TC_22_3_1_7FAIL, TC_22_3_1_7Unknow))
    print("TC_22_3_1_9执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_3_1_9PASS+TC_22_3_1_9FAIL+TC_22_3_1_9Unknow), TC_22_3_1_9PASS, TC_22_3_1_9FAIL, TC_22_3_1_9Unknow))
    print("TC_22_3_2_1执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_3_2_1PASS+TC_22_3_2_1FAIL+TC_22_3_2_1Unknow), TC_22_3_2_1PASS, TC_22_3_2_1FAIL, TC_22_3_2_1Unknow))
    print("TC_22_3_2_2执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_3_2_2PASS+TC_22_3_2_2FAIL+TC_22_3_2_2Unknow), TC_22_3_2_2PASS, TC_22_3_2_2FAIL, TC_22_3_2_2Unknow))
    print("TC_22_3_2_3执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_3_2_3PASS+TC_22_3_2_3FAIL+TC_22_3_2_3Unknow), TC_22_3_2_3PASS, TC_22_3_2_3FAIL, TC_22_3_2_3Unknow))
    print("TC_22_3_2_4执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_3_2_4PASS+TC_22_3_2_4FAIL+TC_22_3_2_4Unknow), TC_22_3_2_4PASS, TC_22_3_2_4FAIL, TC_22_3_2_4Unknow))
    print("TC_22_3_2_5执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_3_2_5PASS+TC_22_3_2_5FAIL+TC_22_3_2_5Unknow), TC_22_3_2_5PASS, TC_22_3_2_5FAIL, TC_22_3_2_5Unknow))
    print("TC_22_3_2_7执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_3_2_7PASS+TC_22_3_2_7FAIL+TC_22_3_2_7Unknow), TC_22_3_2_7PASS, TC_22_3_2_7FAIL, TC_22_3_2_7Unknow))
    print("TC_22_3_2_8执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_3_2_8PASS+TC_22_3_2_8FAIL+TC_22_3_2_8Unknow), TC_22_3_2_8PASS, TC_22_3_2_8FAIL, TC_22_3_2_8Unknow))
    print("TC_22_3_3_1执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_3_3_1PASS+TC_22_3_3_1FAIL+TC_22_3_3_1Unknow), TC_22_3_3_1PASS, TC_22_3_3_1FAIL, TC_22_3_3_1Unknow))
    print("TC_22_3_3_2执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_3_3_2PASS+TC_22_3_3_2FAIL+TC_22_3_3_2Unknow), TC_22_3_3_2PASS, TC_22_3_3_2FAIL, TC_22_3_3_2Unknow))
    print("TC_22_3_3_3执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_3_3_3PASS+TC_22_3_3_3FAIL+TC_22_3_3_3Unknow), TC_22_3_3_3PASS, TC_22_3_3_3FAIL, TC_22_3_3_3Unknow))
    print("TC_22_3_3_4执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_3_3_4PASS+TC_22_3_3_4FAIL+TC_22_3_3_4Unknow), TC_22_3_3_4PASS, TC_22_3_3_4FAIL, TC_22_3_3_4Unknow))
    print("TC_22_3_3_5执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_3_3_5PASS+TC_22_3_3_5FAIL+TC_22_3_3_5Unknow), TC_22_3_3_5PASS, TC_22_3_3_5FAIL, TC_22_3_3_5Unknow))
    print("TC_22_3_3_6执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_3_3_6PASS+TC_22_3_3_6FAIL+TC_22_3_3_6Unknow), TC_22_3_3_6PASS, TC_22_3_3_6FAIL, TC_22_3_3_6Unknow))
    print("TC_22_4_1执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_4_1PASS+TC_22_4_1FAIL+TC_22_4_1Unknow), TC_22_4_1PASS, TC_22_4_1FAIL, TC_22_4_1Unknow))
    print("TC_22_4_11执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_4_11PASS+TC_22_4_11FAIL+TC_22_4_11Unknow), TC_22_4_11PASS, TC_22_4_11FAIL, TC_22_4_11Unknow))
    print("TC_22_4_13执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_4_13PASS+TC_22_4_13FAIL+TC_22_4_13Unknow), TC_22_4_13PASS, TC_22_4_13FAIL, TC_22_4_13Unknow))
    print("TC_22_4_12执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_4_12PASS+TC_22_4_12FAIL+TC_22_4_12Unknow), TC_22_4_12PASS, TC_22_4_12FAIL, TC_22_4_12Unknow))
    print("TC_22_4_14执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_4_14PASS+TC_22_4_14FAIL+TC_22_4_14Unknow), TC_22_4_14PASS, TC_22_4_14FAIL, TC_22_4_14Unknow))
    print("TC_22_4_15执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_4_15PASS+TC_22_4_15FAIL+TC_22_4_15Unknow), TC_22_4_15PASS, TC_22_4_15FAIL, TC_22_4_15Unknow))
    print("TC_22_4_16执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_4_16PASS+TC_22_4_16FAIL+TC_22_4_16Unknow), TC_22_4_16PASS, TC_22_4_16FAIL, TC_22_4_16Unknow))
    print("TC_22_4_18执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_4_18PASS+TC_22_4_18FAIL+TC_22_4_18Unknow), TC_22_4_18PASS, TC_22_4_18FAIL, TC_22_4_18Unknow))
    print("TC_22_4_19a执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_4_19aPASS+TC_22_4_19aFAIL+TC_22_4_19aUnknow), TC_22_4_19aPASS, TC_22_4_19aFAIL, TC_22_4_19aUnknow))
    print("TC_22_4_2执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_4_2PASS+TC_22_4_2FAIL+TC_22_4_2Unknow), TC_22_4_2PASS, TC_22_4_2FAIL, TC_22_4_2Unknow))
    print("TC_22_4_20执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_4_20PASS+TC_22_4_20FAIL+TC_22_4_20Unknow), TC_22_4_20PASS, TC_22_4_20FAIL, TC_22_4_20Unknow))
    print("TC_22_4_21执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_4_21PASS+TC_22_4_21FAIL+TC_22_4_21Unknow), TC_22_4_21PASS, TC_22_4_21FAIL, TC_22_4_21Unknow))
    print("TC_22_4_20a执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_4_2aPASS+TC_22_4_2aFAIL+TC_22_4_2aUnknow), TC_22_4_2aPASS, TC_22_4_2aFAIL, TC_22_4_2aUnknow))
    print("TC_22_4_22执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_4_22PASS+TC_22_4_22FAIL+TC_22_4_22Unknow), TC_22_4_22PASS, TC_22_4_22FAIL, TC_22_4_22Unknow))
    print("TC_22_4_23执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_4_23PASS+TC_22_4_23FAIL+TC_22_4_23Unknow), TC_22_4_23PASS, TC_22_4_23FAIL, TC_22_4_23Unknow))
    print("TC_22_4_6执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_4_6PASS+TC_22_4_6FAIL+TC_22_4_6Unknow), TC_22_4_6PASS, TC_22_4_6FAIL, TC_22_4_6Unknow))
    print("TC_22_4_7执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_4_7PASS+TC_22_4_7FAIL+TC_22_4_7Unknow), TC_22_4_7PASS, TC_22_4_7FAIL, TC_22_4_7Unknow))
    print("TC_22_5_1执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_5_1PASS+TC_22_5_1FAIL+TC_22_5_1Unknow), TC_22_5_1PASS, TC_22_5_1FAIL, TC_22_5_1Unknow))
    print("TC_22_5_10执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_5_10PASS+TC_22_5_10FAIL+TC_22_5_10Unknow), TC_22_5_10PASS, TC_22_5_10FAIL, TC_22_5_10Unknow))
    print("TC_22_5_11执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_5_11PASS+TC_22_5_11FAIL+TC_22_5_11Unknow), TC_22_5_11PASS, TC_22_5_11FAIL, TC_22_5_11Unknow))
    print("TC_22_5_12执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_5_12PASS+TC_22_5_12FAIL+TC_22_5_12Unknow), TC_22_5_12PASS, TC_22_5_12FAIL, TC_22_5_12Unknow))
    print("TC_22_5_17执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_5_17PASS+TC_22_5_17FAIL+TC_22_5_17Unknow), TC_22_5_17PASS, TC_22_5_17FAIL, TC_22_5_17Unknow))
    print("TC_22_5_15执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_5_15PASS+TC_22_5_15FAIL+TC_22_5_15Unknow), TC_22_5_15PASS, TC_22_5_15FAIL, TC_22_5_15Unknow))
    print("TC_22_5_18执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_5_18PASS+TC_22_5_18FAIL+TC_22_5_18Unknow), TC_22_5_18PASS, TC_22_5_18FAIL, TC_22_5_18Unknow))
    print("TC_22_5_2执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_5_2PASS+TC_22_5_2FAIL+TC_22_5_2Unknow), TC_22_5_2PASS, TC_22_5_2FAIL, TC_22_5_2Unknow))
    print("TC_22_5_20执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_5_20PASS+TC_22_5_20FAIL+TC_22_5_20Unknow), TC_22_5_20PASS, TC_22_5_20FAIL, TC_22_5_20Unknow))
    print("TC_22_5_3执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_5_3PASS+TC_22_5_3FAIL+TC_22_5_3Unknow), TC_22_5_3PASS, TC_22_5_3FAIL, TC_22_5_3Unknow))
    print("TC_22_5_4执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_5_4PASS+TC_22_5_4FAIL+TC_22_5_4Unknow), TC_22_5_4PASS, TC_22_5_4FAIL, TC_22_5_4Unknow))
    print("TC_22_5_6执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_5_6PASS+TC_22_5_6FAIL+TC_22_5_6Unknow), TC_22_5_6PASS, TC_22_5_6FAIL, TC_22_5_6Unknow))
    print("TC_22_5_9执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_5_9PASS+TC_22_5_9FAIL+TC_22_5_9Unknow), TC_22_5_9PASS, TC_22_5_9FAIL, TC_22_5_9Unknow))
    print("TC_22_6_1执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_6_1PASS+TC_22_6_1FAIL+TC_22_6_1Unknow), TC_22_6_1PASS, TC_22_6_1FAIL, TC_22_6_1Unknow))
    print("TC_22_6_1a执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_6_1aPASS+TC_22_6_1aFAIL+TC_22_6_1aUnknow), TC_22_6_1aPASS, TC_22_6_1aFAIL, TC_22_6_1aUnknow))
    print("TC_22_6_5执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_6_5PASS+TC_22_6_5FAIL+TC_22_6_5Unknow), TC_22_6_5PASS, TC_22_6_5FAIL, TC_22_6_5Unknow))
    print("TC_22_6_2执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_6_2PASS+TC_22_6_2FAIL+TC_22_6_2Unknow), TC_22_6_2PASS, TC_22_6_2FAIL, TC_22_6_2Unknow))
    print("TC_22_6_3执行总数{},PASS个数{},FAIL个数{}，Unknown总数{}".format((TC_22_6_3PASS+TC_22_6_3FAIL+TC_22_6_3Unknow), TC_22_6_3PASS, TC_22_6_3FAIL, TC_22_6_3Unknow))


if __name__ == '__main__':
    getDataInfo()