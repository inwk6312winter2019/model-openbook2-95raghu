myfile = open("Street_Centrelines.csv","r")

"""A tuple of (STR_NAME,FULL_NAME,FROM_STR,TO_STR)"""
def dotuple():
    for f in myfile:
        f = f.split(",")
        string = (f[2],f[4],f[6],f[7])
        print(string)  

"""A histogram of the different types of maintenance."""

def maintanancehistogram():
    mydict = dict()
    for f in myfile:
        f = f.split(",")
        if f[12] not in mydict:
            mydict[f[12]] = 1
        else:
            mydict[f[12]] += 1
    print(mydict)

"""List of unique owners for the streets. """

def listowners():
    owners = []
    for f in myfile:
        f = f.split(",")
        if f[11] not in owners:
            owners.append(f[11])
    print(owners)

"""Different types of Street classes ["ST_CLASS"] and a list of streets undereach class"""

def getstreetclass():
    stclass = []
    myfile = open("Street_Centrelines.csv","r")
    for f in myfile:
        f = f.split(",")
        f = f[10].strip()
        f = f.replace(" ","")
        if f not in stclass:
            if len(f) >= 1:
                stclass.append(f)
    return stclass


def streeclassnstreets():
    stclass = getstreetclass()
    myfile = open("Street_Centrelines.csv","r")
    print(stclass)
    my_file = open("Street_Centrelines.csv","r")
    for st in stclass:
        print(".",st)
        for fm in my_file:
            fm = fm.split(",")
            fcm = fm[10].strip()
            fcm = fcm.lower()
            fcm = fcm.replace(" ","")
            print(fm[12])


dotuple()
maintanancehistogram()
listowners()
streeclassnstreets()


