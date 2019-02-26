import pymongo
import requests
myclient = pymongo.MongoClient("mongodb://Admin:TeamTrees11!@ds351455.mlab.com:51455/teamtrees")


# Function which returns bot menu as a string to be displayed on command line
def showMenu():
    s = "Bot Menu \n" + "Resources \n" + "Quizzes \n" + "Survey \n" + "Email \n" + "Help"
    return s

# Function which returns a string containing a list of all the resources available to the student
def showResources(mongoValue):
    # Functions that displays a list of resources available submitted by the admin. Reads from database later
    #resources = {'Resource1': 'https://github.com/4rsalan/WebexBot/blob/master/flaskTest.py','Resource2': 'https://github.com/4rsalan/WebexBot/blob/master/flaskTest.py'}
    resources =  []
    for resource in mongoValue['teamtrees']['resources'].find():
        resources.append(resource)

    return str(resources[0]["Hello"])


def addResource(mongoValue, resource_name, resource_value):
    mongoValue["teamtrees"]["resources"].insert_one({resource_name: resource_value})



def showHelp():
    s = ""
    return s

#addResource(myclient, "Hello", "My name is arsalan")

print(showResources(myclient))