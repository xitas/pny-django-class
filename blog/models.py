from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.CharField(max_length=512, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title