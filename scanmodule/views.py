from django.shortcuts import render
from .models import SiteAssest

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # Total scan query    
        context['total_scan'] = SiteAssest.objects..count()