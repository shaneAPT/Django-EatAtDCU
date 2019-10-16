from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Restaurant,Campus
import json,requests
from random import randint

def index(request):
	template = loader.get_template('eatatdcu/index.html')## https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9
	featured_restaurant = Restaurant.objects.filter(restaurant_id=randint(1,len(Restaurant.objects.all())))
	return HttpResponse(template.render({'featured_restaurant':featured_restaurant},request))

def restaurants(request):
	template = loader.get_template('eatatdcu/restaurants.html')
	campus_name = request.GET.get('campus','').lower()
	try:
		campus = Campus.objects.get(name=campus_name)
		if "staff-only" in request.GET: ## https://stackoverflow.com/questions/19299344/how-to-know-whether-a-checkbox-was-selected-in-python-django
			if "restaurant-checkbox" in request.GET and "cafe-checkbox" in request.GET:
				cafes = Restaurant.objects.filter(campus_id=campus,is_restaurant=False, is_staff_only=1)
				restaurants = Restaurant.objects.filter(campus_id=campus,is_restaurant=True, is_staff_only=1)
			elif "restaurant-checkbox" in request.GET:
				restaurants = Restaurant.objects.filter(campus_id=campus,is_restaurant=True, is_staff_only=1)
				cafes = None
			elif "cafe-checkbox" in request.GET:
				cafes = Restaurant.objects.filter(campus_id=campus,is_restaurant=False, is_staff_only=1)
				restaurants = None
			else:
				restaurants = None
				cafes = None
		else:
			if "restaurant-checkbox" in request.GET and "cafe-checkbox" in request.GET:
				cafes = Restaurant.objects.filter(campus_id=campus,is_restaurant=False)
				restaurants = Restaurant.objects.filter(campus_id=campus,is_restaurant=True)				
			elif "restaurant-checkbox" in request.GET:
				restaurants = Restaurant.objects.filter(campus_id=campus,is_restaurant=True)
				cafes = None
			elif "cafe-checkbox" in request.GET:
				cafes = Restaurant.objects.filter(campus_id=campus,is_restaurant=False)
				restaurants = None
			else:
				restaurants = None
				cafes = None			

	except Restaurant.DoesNotExist:
		return HttpResponse(template.render({'error':'No such restaurant','campus_name':campus_name},request))
	except Campus.DoesNotExist:
		return HttpResponse(template.render({'error':'Error: you must enter a valid DCU campus (example: St Pats, DCU Alpha)','campus_name':campus_name},request))
	return HttpResponse(template.render({'restaurants':restaurants,'cafes':cafes,'campus_name':campus_name},request))

def specials(request,restaurant):
	template = loader.get_template('eatatdcu/specials.html')
	daily_webservice_url = 'http://jfoster.pythonanywhere.com/specials/'+restaurant
	all_webservice_url = 'http://jfoster.pythonanywhere.com/allspecials/'+restaurant

	daily_real_time_info = requests.get(daily_webservice_url).json()
	all_real_time_info = requests.get(all_webservice_url).json()

	if 'error_msg' in daily_real_time_info or 'error_msg' in all_real_time_info:
	   return HttpResponse(template.render({'error':daily_real_time_info['error_msg']},request))
	else:
	   return HttpResponse(template.render({'real_time':daily_real_time_info, 'all_time':all_real_time_info},request))
