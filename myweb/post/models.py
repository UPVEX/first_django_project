from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    test = models.TextField()
    is_enabel = models.BooleanField(default=False)
    publish_date = models.DateField()
    created_time = models.DateTimeField()
    update_time = models.DateTimeField()
