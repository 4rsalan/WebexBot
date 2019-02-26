import requests
import pymongo
import quiz
from flask import Flask, request

app = Flask(__name__)

quiz_rooms = {}
key = 'Bearer MzJhMmE2MDMtOWQ2MS00YTM4LWE1M2EtZWI1YTEzOTgxM2Y5ZDlmMDhjMmYtNzNj_PF84_consumer'
#bot_key = 'Bearer NWQ3YzQyYmQtYTQ2Yy00MDUxLWI5ZGUtM2M5ZmY3Y2MwNWE4MmU1NDkyZjYtMjE2_PF84_consumer'
bot_key = 'Bearer NWQ3YzQyYmQtYTQ2Yy00MDUxLWI5ZGUtM2M5ZmY3Y2MwNWE4MmU1NDkyZjYtMjE2_PF84_consumer'

room_id = 'roomId=Y2lzY29zcGFyazovL3VzL1JPT00vZjBiMzA4ODAtMzkyYy0xMWU5LTgzYmMtMDE5MWQ3YmY4ZTNk'

def createQuizRoom(user_id):
    #create room
    '''
    # get user data
    url_user_data = 'https://api.ciscospark.com/v1/people/?mentionedPeople=me&userId='+user_id
    json_user_data = requests.get(url_user_data, headers = {'Authorization': bot_key}).json()
    #user_name = json_user_data["displayName"]
    '''

    url_response_message = 'https://api.ciscospark.com/v1/messages'
    data_response_message = {'toPersonId': user_id, 'text': 'Welcome to quiz', 'teamId' : 'Y2lzY29zcGFyazovL3VzL1RFQU0vZjBiMzA4ODAtMzkyYy0xMWU5LTgzYmMtMDE5MWQ3YmY4ZTNk'}
    room_data = requests.post(url_response_message, data_response_message, headers={'Authorization': bot_key})

    url_get_message = 'https://api.ciscospark.com/v1/messages/direct?mentionedPeople=me&personId=' + user_id + '&' + room_id
    message_data = requests.get(url_get_message, headers = {'Authorization': bot_key}).json()

    print ("message  data: " + str(message_data))

    roomId = message_data['items'][0]['roomId']
    quiz_rooms.update({roomId:quiz.quiz()})
    askquestion(roomId, 'from createQuiz')

def checkAnswer(roomId, message):
    if quiz_rooms[roomId].checkAns(message):
        endQuiz(roomId)
    else:
        askquestion(roomId, 'from checkAns')


def askquestion(roomId, message):
    data_question_message = {'roomId': roomId,'text': quiz_rooms[roomId].askQuestion()}
    url_question_message = 'https://api.ciscospark.com/v1/messages'
    requests.post(url_question_message, data_question_message, headers={'Authorization': bot_key})



def endQuiz(roomId):
    message = 'Your Score = {} out of 5'.format(quiz_rooms[roomId].numCorrectAns)
    del quiz_rooms[roomId]
    #post quiz results
    data_quiz_results_message = {'roomId': roomId,'text': message}
    url_quiz_results_message = 'https://api.ciscospark.com/v1/messages'
    requests.post(url_quiz_results_message, data_quiz_results_message, headers={'Authorization': bot_key})


@app.route("/",methods=['POST'])
def webhook():
    myclient = pymongo.MongoClient("mongodb://Admin:TeamTrees11!@ds351455.mlab.com:51455/teamtrees")
    # Get the json data
    json = request.json
    # Retrieving message ID, person ID, email and room ID from message received

    message_id = "messageId=" + json["data"]["id"]
    user_id = json["data"]["personId"]
    email = json["data"]["personEmail"]
    #room_id = json["data"]["roomId"]
    #message_text = json["data"]["text"]
    #print("webhook: " + str(json["data"]['personId']))
    url = 'https://api.ciscospark.com/v1/messages?mentionedPeople=me&' + message_id + "&" + room_id
    message_details = requests.get(url, headers={'Authorization': bot_key}).json()
    print('message details' + str(message_details))
    '''
    #for debugging
    if message_details["text"][0:6] == "repeat":
        data = {'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vZjBiMzA4ODAtMzkyYy0xMWU5LTgzYmMtMDE5MWQ3YmY4ZTNk', 'text': "You Said "+ message_details["text"][6:]}
        url = 'https://api.ciscospark.com/v1/messages'
        requests.post(url, data, headers={'Authorization': key})
    '''
    message_text = message_details ['items'][0]['text']

    if "quiztime" in message_text:
        print ('creating quiz for user id ' + user_id)
        createQuizRoom(user_id)
        return "Success!"
        
    elif message_details["roomId"] in quiz_rooms and user_id != 'Y2lzY29zcGFyazovL3VzL0FQUExJQ0FUSU9OL2RjOTUzYWY2LTMyOGItNDg3Mi1hM2M0LTZjODFlYjBjOTBkMQ':
        checkAnswer(message_details["items"][0]["roomId"],message_details["items"][0]["text"])

    return "Success!"


app.run(host='localhost', port=88)

#myclient["teamtrees"]["quizes"].insert_one({"id":2,"mark":3})




