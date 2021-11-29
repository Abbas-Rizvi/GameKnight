from django.shortcuts import render
from library.models import Game, GenreAssociated, HasTags,Genre, Platform, PlayedOn, Developers
from django.http import Http404
from django.forms.models import model_to_dict
from django.db.models import Q
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
    genre = request.GET.get('genre')
    platform = request.GET.get('platform')
    developer = request.GET.get('developer')
    search = request.GET.get('search')

    
    if search == None or "":
        allgames = Game.objects.all()
    else:
        allgames = Game.objects.all().filter(Q(name__icontains=search))

    if genre == None or genre == "0":
        pass
    else:
        allgames = allgames.filter(genreassociated__fk_genre=genre)


    if platform == None or platform == "0":
        pass
    else:
        allgames = allgames.filter(playedon__fk_plat=platform)

    print(platform)


    genres = Genre.objects.all()
    platforms = Platform.objects.all()
   

    return render(request, "home.html", {
        'allgames':allgames,
        'genres':genres,
        'platforms':platforms
    })