# Generated by Django 4.0.7 on 2022-09-10 18:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general_app', '0005_post_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_text',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]