from django.contrib import admin
from .models import Source, SocialNetwork

class SourceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General',     {'fields': ['name','isotipo','color','color_light']}),
        ('Home',        {'fields':['home_name']}),
        ('About',       {'fields':['about_name','about_title','show_about']}),
        ('Resume',      {'fields':['resume_name','resume_title','show_resume']}),
        ('Services',    {'fields':['services_name','services_title','show_services']}),
        ('Portfoio',    {'fields':['portfoio_name','portfoio_title','show_portfoio']}),
        ('Contact',     {'fields':['contact_name','contact_title','contact_address_lable','contact_social_lable','contact_email_lable','contact_phone_lable','contact_form_name_placeholder','contact_form_email_placeholder','contact_form_subject_placeholder','contact_form_message_placeholder','contact_btn_text','show_contact']}),
        ('Personal',    {'fields':['address','email','phone']})
    ]

admin.site.register(Source, SourceAdmin)
admin.site.register(SocialNetwork)
