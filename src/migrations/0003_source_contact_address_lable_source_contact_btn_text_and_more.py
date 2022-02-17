# Generated by Django 4.0.2 on 2022-02-17 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_rename_section_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='contact_address_lable',
            field=models.CharField(default='My Address', max_length=100),
        ),
        migrations.AddField(
            model_name='source',
            name='contact_btn_text',
            field=models.CharField(default='Send Message', max_length=100),
        ),
        migrations.AddField(
            model_name='source',
            name='contact_email_lable',
            field=models.CharField(default='Email Me', max_length=100),
        ),
        migrations.AddField(
            model_name='source',
            name='contact_form_email_placeholder',
            field=models.CharField(default='Your Email', max_length=100),
        ),
        migrations.AddField(
            model_name='source',
            name='contact_form_message_placeholder',
            field=models.CharField(default='Message', max_length=100),
        ),
        migrations.AddField(
            model_name='source',
            name='contact_form_name_placeholder',
            field=models.CharField(default='Your Name', max_length=100),
        ),
        migrations.AddField(
            model_name='source',
            name='contact_form_subject_placeholder',
            field=models.CharField(default='Subject', max_length=100),
        ),
        migrations.AddField(
            model_name='source',
            name='contact_phone_lable',
            field=models.CharField(default='Call Me', max_length=100),
        ),
        migrations.AddField(
            model_name='source',
            name='contact_social_lable',
            field=models.CharField(default='Social Networks', max_length=100),
        ),
    ]