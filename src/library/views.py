from django.shortcuts import render
from library.models import Game, GenreAssociated, HasTags,Genre, Platform, PlayedOn
from django.http import Http404
from django.forms.models import model_to_dict

# individual game pages
# checks game_id for 
def game_details(request,gameID):

    # game
    #####################################
    try:
        game_obj = Game.objects.get(game_id=gameID)
    except Game.DoesNotExist:
        raise Http404("Game does not exist in database")
    params = dict(model_to_dict(game_obj))

    # find tags
    #####################################
    try:
        tags = HasTags.objects.filter(fk_game=gameID)
        # tag_dict = dict(model_to_dict(tags))
    except Game.DoesNotExist:
        pass

    # find genres assosciated
    #####################################
    try:
        genre_ass_obj = GenreAssociated.objects.filter(fk_game=gameID)
    except GenreAssociated.DoesNotExist:
        pass

    genres = {}

    try:
        counter = 1
        for item in genre_ass_obj:
            counter +=1

            genre_id = model_to_dict(item)['fk_genre']
            genre_item = Genre.objects.get(genre_id=genre_id)
            item = str(model_to_dict(genre_item)['genre_name'])
            genres[counter] = item
    except:
        pass

    # find platforms assosciated
    #####################################
    try:
        plat_ass = PlayedOn.objects.filter(fk_game=gameID)
    except PlayedOn.DoesNotExist:
        pass

    platforms = {}

    try:
        counter = 1
        for item in plat_ass:
            counter +=1

            plat_id = model_to_dict(item)['fk_plat']
            plat_item = Platform.objects.get(plat_id=plat_id)
            item = str(model_to_dict(plat_item)['name'])
            platforms[counter] = item
    except:
        pass


    return render(request, "game_page.html",{
        'game':params,
        'tags':tags,
        'genres':genres,
        'platforms':platforms
        })

# home page render request
def home(request):
    return render(request, "home.html", {})