from rest_framework import serializers
from library.models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['gameid', 'name', 'releasedate', 'price', 'platformid', 'developerid', 'gname']


