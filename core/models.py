from django.db import models
from django.utils.text import slugify
# Create your models here.

INFOCHOICES = (
    ("redis","redis"),
    ("celery","celery"),
    ("celery_beat","celery_beat"),
    ("django-allauth","django-allauth"),
    ("django-environ","django-environ"),
    ("django-jazzmin","django-jazzmin"),
    ("django-modeltranslation","django-modeltranslation"),
    ("django-phonenumber-field","django-phonenumber-field"),
    ("DjangoRestFramework","DjangoRestFramework"),
    ("phonenumbers","phonenumbers"),
    ("postgresql","postgresql"),
    ("stripe","stripe"),
    ("whitenoise","whitenoise"),
    ("Bucket","Bucket"),
    ("Docker","Docker"),
)


class Work(models.Model):
    name = models.CharField(max_length = 150)
    category = models.CharField(max_length = 150)
    description = models.TextField()
    WorkInfo = models.ManyToManyField("WorkInfo")
    slug = models.CharField(max_length = 150, null=True, blank=True)
    image = models.ImageField(upload_to='MainImage/')
    
    def __str__ (self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save()
        
    
class WorkFile(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE ,related_name='works')
    image = models.ImageField(upload_to='WorkImages/')
        
    def __str__ (self):
        return self.work.name

class WorkInfo(models.Model):
    name = models.CharField(max_length = 150, choices=INFOCHOICES)
    
    def __str__ (self):
        return self.name
    