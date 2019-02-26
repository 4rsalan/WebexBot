
# Function which returns bot menu as a string to be displayed on command line
def showMenu():
    s = "Bot Menu \n" + "Resources \n" + "Quizzes \n" + "Survey \n" + "Email \n" + "Help"
    return s

# Function which returns a string containing a list of all the resources available to the student
def showResources():
    # Functions that displays a list of resources available submitted by the admin. Reads from database later
    resources = {'Resource1': 'https://github.com/4rsalan/WebexBot/blob/master/flaskTest.py',
                 'Resource2': 'https://github.com/4rsalan/WebexBot/blob/master/flaskTest.py'}

    return str(resources)
