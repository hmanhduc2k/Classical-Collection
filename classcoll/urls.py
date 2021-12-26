from django.urls import path
from classcoll.views import Attributes, Authentication, Composers, Discussion, Pieces, UserFavorite, Index

urlpatterns = [
    path("", Index.landingPage, name="index"),
    path("login", Authentication.loginPage, name="login"),
    path("logout", Authentication.logoutPage, name="logout"),
    path("register", Authentication.registerPage, name="register"),
    
    path('piece/', Pieces.allPieces, name="all_piece"),
    path('piece/<str:name>', Pieces.pieceInfo, name='piece'),
    
    path('composer/', Composers.allComposers, name="all_composer"),
    path('composer/<str:name>', Composers.composerInfo, name="composer"),
    
    path('period/<str:name>', Attributes.period, name="period"),
    path('difficulty/<str:name>', Attributes.difficulty, name="difficulty"),
    
    path('favorite/', UserFavorite.userFavorite, name="favorite"),
    path('favpiece/<str:id>', UserFavorite.favoritePiece, name="fav-piece"),
    path('favcomposer/<str:id>', UserFavorite.favoriteComposer, name='fav-composer'),
    
    path('comment/<str:id>', Discussion.comment, name="comment"),
    path('upvote/<str:id>', Discussion.upvote, name="upvote")
]
