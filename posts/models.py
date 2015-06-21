from django.db import models

class Post(models.Model):
    title = models.CharField(u'Зоголовок поста', max_length=150)
    content = models.TextField(u'Контент', blank=True)
    published = models.BooleanField(u'Опубликовано', default=False)


def __unicode__(self):
        return self.title

def get_absolute_url(self):
        return "posts/%i/" % self.id
