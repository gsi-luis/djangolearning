# Generated by Django 3.0.8 on 2020-07-04 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_form', '0002_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_of_death',
            field=models.DateTimeField(blank=True),
        ),
    ]
