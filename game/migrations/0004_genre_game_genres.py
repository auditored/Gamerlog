# Generated by Django 4.0.5 on 2023-01-12 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_delete_platformer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='genres',
            field=models.ManyToManyField(to='game.genre'),
        ),
    ]