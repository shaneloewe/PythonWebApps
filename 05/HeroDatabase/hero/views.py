from django.shortcuts import render
from pathlib import Path
from django.views.generic import TemplateView
from .models import Hero

# Create your views here.


def hero_list():
    def hero_details(i, f):
        return dict(id=i, file=f, caption="", name="")

    heroes = Hero.objects.all()
    heroes = [hero_details(i, f) for i, f in enumerate(heroes)]
    return heroes


class HomeView(TemplateView):
    template_name = 'heroDetail.html'


class HeroListView(TemplateView):
    template_name = 'databaseHome.html'

    def get_context_data(self, **kwargs):
        return dict(heroes=hero_list())


class HeroDetailView(TemplateView):
    template_name = 'heroDetail.html'

    def get_context_data(self, **kwargs):
        i = kwargs['id']
        heroes = hero_list()
        h = heroes[i-1]
        return dict(hero=h)
