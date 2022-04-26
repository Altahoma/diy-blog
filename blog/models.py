from django.db import models
from django.urls import reverse
import datetime


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(max_length=1000)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('blogger-detail', args=[str(self.id)])

    class Meta:
        ordering = ['-reg_date']


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])

    class Meta:
        ordering = ['-pub_date']


class Comment(models.Model):
    description = models.TextField(max_length=500)
    author = models.ForeignKey('Author', on_delete=models.SET('Author DELETED'))
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.description[:75]}...'

    class Meta:
        ordering = ['pub_date']
