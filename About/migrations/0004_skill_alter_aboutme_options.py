# Generated by Django 4.0.2 on 2022-02-24 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0003_rename_counts_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('percentage', models.IntegerField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='aboutme',
            options={'verbose_name': 'About Me', 'verbose_name_plural': 'About Me'},
        ),
    ]