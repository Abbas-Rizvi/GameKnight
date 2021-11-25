from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from savegame.models import Developers,Game, Genre, GenreAssociated, HasTags, Platform, PlayedOn
import requests
from decouple import config

# Save external rawg game api data into models
def rawg(request,gameID):
    json_response = requests.get(('https://api.rawg.io/api/games/' + str(gameID)),params={'key':config('RAWG_KEY')}).json()
    
    #debugging print statements
    print('###############################')

    # Developer
    # --------------------------------------------
    developers = json_response['developers']

    dev_id=developers[0]['id']
    dev_name=developers[0]['name']
    dev_img=developers[0]['image_background']

    # Object Creation
    dev_obj, created = Developers.objects.get_or_create(rawg_dev_id=dev_id, defaults={
        'dev_name':dev_name,
        'dev_img':dev_img
    })

    if created:
        dev_obj.save()
    else:
        print("developer object already exists")

    # Game
    # --------------------------------------------

    # Attributes
    id= json_response['id']
    name = json_response['name']
    releasedate = json_response['released']
    img=json_response['background_image']
    description = json_response['description_raw']
    rating = json_response['metacritic']

    # Object Creation
    game_obj, created = Game.objects.update_or_create(rawg_gameid=id, defaults={
        'fk_dev':dev_obj,
        'name':name,
        'release_date':releasedate,
        'game_img':img,
        'description':description,
        'metacritic_score':rating
        })

    if created:
        game_obj.save()
    else:
        print("game object already exists")


    # Genre
    # ----------------------
    # Creats as many genres as listed in api, saves to database

    genres = json_response['genres']

    for i in range(len(genres)):
        gen_rawg_id= genres[i]['id']
        gen_name=genres[i]['name']

        # Object Creation
        gen_obj, created = Genre.objects.update_or_create(rawg_genre_id=gen_rawg_id,defaults={
            'genre_name':gen_name
        })

        if created:
            gen_obj.save()
        else:
            print("genre object already exists")   

        #genre associated
        ###################

        gen_obj = Genre.objects.get(rawg_genre_id=gen_rawg_id)
        gen_ass_obj, created = GenreAssociated.objects.update_or_create(fk_game=game_obj,fk_genre=gen_obj)
        
        if created:
            gen_ass_obj.save()
        else:
            print("genre_associated object already exists")  

    # Tags
    # ------------------------------------
    tags = json_response['tags']

    for i in range(len(tags)):
        rawg_tag_id = tags[i]['id']
        tag_name= tags[i]['name']

        #object creation
        ht_obj, created = HasTags.objects.update_or_create(rawg_tag_id=rawg_tag_id, defaults={
            'fk_game':game_obj,
            'tag':tag_name
        })

        if created:
            ht_obj.save()
        else:
            print("has_tags object already exists")  

    # Platform 
    # --------------------------------------------
    platforms = json_response['platforms']

    for i in range(len(platforms)):
        plat_id= platforms[i]['platform']['id']
        plat_name=platforms[i]['platform']['name']
        plat_release=platforms[i]['released_at']

        # Object Creation
        plat_obj, created = Platform.objects.update_or_create(rawg_platform_id=plat_id,defaults={
            'name':plat_name,
        })

        if created:
            plat_obj.save()
        else:
            print("platform object already exists")  


        #played on
        #####################
        plat_obj = Platform.objects.get(rawg_platform_id=plat_id)

        played_on_obj ,created = PlayedOn.objects.update_or_create(fk_plat=plat_obj,fk_game=game_obj,defaults={
            'release_date':plat_release
        })

        if created:
            played_on_obj.save()
        else:
            print("played_on object already exists")  


    return JsonResponse({'log':'Item Saved Successfully'})
    return HttpResponse("You're looking at question %s." % name)
