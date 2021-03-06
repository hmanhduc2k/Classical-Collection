from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Composer(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    image = models.URLField(blank=False)
    
    def __str__(self) -> str:
        return f"{self.name}#{self.id}"
    
    def serialize(self):
        return {
            'name': self.name,
            'biography': self.biography,
            'image': self.image
        }
    
class Period(models.Model):
    era = models.CharField(max_length=50)
    description = models.TextField(null=True)
    
    def __str__(self) -> str:
        return f"{self.era}#{self.id}"
    
class Difficulty(models.Model):
    rating = models.CharField(max_length=20)
    description = models.TextField(null=True)
    
    def __str__(self) -> str:
        return f"{self.rating}#{self.id}"
    
class Piece(models.Model):
    name = models.CharField(max_length=100)
    composer = models.ForeignKey(Composer, on_delete=models.CASCADE)
    description = models.TextField()
    source = models.FileField()
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.name}#{self.composer}#{self.id}"
    
    def serialize(self):
        return {
            'name': self.name,
            'composer': self.composer,
            'description': self.description,
            'source': self.source,
            'period': self.period,
            'difficulty': self.difficulty
        }
    
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pieces = models.ManyToManyField(Piece, blank=True, related_name='pieces')
    composers = models.ManyToManyField(Composer, blank=True, related_name='composers')
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    piece = models.ForeignKey(Piece, null=True, on_delete=models.CASCADE, related_name='piece')
    
    def __str__(self) -> str:
        return f"{self.user} commented {self.content} at {self.time}"

class Upvote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)