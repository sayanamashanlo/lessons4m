# Generated by Django 4.2.8 on 2023-12-27 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shows', to='tv_shows.category'),
        ),
    ]
