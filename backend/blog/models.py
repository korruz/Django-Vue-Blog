from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)

    class Meta:
        db_table = "t_blog"
