# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from scanmodule.models import SiteAssest, ScanHistory
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth

@login_required(login_url="/login/")
def index(request):
    site_obj_count = SiteAssest.objects.aggregate(Sum('scan_count'))
    positive_rank = SiteAssest.objects.filter(site_rank__lte=5).count()
    medium_rank = SiteAssest.objects.filter(site_rank__gt=5, site_rank__lte=7).count()
    bad_rank = SiteAssest.objects.filter(site_rank__gte=8).count()
    agg_month_year = ScanHistory.objects.annotate(month=TruncMonth('scan_date_record'))

    return render(request, "index.html",{'site_obj_count':site_obj_count, 
    'positive_rank':positive_rank, 'medium_rank':medium_rank,
     'bad_rank':bad_rank, 'agg_month_year':agg_month_year})

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
