# Generated by Django 2.2.4 on 2019-10-25 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sidebyside1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recording',
            name='chapter',
        ),
        migrations.RemoveField(
            model_name='recording',
            name='recording_number',
        ),
        migrations.AddField(
            model_name='recording',
            name='title',
            field=models.CharField(default='Not uploaded', max_length=256),
        ),
        migrations.DeleteModel(
            name='Chapter',
        ),
    ]
