# Generated by Django 4.0.7 on 2022-09-26 09:34

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
                ('title', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=100, null=True)),
                ('album', models.CharField(blank=True, max_length=100, null=True)),
                ('lyric', models.TextField()),
                ('tag', models.CharField(max_length=50)),
                ('language', models.CharField(choices=[('chinese', 'CH'), ('english', 'ENG'), ('khmer', 'KM'), ('thai', 'TH')], max_length=50)),
                ('image', models.ImageField(default='default-img.jpg', upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='User_Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('report', models.TextField()),
            ],
        ),
    ]
