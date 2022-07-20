from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=45)
    slug = models.SlugField()
    intro= models.TextField()
    body = models.TextField()
    image = models.ImageField(upload_to='uploads/',blank=True,null=True)
    user = models.ForeignKey(User,related_name="posts",on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
    user = models.ForeignKey(User,related_name="comments",on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
