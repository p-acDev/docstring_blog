from django.db import models

# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.tag_name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField()
    tag = models.ManyToManyField(Tag, blank=True)
    
    
