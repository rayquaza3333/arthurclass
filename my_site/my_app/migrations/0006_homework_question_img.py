# Generated by Django 2.2.4 on 2019-10-09 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_delete_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='question_img',
            field=models.ImageField(null='True', upload_to='homeworks'),
            preserve_default='True',
        ),
    ]