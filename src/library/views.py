from django.shortcuts import render
from library.models import Game, GenreAssociated, HasTags
from django.http import Http404
from django.forms.models import model_to_dict

# individual game pages
# checks game_id for 
def game_details(request,gameID):

    try:
        game_obj = Game.objects.get(game_id=gameID)
    except Game.DoesNotExist:
        raise Http404("Game does not exist in database")
    params = dict(model_to_dict(game_obj))


    try:
        tags = HasTags.objects.filter(fk_game=gameID)
        # tag_dict = dict(model_to_dict(tags))
    except Game.DoesNotExist:
        pass


    return render(request, "game_page.html",{
        'game':params,
        'tags':tags
        })

# home page render request
def home(request):
    return render(request, "home.html", {})