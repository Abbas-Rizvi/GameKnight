# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Developers(models.Model):
    dev_id = models.AutoField(primary_key=True)
    rawg_dev_id = models.IntegerField()
    dev_name = models.CharField(max_length=45, blank=True, null=True)
    dev_img = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'developers'
        unique_together = (('dev_id', 'rawg_dev_id'),)


class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    rawg_gameid = models.IntegerField()
    fk_dev = models.ForeignKey(Developers, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    release_date = models.CharField(max_length=45, blank=True, null=True)
    game_img = models.CharField(max_length=2555, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    metacritic_score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game'
        unique_together = (('game_id', 'rawg_gameid'),)


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    rawg_genre_id = models.IntegerField()
    genre_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genre'
        unique_together = (('genre_id', 'rawg_genre_id'),)


class GenreAssociated(models.Model):
    ga_id = models.AutoField(primary_key=True)
    fk_game = models.ForeignKey(Game, models.DO_NOTHING)
    fk_genre = models.ForeignKey(Genre, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'genre_associated'


class HasTags(models.Model):
    ht_id = models.AutoField(primary_key=True)
    fk_game = models.ForeignKey(Game, models.DO_NOTHING)
    rawg_tag_id = models.IntegerField()
    tag = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'has_tags'


class Platform(models.Model):
    plat_id = models.AutoField(primary_key=True)
    rawg_platform_id = models.IntegerField()
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'platform'
        unique_together = (('plat_id', 'rawg_platform_id'),)


class PlayedOn(models.Model):
    played_on_id = models.AutoField(primary_key=True)
    fk_plat = models.ForeignKey(Platform, models.DO_NOTHING)
    fk_game = models.ForeignKey(Game, models.DO_NOTHING)
    release_date = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'played_on'
