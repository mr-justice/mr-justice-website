from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.CharField(max_length=100)
    
    # returns name/title of object instead of 'object (#)'
    def __str__(self):
        return self.title #or self.title for blog posts