from django.urls import path
from .views import BlackWidow, Hero1View, IndexView, IronManView

urlpatterns = [
    path('', IndexView.as_view()),
    path('hulk', Hero1View.as_view()),
    path('ironman', IronManView.as_view()),
    path('blackwidow', BlackWidow.as_view()),
]
