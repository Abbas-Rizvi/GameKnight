from django.conf.urls import include, url
from api import views


urlpatterns = [

  url(r'^authgroup/(?P<id>[0-9]+)/$', views.AuthGroupAPIView.as_view()),
  url(r'^authgroup/$', views.AuthGroupAPIListView.as_view()),

  url(r'^authgrouppermissions/(?P<id>[0-9]+)/$', views.AuthGroupPermissionsAPIView.as_view()),
  url(r'^authgrouppermissions/$', views.AuthGroupPermissionsAPIListView.as_view()),

  url(r'^authpermission/(?P<id>[0-9]+)/$', views.AuthPermissionAPIView.as_view()),
  url(r'^authpermission/$', views.AuthPermissionAPIListView.as_view()),

  url(r'^authuser/(?P<id>[0-9]+)/$', views.AuthUserAPIView.as_view()),
  url(r'^authuser/$', views.AuthUserAPIListView.as_view()),

  url(r'^authusergroups/(?P<id>[0-9]+)/$', views.AuthUserGroupsAPIView.as_view()),
  url(r'^authusergroups/$', views.AuthUserGroupsAPIListView.as_view()),

  url(r'^authuseruserpermissions/(?P<id>[0-9]+)/$', views.AuthUserUserPermissionsAPIView.as_view()),
  url(r'^authuseruserpermissions/$', views.AuthUserUserPermissionsAPIListView.as_view()),

  url(r'^developers/(?P<id>[0-9]+)/$', views.DevelopersAPIView.as_view()),
  url(r'^developers/$', views.DevelopersAPIListView.as_view()),

  url(r'^djangoadminlog/(?P<id>[0-9]+)/$', views.DjangoAdminLogAPIView.as_view()),
  url(r'^djangoadminlog/$', views.DjangoAdminLogAPIListView.as_view()),

  url(r'^djangocontenttype/(?P<id>[0-9]+)/$', views.DjangoContentTypeAPIView.as_view()),
  url(r'^djangocontenttype/$', views.DjangoContentTypeAPIListView.as_view()),

  url(r'^djangomigrations/(?P<id>[0-9]+)/$', views.DjangoMigrationsAPIView.as_view()),
  url(r'^djangomigrations/$', views.DjangoMigrationsAPIListView.as_view()),

  url(r'^djangosession/(?P<id>[0-9]+)/$', views.DjangoSessionAPIView.as_view()),
  url(r'^djangosession/$', views.DjangoSessionAPIListView.as_view()),

  url(r'^game/(?P<id>[0-9]+)/$', views.GameAPIView.as_view()),
  url(r'^game/$', views.GameAPIListView.as_view()),

  url(r'^genre/(?P<id>[0-9]+)/$', views.GenreAPIView.as_view()),
  url(r'^genre/$', views.GenreAPIListView.as_view()),

  url(r'^genreassociated/(?P<id>[0-9]+)/$', views.GenreAssociatedAPIView.as_view()),
  url(r'^genreassociated/$', views.GenreAssociatedAPIListView.as_view()),

  url(r'^hastags/(?P<id>[0-9]+)/$', views.HasTagsAPIView.as_view()),
  url(r'^hastags/$', views.HasTagsAPIListView.as_view()),

  url(r'^platform/(?P<id>[0-9]+)/$', views.PlatformAPIView.as_view()),
  url(r'^platform/$', views.PlatformAPIListView.as_view()),

  url(r'^playedon/(?P<id>[0-9]+)/$', views.PlayedOnAPIView.as_view()),
  url(r'^playedon/$', views.PlayedOnAPIListView.as_view()),

]
