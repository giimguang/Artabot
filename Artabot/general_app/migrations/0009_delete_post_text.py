# Generated by Django 4.0.7 on 2022-09-10 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general_app', '0008_alter_post_lyric_alter_post_text_text'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post_Text',
        ),
    ]
