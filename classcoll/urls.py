from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('piece/', views.allPieces, name="all_piece"),
    path('piece/<str:name>', views.piece, name='piece'),
    path('composer/', views.allComposers, name="all_composer"),
    path('composer/<str:name>', views.composer, name="composer")
]
