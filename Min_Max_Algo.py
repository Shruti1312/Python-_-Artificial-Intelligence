import os

class Applicant:
    applicantId = ""
    isFemale = False
    isOver17 = False
    havePets = False
    haveMedicalCoditions = False
    haveCar = False
    haveDrivingLicence = False
    DaysRequired = 0
    isMonRequired = 0
    isTuesRequired = 0
    isWedRequired = 0
    isThursRequired = 0
    isFriRequired = 0
    isSatRequired = 0
    isSunRequired = 0

class AppInfo:
    nLHSABeds = 0
    nSPLASpaces = 0
    nLHSA = 0
    applicantsLHSA = { }
    nSPLA = 0
    applicantsSPLA = { }
    nTotal = 0
    applicants = { }

problemInfo = AppInfo()
totalApplicantsInfo = {}
nextApplicantToBeSelected = ""

def GetProblemInfo(filename):
    f = open(filename)
    lines = f.readlines()
    numberLHSABeds = lines[0]
    numberSPLASpaces = lines[1]
    numberLHSA = lines[2]
    applicantsLHSA = []
    i = 3
    while i < int(numberLHSA) + 3:
        applicantsLHSA.append(lines[i])
        i = i + 1

    numberSPLA = lines[i]
    applicantsSPLA = []
    j = i + 1
    while j < (int(numberSPLA) + i + 1):
        applicantsSPLA.append(lines[j])
        j = j+1

    numberTotal = lines[j]
    applicantsTotal = []
    w= j + 1
    while w < int(numberTotal) + j + 1:
        applicantsTotal.append(lines[w])
        w = w+1

    problemInfo.nLHSABeds =  numberLHSABeds
    problemInfo.nSPLASpaces = numberSPLASpaces
    problemInfo.nLHSA = numberLHSABeds
    problemInfo.applicantsLHSA = applicantsLHSA
    problemInfo.nSPLA = numberSPLA
    problemInfo.applicantsSPLA = applicantsSPLA
    problemInfo.nTotal = numberTotal
    problemInfo.applicants =  applicantsTotal

def ParseApplicantInfo():
    for x in problemInfo.applicants:
        applicant = Applicant()
        applicant.applicantId = x[0:5]
        if x[5:6] ==  "F":
            applicant.isFemale = True
        else: applicant.isFemale = False
        if int(x[6:9]) > 17:
            applicant.isOver17 = True
        else: applicant.isOver17 = False
        if x[9:10] ==  "Y":
            applicant.havePets = True
        else: applicant.havePets = False
        if x[10:11] ==  "Y":
            applicant.haveMedicalCoditions = True
        else: applicant.haveMedicalCoditions = False
        if x[11:12] ==  "Y":
            applicant.haveCar = True
        else: applicant.haveCar = False
        if x[12:13] ==  "Y":
            applicant.haveDrivingLicence = True
        else: applicant.haveDrivingLicence = False
        stayDays = 0
        if x[13:14] ==  "1":
            stayDays = stayDays + 1
            applicant.isMonRequired = 1
        if x[14:15] ==  "1":
            stayDays = stayDays + 1
            applicant.isTuesRequired = 1
        if x[15:16] ==  "1":
            stayDays = stayDays + 1
            applicant.isWedRequired = 1
        if x[16:17] ==  "1":
           stayDays = stayDays + 1
           applicant.isThursRequired = 1
        if x[17:18] ==  "1":
           stayDays = stayDays + 1
           applicant.isFriRequired = 1
        if x[18:19] ==  "1":
           stayDays = stayDays + 1
           applicant.isSatRequired = 1
        if x[19:20] ==  "1":
            stayDays = stayDays + 1
            applicant.isSunRequired = 1

        applicant.DaysRequired = stayDays
        totalApplicantsInfo[applicant.applicantId] = applicant

def PrintNextApplicantToBePintedBySPLA():
    monCountLHSA = 0
    tueCountLHSA = 0
    wedCountLHSA = 0
    thursCountLHSA = 0
    friCountLHSA = 0
    satCountLHSA = 0
    sunCountLHSA = 0

    monCountSPLA = 0
    tueCountSPLA = 0
    wedCountSPLA= 0
    thursCountSPLA = 0
    friCountSPLA = 0
    satCountSPLA = 0
    sunCountSPLA = 0

    for x in problemInfo.applicantsLHSA:
        monCountLHSA = monCountLHSA + totalApplicantsInfo[x.rstrip()].isMonRequired
        tueCountLHSA = tueCountLHSA + totalApplicantsInfo[x.rstrip()].isTuesRequired
        wedCountLHSA = wedCountLHSA + totalApplicantsInfo[x.rstrip()].isWedRequired
        thursCountLHSA = thursCountLHSA + totalApplicantsInfo[x.rstrip()].isThursRequired
        friCountLHSA = friCountLHSA + totalApplicantsInfo[x.rstrip()].isFriRequired
        satCountLHSA = satCountLHSA + totalApplicantsInfo[x.rstrip()].isSatRequired
        sunCountLHSA = sunCountLHSA + totalApplicantsInfo[x.rstrip()].isSunRequired
        totalApplicantsInfo.pop(x.rstrip())

    for x in problemInfo.applicantsSPLA:
        monCountSPLA = monCountSPLA + totalApplicantsInfo[x.rstrip()].isMonRequired
        tueCountSPLA = tueCountSPLA + totalApplicantsInfo[x.rstrip()].isTuesRequired
        wedCountSPLA = wedCountSPLA + totalApplicantsInfo[x.rstrip()].isWedRequired
        thursCountSPLA = thursCountSPLA + totalApplicantsInfo[x.rstrip()].isThursRequired
        friCountSPLA = friCountSPLA + totalApplicantsInfo[x.rstrip()].isFriRequired
        satCountSPLA = satCountSPLA + totalApplicantsInfo[x.rstrip()].isSatRequired
        sunCountSPLA = sunCountSPLA + totalApplicantsInfo[x.rstrip()].isSunRequired
        totalApplicantsInfo.pop(x.rstrip())

    #To be Deleted
    print "FOR SPLA"
    print("Monday Count ********", monCountSPLA)
    print("Tuesday Count ********", tueCountSPLA)
    print("Wednesday Count ********", wedCountSPLA)
    print("Thursday Count ********", thursCountSPLA)
    print("Friday Count ********", friCountSPLA)
    print("Saturday Count ********", satCountSPLA)
    print("Sunday Count ********", sunCountSPLA)

    #To be Deleted
    print "FOR LHSA"
    print("Monday Count ********", monCountLHSA)
    print("Tuesday Count ********", tueCountLHSA)
    print("Wednesday Count ********", wedCountLHSA)
    print("Thursday Count ********", thursCountLHSA)
    print("Friday Count ********", friCountLHSA)
    print("Saturday Count ********", satCountLHSA)
    print("Sunday Count ********", sunCountLHSA)

    choicesForFuture = { }
    for x, y in totalApplicantsInfo.items():
        if not y.haveCar or not y.haveDrivingLicence or y.haveMedicalCoditions:
            totalApplicantsInfo.pop(x.rstrip())
        elif y.isMonRequired == 1 and monCountSPLA == int(problemInfo.nSPLASpaces):
            print("Removing *********** ", x)
            totalApplicantsInfo.pop(x.rstrip())
        elif y.isTuesRequired == 1 and tueCountSPLA == int(problemInfo.nSPLASpaces):
            print("Removing *********** ", x)
            totalApplicantsInfo.pop(x.rstrip())
        elif y.isWedRequired == 1 and wedCountSPLA == int(problemInfo.nSPLASpaces):
            print("Removing *********** ", x)
            totalApplicantsInfo.pop(x.rstrip())
        elif y.isThursRequired == 1 and thursCountSPLA == int(problemInfo.nSPLASpaces):
            print("Removing *********** ", x)
            totalApplicantsInfo.pop(x.rstrip())
        elif y.isFriRequired == 1 and friCountSPLA == int(problemInfo.nSPLASpaces):
            print("Removing *********** ", x)
            totalApplicantsInfo.pop(x.rstrip())
        elif y.isSatRequired == 1 and satCountSPLA == int(problemInfo.nSPLASpaces):
            print("Removing *********** ", x)
            totalApplicantsInfo.pop(x.rstrip())
        elif y.isSunRequired == 1 and sunCountSPLA == int(problemInfo.nSPLASpaces):
            print("Removing *********** ", x)
            totalApplicantsInfo.pop(x.rstrip())
        elif not y.isFemale or y.havePets:
            choicesForFuture[x.rstrip()] = y
            totalApplicantsInfo.pop(x.rstrip())
        elif y.isFemale and not y.isOver17:
             choicesForFuture[x.rstrip()] = y
             totalApplicantsInfo.pop(x.rstrip())
        elif y.isMonRequired == 1 and monCountLHSA == int(problemInfo.nLHSABeds):
            print("Adding *********** ", x)
            choicesForFuture[x.rstrip()] = y
            totalApplicantsInfo.pop(x.rstrip())
        elif y.isTuesRequired == 1 and tueCountLHSA == int(problemInfo.nLHSABeds):
            print("Adding *********** ", x)
            choicesForFuture[x.rstrip()] = y
            totalApplicantsInfo.pop(x.rstrip())
        elif y.isWedRequired == 1 and wedCountLHSA == int(problemInfo.nLHSABeds):
            print("Adding *********** ", x)
            choicesForFuture[x.rstrip()] = y
            totalApplicantsInfo.pop(x.rstrip())
        elif y.isThursRequired == 1 and thursCountLHSA == int(problemInfo.nLHSABeds):
            print("Adding *********** ", x)
            choicesForFuture[x.rstrip()] = y
            totalApplicantsInfo.pop(x.rstrip())
        elif y.isFriRequired == 1 and friCountLHSA == int(problemInfo.nLHSABeds):
            print("Adding *********** ", x)
            choicesForFuture[x.rstrip()] = y
            totalApplicantsInfo.pop(x.rstrip())
        elif y.isSatRequired == 1 and satCountLHSA == int(problemInfo.nLHSABeds):
            print("Adding *********** ", x)
            choicesForFuture[x.rstrip()] = y
            totalApplicantsInfo.pop(x.rstrip())
        elif y.isSunRequired == 1 and sunCountLHSA == int(problemInfo.nLHSABeds):
            print("Adding *********** ", x)
            choicesForFuture[x.rstrip()] = y
            totalApplicantsInfo.pop(x.rstrip())


    # TO BE DELETED
    print ("Number of applicants in total ************ ", len( totalApplicantsInfo))
    for x in totalApplicantsInfo:
        print x
    print ("Number of applicants in Choice Future ***********", len(choicesForFuture))
    for x in choicesForFuture:
        print x

    maxStay = 0
    if len(totalApplicantsInfo) != 0:
       for x, y in totalApplicantsInfo.items():
           if y.DaysRequired > maxStay:
               maxStay = y.DaysRequired
               nextApplicantToBeSelected = x
           elif y.DaysRequired == maxStay and int(nextApplicantToBeSelected) > int(x):
               nextApplicantToBeSelected = x
       print ("Best Pick ************** " , nextApplicantToBeSelected)
       print ("Max number of days required for stay *********** " , maxStay)
    elif len(choicesForFuture) != 0:
        for x, y in choicesForFuture.items():
            if y.DaysRequired > maxStay:
               maxStay = y.DaysRequired
               nextApplicantToBeSelected = x
            elif y.DaysRequired == maxStay and int(nextApplicantToBeSelected) > int(x):
               nextApplicantToBeSelected = x
        print ("Best Pick ************ " , nextApplicantToBeSelected)
        print ("Max number of days required for stay ************ " , maxStay)
    return nextApplicantToBeSelected


input = "input"
ouput = "output"
textfile = ".txt"
inputfilename = " "
outputfilename = " "
if os.path.exists("output.txt"): os.remove("output.txt")
for i in range(0,24):
    inputfilename = input + str(i) + textfile
    GetProblemInfo(inputfilename)
    ParseApplicantInfo()

    h = open("output.txt", "a")
    h.write( PrintNextApplicantToBePintedBySPLA() + "\n")

"""input = "input"
ouput = "output"
textfile = ".txt"
inputfilename = " "
outputfilename = " "
for i in range(0,24):
    inputfilename = input + str(i) + textfile
    outputfilename = ouput + str(i) + textfile
    if os.path.exists("output.txt"): os.remove("output.txt")
    GetProblemInfo(inputfilename)
    ParseApplicantInfo()

    h = open("output.txt", "a")
    h.write( PrintNextApplicantToBePintedBySPLA() + "\n")"""

"""if os.path.exists("output0.txt"): os.remove("output0.txt")
if os.path.exists("input.txt"):
    GetProblemInfo("input.txt")
    ParseApplicantInfo()
    h = open("output.txt", "a")
    h.write( PrintNextApplicantToBePintedBySPLA() + "\n")"""
