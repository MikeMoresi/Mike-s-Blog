# Generated by Django 3.2.3 on 2021-06-04 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_auto_20210604_1026'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
