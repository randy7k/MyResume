from django.db import models
class Source(models.Model):
    # Feneral
    name = models.CharField(max_length=100)
    isotipo = models.ImageField(upload_to='src/isotipos', blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    color_light = models.CharField(max_length=100, blank=True, null=True)

    # Home
    home_name = models.CharField(max_length=100, default="Home")

    # About
    about_name = models.CharField(max_length=100, default="About")
    about_title = models.CharField(max_length=100, default="Learn more about me")
    show_about = models.BooleanField(default=True)

    # Resume
    resume_name = models.CharField(max_length=100, default="Resume")
    resume_title = models.CharField(max_length=100, default="Check my resume")
    show_resume = models.BooleanField(default=True)

    # Services
    services_name = models.CharField(max_length=100, default="Services")
    services_title = models.CharField(max_length=100, default="My services")
    show_services = models.BooleanField(default=True)

    # Portfoio
    portfoio_name = models.CharField(max_length=100, default="Portfoio")
    portfoio_title = models.CharField(max_length=100, default="My works")
    show_portfoio = models.BooleanField(default=True)

    # Contact
    contact_name = models.CharField(max_length=100, default="Contact")
    contact_title = models.CharField(max_length=100, default="Contact me")
    
    contact_address_lable = models.CharField(max_length=100, default="My Address")
    contact_social_lable = models.CharField(max_length=100, default="Social Networks")
    contact_email_lable = models.CharField(max_length=100, default="Email Me")
    contact_phone_lable = models.CharField(max_length=100, default="Call Me")
    
    contact_form_name_placeholder = models.CharField(max_length=100, default="Your Name")
    contact_form_email_placeholder = models.CharField(max_length=100, default="Your Email")
    contact_form_subject_placeholder = models.CharField(max_length=100, default="Subject")
    contact_form_message_placeholder = models.CharField(max_length=100, default="Message")
    contact_btn_text = models.CharField(max_length=100, default="Send Message")

    show_contact = models.BooleanField(default=True)

    # Personal
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class SocialNetwork(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    url = models.URLField()
    source = models.ForeignKey(Source, on_delete=models.CASCADE, default=Source.objects.last().id, related_name='social_networks')

    def __str__(self):
        return self.name