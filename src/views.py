from django.shortcuts import render
from django.views import generic
from src.models import Source
from Home.models import Header
from About.models import AboutMe, Count, Skill, Interest, Testimonial

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
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())