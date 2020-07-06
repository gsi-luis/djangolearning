from django.db import models
from django.db.models import Value
from django.db.models.functions import Concat


class PersonQuerySet(models.QuerySet):
    def authors(self):
        return self.filter(role='A')

    def editors(self):
        return self.filter(role='E')


class PersonManager(models.Manager):
    def get_queryset(self):
        return PersonQuerySet(self.model, using=self._db)

    def authors(self):
        return self.get_queryset().authors()

    def editors(self):
        return self.get_queryset().editors()


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=1, choices=[('A', 'Author'), ('E', 'Editor')])
    peoples = PersonManager()

    def full_name(self):
        return self.first_name + ' ' + self.last_name

    full_name.admin_order_field = Concat('first_name', Value(' '), 'last_name')

    def __str__(self):
        return self.full_name()
