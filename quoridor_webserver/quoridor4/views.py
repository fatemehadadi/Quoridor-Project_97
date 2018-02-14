from django.shortcuts import render
from signup.models import Users
from quoridor2.models import Boardgames, PlayersRooms
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
import json


def set_play(request):
    # unpacking
    dic = json.load(request.POST.dict())

    actions = ["start_game", "wait", "update", "get_move"]
    if dic["action"] in actions:

        if dic["action"] == "start_game":
            pass
        if dic["wait"] == "wait":
            pass
        if dic["update"] == "update":
            pass
        if dic["get_move"] == "":
            pass
        if dic["action"] == "start_game":
            pass
    else:
        return HttpResponseBadRequest("Enter Valid Data")

        # models of users want to play quoridor

        # set them


def quoridor2(user1, user2):
    board = None
    walls = None
    massage = {"text": "you are in game", "board": board, "walls": walls}
    send_data(None)


def send_data(data):
    respon = json.JSONEncoder.encode(data)
    return HttpResponse(respon)

# Create your views here.
