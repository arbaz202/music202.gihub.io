# Generated by Django 2.2.3 on 2019-07-23 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='album title', max_length=100)),
                ('artist', models.CharField(help_text='album artist', max_length=50)),
                ('genre', models.CharField(help_text='album genre', max_length=20)),
                ('year', models.DateField(help_text='release date')),
                ('image', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Song title', max_length=100)),
                ('artist', models.CharField(help_text='Song artist', max_length=50)),
                ('genre', models.CharField(help_text='Song genre', max_length=20)),
                ('sfile', models.FileField(upload_to='')),
                ('image', models.FileField(upload_to='')),
                ('al_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gaana.Album')),
            ],
        ),
    ]
