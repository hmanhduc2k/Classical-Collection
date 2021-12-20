from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Composer)
admin.site.register(Period)
admin.site.register(Difficulty)
admin.site.register(Comment)
admin.site.register(Upvote)
admin.site.register(Piece)
admin.site.register(Favorite)