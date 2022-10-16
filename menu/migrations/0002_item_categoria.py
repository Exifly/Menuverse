# Generated by Django 4.1 on 2022-09-02 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='categoria',
            field=models.CharField(blank=True, choices=[('v', 'Vegan'), ('g', 'Gluten Free'), ('t', 'Vegetarian')], default='', max_length=1),
        ),
    ]