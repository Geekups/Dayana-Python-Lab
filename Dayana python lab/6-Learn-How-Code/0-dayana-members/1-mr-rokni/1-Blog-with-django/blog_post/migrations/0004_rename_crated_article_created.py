# Generated by Django 4.0.6 on 2022-08-01 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0003_category_article_pubdate_article_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='crated',
            new_name='created',
        ),
    ]
