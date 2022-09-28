from hero.views import HeroListView, HeroDetailView, AboutView, ClientView
from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path


urlpatterns = [
    # Home
    path('', RedirectView.as_view(url='hero/')),
    path('hero/', HeroListView.as_view()),

    # Detail View
    path('hero/<int:id>', HeroDetailView.as_view()),

    # Admin Page
    path('admin/', admin.site.urls),

    # About Page
    path('hero/about.html', AboutView.as_view()),

    # Client Page
    path('hero/clients.html', ClientView.as_view())
]
