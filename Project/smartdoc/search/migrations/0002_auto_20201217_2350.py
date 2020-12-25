# Generated by Django 3.1.4 on 2020-12-17 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='text',
            field=models.CharField(blank=True, default='image text', max_length=5000),
        ),
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(upload_to='uploads/images'),
        ),
    ]