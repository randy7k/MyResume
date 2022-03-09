from django.shortcuts import render
from django.core.mail import send_mail
from django.views import generic
from django.http import HttpResponse
from src.models import Source
from Home.models import Header
from About.models import AboutMe, Count, Skill, Interest, Testimonial
from Resume.models import Section
from Service.models import Service
from Portfolio.models import Category
from Contact.forms import ContactForm
from MyResume.settings import EMAIL_RECEIVER_LIST

class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['src'] = Source.objects.last()
        context['header'] = Header.objects.last()
        context['about_me'] = AboutMe.objects.last()
        context['counts'] = Count.objects.all()
        context['skills'] = Skill.objects.all()
        context['interests'] = Interest.objects.all()
        context['testimonials'] = Testimonial.objects.all()
        context['resume'] = Section.objects.all()
        context['services'] = Service.objects.all()
        context['portfolio_categories'] = Category.objects.distinct().filter(portfolio__show=True)
        context['contact_form'] = ContactForm()
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['contact_form'] = ContactForm(request.POST)
        
        if context['contact_form'].is_valid():    
            context['contact_form'].save()
            send_email(request)
            context['contact_message_success'] = "Your message has been sent. <strong>Thank you!</strong>"
            context['contact_form'] = ContactForm()
        
        return render(request, self.template_name, context)

def send_email(request):
    name = request.POST.get('name', '')
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('email', '')
    message += "\n\nfrom: " + name + " (" + from_email + ")"
    
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, EMAIL_RECEIVER_LIST)
        except:
            return HttpResponse('Invalid header found.')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')