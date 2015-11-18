import mptt
from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField('name', max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name="parent", related_name='child')

    def __unicode__(self):
        return self.title

mptt.register(Category,)