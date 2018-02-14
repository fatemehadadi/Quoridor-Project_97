from django.db import models


# Create your models here.
class PlayersRooms(models.Model):
    room = models.CharField(max_length=100)

    def __str__(self):
        return self.room


class Boardgames(models.Model):
    room = models.CharField(max_length=100)

    action = models.CharField(max_length=100)

    players = models.CharField(max_length=100)

    board = models.CharField(max_length=800)

    status = models.CharField(max_length=800)

    def __repr__(self):
        return json.JSONEncoder().encode({
            'room': self.room,
            'action': self.action,
            'player': self.players,
            'board': self.board,
            'status': self.status,
        })

