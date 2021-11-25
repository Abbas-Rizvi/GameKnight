from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import AuthGroupSerializer, AuthGroupPermissionsSerializer, AuthPermissionSerializer, AuthUserSerializer, AuthUserGroupsSerializer, AuthUserUserPermissionsSerializer, DevelopersSerializer, DjangoAdminLogSerializer, DjangoContentTypeSerializer, DjangoMigrationsSerializer, DjangoSessionSerializer, GameSerializer, GenreSerializer, GenreAssociatedSerializer, HasTagsSerializer, PlatformSerializer, PlayedOnSerializer
from api.models import AuthGroup, AuthGroupPermissions, AuthPermission, AuthUser, AuthUserGroups, AuthUserUserPermissions, Developers, DjangoAdminLog, DjangoContentType, DjangoMigrations, DjangoSession, Game, Genre, GenreAssociated, HasTags, Platform, PlayedOn


class AuthGroupAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = AuthGroup.objects.get(pk=id)
            serializer = AuthGroupSerializer(item)
            return Response(serializer.data)
        except AuthGroup.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = AuthGroup.objects.get(pk=id)
        except AuthGroup.DoesNotExist:
            return Response(status=404)
        serializer = AuthGroupSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = AuthGroup.objects.get(pk=id)
        except AuthGroup.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AuthGroupAPIListView(APIView):

    def get(self, request, format=None):
        items = AuthGroup.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = AuthGroupSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AuthGroupPermissionsAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = AuthGroupPermissions.objects.get(pk=id)
            serializer = AuthGroupPermissionsSerializer(item)
            return Response(serializer.data)
        except AuthGroupPermissions.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = AuthGroupPermissions.objects.get(pk=id)
        except AuthGroupPermissions.DoesNotExist:
            return Response(status=404)
        serializer = AuthGroupPermissionsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = AuthGroupPermissions.objects.get(pk=id)
        except AuthGroupPermissions.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AuthGroupPermissionsAPIListView(APIView):

    def get(self, request, format=None):
        items = AuthGroupPermissions.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = AuthGroupPermissionsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthGroupPermissionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AuthPermissionAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = AuthPermission.objects.get(pk=id)
            serializer = AuthPermissionSerializer(item)
            return Response(serializer.data)
        except AuthPermission.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = AuthPermission.objects.get(pk=id)
        except AuthPermission.DoesNotExist:
            return Response(status=404)
        serializer = AuthPermissionSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = AuthPermission.objects.get(pk=id)
        except AuthPermission.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AuthPermissionAPIListView(APIView):

    def get(self, request, format=None):
        items = AuthPermission.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = AuthPermissionSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthPermissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AuthUserAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = AuthUser.objects.get(pk=id)
            serializer = AuthUserSerializer(item)
            return Response(serializer.data)
        except AuthUser.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = AuthUser.objects.get(pk=id)
        except AuthUser.DoesNotExist:
            return Response(status=404)
        serializer = AuthUserSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = AuthUser.objects.get(pk=id)
        except AuthUser.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AuthUserAPIListView(APIView):

    def get(self, request, format=None):
        items = AuthUser.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = AuthUserSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class AuthGroupAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = AuthGroup.objects.get(pk=id)
            serializer = AuthGroupSerializer(item)
            return Response(serializer.data)
        except AuthGroup.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = AuthGroup.objects.get(pk=id)
        except AuthGroup.DoesNotExist:
            return Response(status=404)
        serializer = AuthGroupSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = AuthGroup.objects.get(pk=id)
        except AuthGroup.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AuthGroupAPIListView(APIView):

    def get(self, request, format=None):
        items = AuthGroup.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = AuthGroupSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AuthGroupPermissionsAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = AuthGroupPermissions.objects.get(pk=id)
            serializer = AuthGroupPermissionsSerializer(item)
            return Response(serializer.data)
        except AuthGroupPermissions.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = AuthGroupPermissions.objects.get(pk=id)
        except AuthGroupPermissions.DoesNotExist:
            return Response(status=404)
        serializer = AuthGroupPermissionsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = AuthGroupPermissions.objects.get(pk=id)
        except AuthGroupPermissions.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AuthGroupPermissionsAPIListView(APIView):

    def get(self, request, format=None):
        items = AuthGroupPermissions.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = AuthGroupPermissionsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthGroupPermissionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AuthPermissionAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = AuthPermission.objects.get(pk=id)
            serializer = AuthPermissionSerializer(item)
            return Response(serializer.data)
        except AuthPermission.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = AuthPermission.objects.get(pk=id)
        except AuthPermission.DoesNotExist:
            return Response(status=404)
        serializer = AuthPermissionSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = AuthPermission.objects.get(pk=id)
        except AuthPermission.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AuthPermissionAPIListView(APIView):

    def get(self, request, format=None):
        items = AuthPermission.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = AuthPermissionSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthPermissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AuthUserAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = AuthUser.objects.get(pk=id)
            serializer = AuthUserSerializer(item)
            return Response(serializer.data)
        except AuthUser.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = AuthUser.objects.get(pk=id)
        except AuthUser.DoesNotExist:
            return Response(status=404)
        serializer = AuthUserSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = AuthUser.objects.get(pk=id)
        except AuthUser.DoesNotExist:
            return Response(status=404)
    def post(self, request, format=None):
        serializer = AuthUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AuthUserGroupsAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = AuthUserGroups.objects.get(pk=id)
            serializer = AuthUserGroupsSerializer(item)
            return Response(serializer.data)
        except AuthUserGroups.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = AuthUserGroups.objects.get(pk=id)
        except AuthUserGroups.DoesNotExist:
            return Response(status=404)
        serializer = AuthUserGroupsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = AuthUserGroups.objects.get(pk=id)
        except AuthUserGroups.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AuthUserGroupsAPIListView(APIView):

    def get(self, request, format=None):
        items = AuthUserGroups.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = AuthUserGroupsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthUserGroupsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AuthUserUserPermissionsAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = AuthUserUserPermissions.objects.get(pk=id)
            serializer = AuthUserUserPermissionsSerializer(item)
            return Response(serializer.data)
        except AuthUserUserPermissions.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = AuthUserUserPermissions.objects.get(pk=id)
        except AuthUserUserPermissions.DoesNotExist:
            return Response(status=404)
        serializer = AuthUserUserPermissionsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = AuthUserUserPermissions.objects.get(pk=id)
        except AuthUserUserPermissions.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AuthUserUserPermissionsAPIListView(APIView):

    def get(self, request, format=None):
        items = AuthUserUserPermissions.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = AuthUserUserPermissionsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthUserUserPermissionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class DevelopersAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Developers.objects.get(pk=id)
            serializer = DevelopersSerializer(item)
            return Response(serializer.data)
        except Developers.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Developers.objects.get(pk=id)
        except Developers.DoesNotExist:
            return Response(status=404)
        serializer = DevelopersSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Developers.objects.get(pk=id)
        except Developers.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class DevelopersAPIListView(APIView):

    def get(self, request, format=None):
        items = Developers.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = DevelopersSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = DevelopersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class DjangoAdminLogAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = DjangoAdminLog.objects.get(pk=id)
            serializer = DjangoAdminLogSerializer(item)
            return Response(serializer.data)
        except DjangoAdminLog.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = DjangoAdminLog.objects.get(pk=id)
        except DjangoAdminLog.DoesNotExist:
            return Response(status=404)
        serializer = DjangoAdminLogSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = DjangoAdminLog.objects.get(pk=id)
        except DjangoAdminLog.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class DjangoAdminLogAPIListView(APIView):

    def get(self, request, format=None):
        items = DjangoAdminLog.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = DjangoAdminLogSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = DjangoAdminLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class DjangoContentTypeAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = DjangoContentType.objects.get(pk=id)
            serializer = DjangoContentTypeSerializer(item)
            return Response(serializer.data)
        except DjangoContentType.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = DjangoContentType.objects.get(pk=id)
        except DjangoContentType.DoesNotExist:
            return Response(status=404)
        serializer = DjangoContentTypeSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = DjangoContentType.objects.get(pk=id)
        except DjangoContentType.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class DjangoContentTypeAPIListView(APIView):

    def get(self, request, format=None):
        items = DjangoContentType.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = DjangoContentTypeSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = DjangoContentTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class DjangoMigrationsAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = DjangoMigrations.objects.get(pk=id)
            serializer = DjangoMigrationsSerializer(item)
            return Response(serializer.data)
        except DjangoMigrations.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = DjangoMigrations.objects.get(pk=id)
        except DjangoMigrations.DoesNotExist:
            return Response(status=404)
        serializer = DjangoMigrationsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = DjangoMigrations.objects.get(pk=id)
        except DjangoMigrations.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class DjangoMigrationsAPIListView(APIView):

    def get(self, request, format=None):
        items = DjangoMigrations.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = DjangoMigrationsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = DjangoMigrationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class DjangoSessionAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = DjangoSession.objects.get(pk=id)
            serializer = DjangoSessionSerializer(item)
            return Response(serializer.data)
        except DjangoSession.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = DjangoSession.objects.get(pk=id)
        except DjangoSession.DoesNotExist:
            return Response(status=404)
        serializer = DjangoSessionSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = DjangoSession.objects.get(pk=id)
        except DjangoSession.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class DjangoSessionAPIListView(APIView):

    def get(self, request, format=None):
        items = DjangoSession.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = DjangoSessionSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = DjangoSessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class GameAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Game.objects.get(pk=id)
            serializer = GameSerializer(item)
            return Response(serializer.data)
        except Game.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Game.objects.get(pk=id)
        except Game.DoesNotExist:
            return Response(status=404)
        serializer = GameSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Game.objects.get(pk=id)
        except Game.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class GameAPIListView(APIView):

    def get(self, request, format=None):
        items = Game.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = GameSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class GenreAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Genre.objects.get(pk=id)
            serializer = GenreSerializer(item)
            return Response(serializer.data)
        except Genre.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Genre.objects.get(pk=id)
        except Genre.DoesNotExist:
            return Response(status=404)
        serializer = GenreSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Genre.objects.get(pk=id)
        except Genre.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class GenreAPIListView(APIView):

    def get(self, request, format=None):
        items = Genre.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = GenreSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class GenreAssociatedAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = GenreAssociated.objects.get(pk=id)
            serializer = GenreAssociatedSerializer(item)
            return Response(serializer.data)
        except GenreAssociated.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = GenreAssociated.objects.get(pk=id)
        except GenreAssociated.DoesNotExist:
            return Response(status=404)
        serializer = GenreAssociatedSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = GenreAssociated.objects.get(pk=id)
        except GenreAssociated.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class GenreAssociatedAPIListView(APIView):

    def get(self, request, format=None):
        items = GenreAssociated.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = GenreAssociatedSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = GenreAssociatedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class HasTagsAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = HasTags.objects.get(pk=id)
            serializer = HasTagsSerializer(item)
            return Response(serializer.data)
        except HasTags.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = HasTags.objects.get(pk=id)
        except HasTags.DoesNotExist:
            return Response(status=404)
        serializer = HasTagsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = HasTags.objects.get(pk=id)
        except HasTags.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class HasTagsAPIListView(APIView):

    def get(self, request, format=None):
        items = HasTags.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = HasTagsSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = HasTagsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PlatformAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Platform.objects.get(pk=id)
            serializer = PlatformSerializer(item)
            return Response(serializer.data)
        except Platform.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Platform.objects.get(pk=id)
        except Platform.DoesNotExist:
            return Response(status=404)
        serializer = PlatformSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Platform.objects.get(pk=id)
        except Platform.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class PlatformAPIListView(APIView):

    def get(self, request, format=None):
        items = Platform.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = PlatformSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = PlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PlayedOnAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = PlayedOn.objects.get(pk=id)
            serializer = PlayedOnSerializer(item)
            return Response(serializer.data)
        except PlayedOn.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = PlayedOn.objects.get(pk=id)
        except PlayedOn.DoesNotExist:
            return Response(status=404)
        serializer = PlayedOnSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = PlayedOn.objects.get(pk=id)
        except PlayedOn.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class PlayedOnAPIListView(APIView):

    def get(self, request, format=None):
        items = PlayedOn.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = PlayedOnSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = PlayedOnSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
