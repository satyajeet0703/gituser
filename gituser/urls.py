from django.conf.urls import include,url
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from usersearch import views
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

router.register(r'searchusers', views.SerachUserViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^usersearch/',views.SerachUserView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
