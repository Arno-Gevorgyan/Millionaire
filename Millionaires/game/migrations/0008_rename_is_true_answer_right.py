# Generated by Django 3.2.3 on 2021-06-02 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_auto_20210602_1031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='is_true',
            new_name='right',
        ),
    ]