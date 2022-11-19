from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from django.contrib.messages.views import SuccessMessageMixin

from .models import Superhero, User, Message


class HomeView(ListView):
    template_name = "hero/home.html"
    model = Superhero
    context_object_name = "home"


class HeroListView(ListView):
    template_name = 'hero/list.html'
    model = Superhero
    context_object_name = "heroes"


class HeroDetailView(DetailView):
    template_name = 'hero/detail.html'
    model = Superhero
    context_object_name = "hero"


class HeroCreateView(LoginRequiredMixin, CreateView):
    template_name = "hero/add.html"
    model = Superhero
    fields = ['name', 'identity', 'description',
              'image', 'strengths', 'weaknesses']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class HeroUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "hero/edit.html"
    model = Superhero
    fields = '__all__'

    # This is just a test comment to see if Digital Ocean will reset my database upon a new build


class HeroDeleteView(LoginRequiredMixin, DeleteView):
    model = Superhero
    template_name = 'hero/delete.html'
    success_url = '..'


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class MyHeroesView(LoginRequiredMixin, ListView):
    model = Superhero
    template_name = "registration/my_heroes.html"
    context_object_name = "heroes"
    fields = '__all__'


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = "user_detail.html"

# ARTICLE VIEWS vvvv


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/list.html'
    context_object_name = "articles"


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "articles/add.html"
    model = Article
    fields = ['title', 'date', 'body', 'image']

    def form_valid(self, form):
        form.instance.investigator = self.request.user
        return super().form_valid(form)


class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/detail.html"
    context_object_name = "article"


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'articles/delete.html'
    success_url = '..'


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "articles/edit.html"
    model = Article
    fields = '__all__'


class MyArticlesView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "registration/my_articles.html"
    context_object_name = "articles"
    fields = '__all__'

# class ArticleCreateView(LoginRequiredMixin, CreateView):
#   template_name = "article_add.html"
#    model = Article
#    fields = '__all__'
#
#    def form_valid(self, form):
#        form.instance.author = self.request.user
#        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "registration/profile.html"
    model = User
    fields = '__all__'


class MessageListView(ListView):
    template_name = 'message/list.html'
    model = Message


class MessageDetailView(DetailView):
    template_name = 'message/detail.html'
    model = Message


class MessageCreateView(CreateView):
    template_name = "message/add.html"
    model = Message
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    success_url = reverse_lazy('message_list')


class MessageUpdateView(UpdateView):
    template_name = "message/edit.html"
    model = Message
    fields = '__all__'
    success_url = reverse_lazy('message_list')


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'message/delete.html'
    success_url = reverse_lazy('message_list')
