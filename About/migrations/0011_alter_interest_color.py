# Generated by Django 4.0.2 on 2022-03-08 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0010_aboutme_interests_title_aboutme_skills_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='color',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
