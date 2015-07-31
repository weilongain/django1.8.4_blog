from django.db import models
from django_markdown.models import MarkdownField
# Create your models her


class Tag(models.Model):
    question_text = models.CharField(max_length=10)
    def __str__(self):
        return self.question_text


class MyBlog(models.Model):
    tittle = models.CharField(max_length=50,default="")
    tittle_sm = models.CharField(max_length=50,default="")
    body = MarkdownField(default="")
    pub_date = models.DateTimeField(auto_now=True,blank=True)
    publisher = models.BooleanField(default=False)
    tag = models.ForeignKey(Tag)
    def __str__(self):
        return self.tittle


