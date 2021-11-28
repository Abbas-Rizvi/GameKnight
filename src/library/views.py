from django.shortcuts import render
from library.models import Game, GenreAssociated, HasTags,Genre, Platform, PlayedOn, Developers
from django.http import Http404
from django.forms.models import model_to_dict

# individual game pages
# checks game_id for 
def game_details(request,gameID):

    # game
    #----------------------------------------
    try:
        game_obj = Game.objects.select_related('fk_dev').get(game_id=gameID)
    except Game.DoesNotExist:
        raise Http404("Game does not exist in database")

    # find tags
    #----------------------------------------
    tags = HasTags.objects.filter(fk_game=gameID)

    # find genres assosciated
    #----------------------------------------
    genres = Genre.objects.filter(genreassociated__fk_game=gameID)


    # find platforms assosciated
    #----------------------------------------
    platforms = Platform.objects.filter(playedon__fk_game=gameID)


    return render(request, "game_page.html",{
        'game':game_obj,
        'tags':tags,
        'genres':genres,
        'platforms':platforms,
        })

# home page render request
def home(request):
    
    allgames = Game.objects.all()


    return render(request, "home.html", {
        'allgames':allgames
    })