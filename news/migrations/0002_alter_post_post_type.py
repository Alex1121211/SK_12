# Generated by Django 3.2.8 on 2021-11-13 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('PO', 'post'), ('NW', 'news')], max_length=2),
        ),
    ]
