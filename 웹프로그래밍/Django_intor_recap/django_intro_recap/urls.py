from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("throw/", views.throw),
    path("catch/", views.catch),
    path("lotto_pick/", views.lotto_pick),
    path("lotto_get/", views.lotto_get),
    path('lottery/', views.lottery),
    path('jackpot/', views.jackpot),
]
