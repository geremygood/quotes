from django.db import models
import datetime

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=datetime.datetime.now())    
    slug = models.SlugField()
    wiki = models.URLField('Authors Wikipedia Page')

class Topic(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    pub_date = models.DateTimeField(default=datetime.datetime.now())

class Quote(models.Model):
    quote_text = models.TextField(max_length=2000)
    slug = models.SlugField()
    pub_date = models.DateTimeField(default=datetime.datetime.now())
    author = models.ForeignKey(Author)
    topic = models.ForeignKey(Topic)

