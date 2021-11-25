from rest_framework.serializers import ModelSerializer
from api.models import AuthGroup, AuthGroupPermissions, AuthPermission, AuthUser, AuthUserGroups, AuthUserUserPermissions, Developers, DjangoAdminLog, DjangoContentType, DjangoMigrations, DjangoSession, Game, Genre, GenreAssociated, HasTags, Platform, PlayedOn


class AuthGroupSerializer(ModelSerializer):

    class Meta:
        model = AuthGroup
        depth = 2
        fields = '__all__'


class AuthGroupPermissionsSerializer(ModelSerializer):

    class Meta:
        model = AuthGroupPermissions
        depth = 2
        fields = '__all__'


class AuthPermissionSerializer(ModelSerializer):

    class Meta:
        model = AuthPermission
        depth = 2
        fields = '__all__'


class AuthUserSerializer(ModelSerializer):

    class Meta:
        model = AuthUser
        depth = 2
        fields = '__all__'


class AuthUserGroupsSerializer(ModelSerializer):

    class Meta:
        model = AuthUserGroups
        depth = 2
        fields = '__all__'


class AuthUserUserPermissionsSerializer(ModelSerializer):

    class Meta:
        model = AuthUserUserPermissions
        depth = 2
        fields = '__all__'


class DevelopersSerializer(ModelSerializer):

    class Meta:
        model = Developers
        depth = 2
        fields = '__all__'


class DjangoAdminLogSerializer(ModelSerializer):

    class Meta:
        model = DjangoAdminLog
        depth = 2
        fields = '__all__'


class DjangoContentTypeSerializer(ModelSerializer):

    class Meta:
        model = DjangoContentType
        depth = 2
        fields = '__all__'


class DjangoMigrationsSerializer(ModelSerializer):

    class Meta:
        model = DjangoMigrations
        depth = 2
        fields = '__all__'


class DjangoSessionSerializer(ModelSerializer):

    class Meta:
        model = DjangoSession
        depth = 2
        fields = '__all__'


class GameSerializer(ModelSerializer):

    class Meta:
        model = Game
        depth = 2
        fields = '__all__'


class GenreSerializer(ModelSerializer):

    class Meta:
        model = Genre
        depth = 2
        fields = '__all__'


class GenreAssociatedSerializer(ModelSerializer):

    class Meta:
        model = GenreAssociated
        depth = 2
        fields = '__all__'


class HasTagsSerializer(ModelSerializer):

    class Meta:
        model = HasTags
        depth = 2
        fields = '__all__'


class PlatformSerializer(ModelSerializer):

    class Meta:
        model = Platform
        depth = 2
        fields = '__all__'


class PlayedOnSerializer(ModelSerializer):

    class Meta:
        model = PlayedOn
        depth = 2
        fields = '__all__'
