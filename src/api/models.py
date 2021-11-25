# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Developers(models.Model):
    dev_id = models.AutoField(primary_key=True)
    rawg_dev_id = models.IntegerField()
    dev_name = models.CharField(max_length=45, blank=True, null=True)
    dev_img = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'developers'
        unique_together = (('dev_id', 'rawg_dev_id'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
    rawg_tag_id = models.IntegerField()
    fk_game = models.ForeignKey(Game, models.DO_NOTHING)
    tag = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'has_tags'
        unique_together = (('ht_id', 'rawg_tag_id'),)


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
