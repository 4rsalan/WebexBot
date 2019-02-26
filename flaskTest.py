import requests
import sys
import json
import os
import time
import pymongo
from webexteamssdk import WebexTeamsAPI, Webhook
import quiz
from functions import *

from flask import Flask, request


app = Flask(__name__)

quiz_rooms = {}
key = 'Bearer NWQ3YzQyYmQtYTQ2Yy00MDUxLWI5ZGUtM2M5ZmY3Y2MwNWE4MmU1NDkyZjYtMjE2_PF84_consumer'
bot_key = 'MTY0NWMyYjctMTliNi00ZjBjLWE5MDgtMzU5NWNlMjM5NDZlYTM1NTRkYjMtODYx_PF84_consumer'

def showQuizOptions(message):
    data = "Add Quiz \n" + "View Quizzes"
    url = 'https://api.ciscospark.com/v1/messages'
    requests.post(url, data, headers={'Authorization': key})

    message_details = requests.get(url, headers={'Authorization': key}).json()


def createQuizRoom(user_id):
    # create room

    # get user data
    uder_data_url = 'https://api.ciscospark.com/v1/people/' + user_id
    json_user_data = requests.get(uder_data_url, headers={'Authorization': key}).json()
    user_name = json_user_data["displayName"]

    url_response_message = 'https://api.ciscospark.com/v1/messages'
    data_response_message = {'toPersonId': user_id, 'text': 'Welcome to quiz',
                             'teamId': 'Y2lzY29zcGFyazovL3VzL1RFQU0vZjBiMzA4ODAtMzkyYy0xMWU5LTgzYmMtMDE5MWQ3YmY4ZTNk'}
    room_data = requests.post(url_response_message, data_response_message, headers={'Authorization': key})
    json_user_data = room_data.json()
    roomId = json_user_data['roomId']
    quiz_rooms.update({roomId: quiz.quiz()})
    askquestion(roomId, 'from createQuiz')


def checkAnswer(roomId, message):
    if quiz_rooms[roomId].checkAns(message):
        endQuiz(roomId)
    else:
        askquestion(roomId, 'from checkAns')


def askquestion(roomId, message):
    data_question_message = {'roomId': roomId, 'text': quiz_rooms[roomId].askQuestion()}
    url_question_message = 'https://api.ciscospark.com/v1/messages'
    requests.post(url_question_message, data_question_message, headers={'Authorization': key})


def endQuiz(roomId):
    message = 'Your Score = {} out of 5'.format(quiz_rooms[roomId].numCorrectAns)
    del quiz_rooms[roomId]
    # post quiz results
    data_quiz_results_message = {'roomId': roomId, 'text': message}
    url_quiz_results_message = 'https://api.ciscospark.com/v1/messages'
    requests.post(url_quiz_results_message, data_quiz_results_message, headers={'Authorization': key})


@app.route("/", methods=['POST'])
def webhook():
    myclient = pymongo.MongoClient("mongodb://Admin:TeamTrees11!@ds351455.mlab.com:51455/teamtrees")
    # Get the json data
    json = request.json
    # Retrieving message ID, person ID, email and room ID from message received

    message_id = json["data"]["id"]
    user_id = json["data"]["personId"]
    email = json["data"]["personEmail"]
    room_id = json["data"]["roomId"]
    # message_text = json["data"]["text"]
    # print("webhook: " + str(json["data"]['personId']))

    url = 'https://api.ciscospark.com/v1/messages/' + format(message_id)
    message_details = requests.get(url, headers={'Authorization': key}).json()

    if message_details["text"][0:8] == "quiztime":
        createQuizRoom(user_id)

    elif message_details["roomId"] in quiz_rooms and user_id != 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS84MjU0YjA0MS05YzJmLTQ2ZjMtOGFmMC02ZTU4MjhhMjAwMTU':
        checkAnswer(message_details["roomId"], message_details["text"])

    if message_details["text"] == "Menu" or message_details["text"] == "menu":
        data = {'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vZjBiMzA4ODAtMzkyYy0xMWU5LTgzYmMtMDE5MWQ3YmY4ZTNk', 'text': showMenu()}
        url = 'https://api.ciscospark.com/v1/messages'
        requests.post(url, data, headers={'Authorization': key})

    if message_details["text"] == "Resources" or message_details["text"] == "Resources":
        data = {'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vZjBiMzA4ODAtMzkyYy0xMWU5LTgzYmMtMDE5MWQ3YmY4ZTNk', 'text': showResources(myclient)}
        url = 'https://api.ciscospark.com/v1/messages'
        requests.post(url, data, headers={'Authorization': key})

    if message_details["text"] == "Quizzes" or message_details["text"] == "quizzes":
        showQuizOptions(message_details["text"])

    return "Success!"


app.run(host='localhost', port=88)

#myclient["teamtrees"]["quizes"].insert_one({"id":2,"mark":3})


