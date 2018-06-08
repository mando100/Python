from django.shortcuts import render
from django.http import HttpResponse
from .models import Campaign

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def profit (request):
	profit_list = Campaign.objects.get()
	output = ', '.join([q.campaign_id for q in profit_list])
	return HttpResponse(output)