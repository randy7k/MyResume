# Generated by Django 4.0.2 on 2022-02-24 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0005_alter_skill_percentage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]