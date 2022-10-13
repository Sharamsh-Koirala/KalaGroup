from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Subsidiary


def subsidiaryKalaInc(request):
    return render(request, 'subsidiaries/kala_incorp_page.html')

def subsidiaryKalaMarketing(request):
    return render(request, 'subsidiaries/kala_marketing_page.html')

def subsidiaryKalaInternational(request):
    return render(request, 'subsidiaries/kala_international_page.html')

def subsidiaryKalaAgency(request):
    return render(request, 'subsidiaries/kala_agency_page.html')

def subsidiaryEVGO(request):
    return render(request, 'subsidiaries/evgo_nepal_page.html')

def subsidiaryKalaAgro(request):
    return render(request, 'subsidiaries/kala_agro_page.html')

def subsidiaries(request):
    subsidiaries = Subsidiary.objects.all()
    context = {'subsidiaries' : subsidiaries}
    return render(request, 'subsidiaries/subsidiaries.html', context)

def subsidiary(request,pk):
    subsidiaryObj = Subsidiary.objects.get(id=pk)
    context = {'subsidiary':subsidiaryObj}
    return render(request, 'subsidiaries/single-subsidiary.html',context)