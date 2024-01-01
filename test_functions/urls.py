from django.urls import path

from . import views

app_name = "test_functions"
urlpatterns = [
    # path("", views.IndexView.as_view(), name="index"),
    path("search_form/", views.search_form, name="search_form"),
    path("search/", views.search, name="search"),
]
