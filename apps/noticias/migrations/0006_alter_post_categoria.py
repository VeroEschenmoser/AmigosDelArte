# Generated by Django 3.2 on 2022-12-16 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0005_auto_20221216_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categoria',
            field=models.ForeignKey(default='Arte', on_delete=django.db.models.deletion.CASCADE, to='noticias.categoria'),
        ),
    ]