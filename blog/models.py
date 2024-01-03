from django.db import models
#to get user that we created
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=200, default='Title tag')
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()
    
    def __str__(self) -> str:
        return self.title + " | " + str(self.author)
    """
The get_absolute_url method is like a helper function in Django models that helps you generate a link (URL) to a detailed view of an object. Here's why it might be useful:
Consistency: Instead of writing the logic to generate URLs in multiple places in your code, you define it once in the model. This makes your code more organized and easier to maintain.
Reusability: If you decide to change how your URLs are structured or generated, you only need to update it in one place (the get_absolute_url method) rather than hunting through your entire codebase.
"""
    def get_absolute_url(self):
        # we can also use 'home' to redirect to homepage
        return reverse('article', args=str(self.id))
