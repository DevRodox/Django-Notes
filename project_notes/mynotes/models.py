from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(default='Texto predeterminado')
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
