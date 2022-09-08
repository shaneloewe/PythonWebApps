from django.urls import path
from .views import BouncingBoyView, AFOBView, IndexView, MatterEaterLadView

# Links to the hero.html file with X Hero "as view"
urlpatterns = [
    path('', IndexView.as_view()),
    path('afob', AFOBView.as_view()),
    path('mel', MatterEaterLadView.as_view()),
    path('bb', BouncingBoyView.as_view()),
]
