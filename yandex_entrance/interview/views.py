from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader


def index(request):
	template = loader.get_template('index.html')
	context = {
        'test_list': [1, 5, 2]
    }
	return HttpResponse(template.render(context, request))
