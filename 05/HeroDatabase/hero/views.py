from django.shortcuts import render
from pathlib import Path
from django.views.generic import TemplateView
from .models import Hero

# Create your views here.


def hero_list():
    def hero_details(i, f):
        return dict(id=i, file=f)

    heroes = Hero.objects.all()
    heroes = [hero_details(i, f) for i, f in enumerate(heroes)]
    return heroes


class HeroListView(TemplateView):
    template_name = 'databaseHome.html'

    def get_context_data(self, **kwargs):
        return dict(heroes=hero_list())


class HeroDetailView(TemplateView):
    template_name = 'heroDetail.html'

    def get_context_data(self, **kwargs):
        heroes = hero_list()
        for j in range(len(heroes)):
            if kwargs['id'] == j:
                i = kwargs['id']
            else:
                i = j
        h = heroes[i]
        return dict(hero=h)


class AboutView(TemplateView):
    template_name = 'about.html'


class ClientView(TemplateView):
    template_name = 'clients.html'
