# pages URL Configuration

from django.urls import path
from .views import RepoList


urlpatterns = [
    path("api/Repos/", RepoList.as_view()),
]
