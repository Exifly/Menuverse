# Generated by Django 4.1 on 2022-10-16 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_item_descrizione_alter_feedback_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='descrizione',
            field=models.TextField(blank=True, default='This is a wider card with supporting text below as a natural lead-in to\n                            additional content. This content is a little bit longer.', null=True),
        ),
    ]