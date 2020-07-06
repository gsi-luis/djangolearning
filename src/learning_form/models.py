from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.CharField(max_length=500)
    create_date = models.DateTimeField()


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateTimeField()
    date_of_death = models.DateTimeField(blank=True)

    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.full_name()

    def get_absolute_url(self):
        return reverse('learning_form:author_detail', args=(self.pk,))
