from django.urls import path, include
from .views import HeroCreateView, HeroDeleteView, HeroDetailView, HeroListView, HeroUpdateView, SignUpView, HomeView
from .views import ArticleCreateView, ArticleDeleteView, ArticleDetailView, ArticleListView, ArticleUpdateView, MyArticlesView
from .views import MyHeroesView
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [

    # Home
    path('',                HomeView.as_view(),    name='home_list'),

    # Hero
    path('hero/',            HeroListView.as_view(),    name='hero_list'),
    path('hero/<int:pk>',        HeroDetailView.as_view(),  name='hero_detail'),
    path('hero/add',             HeroCreateView.as_view(),  name='hero_add'),
    path('hero/<int:pk>/',       HeroUpdateView.as_view(),  name='hero_edit'),
    path('hero/<int:pk>/delete', HeroDeleteView.as_view(),  name='hero_delete'),

    # Article
    path('article/',                ArticleListView.as_view(),    name='article_list'),
    path('article/<int:pk>',        ArticleDetailView.as_view(),
         name='article_detail'),
    path('article/add',             ArticleCreateView.as_view(),  name='article_add'),
    path('article/<int:pk>/',
         ArticleUpdateView.as_view(),  name='article_edit'),
    path('article/<int:pk>/delete',
         ArticleDeleteView.as_view(),  name='article_delete'),

    # Navbar code
    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/signup/", SignUpView.as_view(), name="signup"),
    path("accounts/your-heroes", MyHeroesView.as_view(), name="my_heroes"),
    path("accounts/your-articles", MyArticlesView.as_view(), name="my_articles"),
    path('accounts/profile/', RedirectView.as_view(url='../..')),

    # Admin views for users
    path('admin/', admin.site.urls),
    # path('admin/', include('admin.site.urls')),   Don't do this!

]
