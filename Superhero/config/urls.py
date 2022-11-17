from django.contrib import admin
from django.urls import path, include

from hero.views import UserUpdateView

urlpatterns = [

    # Hero
    path('', include('hero.urls')),

    # Photo
    path('', include('photos.urls')),

    # Admin views for users
    # path('admin/', admin.site.urls),
    # path('admin/', include('admin.site.urls')),   Don't do this!

]
