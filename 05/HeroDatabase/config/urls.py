from hero.views import HomeView, HeroListView, HeroDetailView
from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path


urlpatterns = [
    # Home
    path('', RedirectView.as_view(url='hero/')),

    # Photos
    path('hero/', HeroListView.as_view()),
    path('hero/', HomeView.as_view()),
    path('hero/<int:id>', HeroDetailView.as_view()),
    path('admin/', admin.site.urls),
]
