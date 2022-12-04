# Generated by Django 3.2 on 2022-12-04 18:55

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('contenido', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]