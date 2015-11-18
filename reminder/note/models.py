from django.db import models
import mptt


# Create your models here.
class Colors(models.Model):
    name = models.CharField(max_length=12)

    def __unicode__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField('name', max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name="parent", related_name='child')

    def __unicode__(self):
        return self.name


class Notes(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    context = models.TextField()
    pub_date = models.DateTimeField('date published')
    color = models.ForeignKey(Colors)
    tag = models.ForeignKey(Tags)
    category = models.ForeignKey(Categories)

mptt.register(Categories,)