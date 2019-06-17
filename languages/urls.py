from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('languages', views.LanguageView)
router.register('programmers', views.ProgrammerView)


urlpatterns = [
    path('', include(router.urls))
]p