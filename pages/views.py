from django.http import HttpResponse
from django.shortcuts import render
from .forms import ToDoForm, MOVIESinfoForm
from .models import ToDo, MOVIESinfo

# Create your views here.

def home_view(request, *args, **kwargs):  # *args & **kwargs  
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):  # *args & **kwargs  
	return render(request, "contact.html", {})   # a string of HTML code

def about_view(request, *args, **kwargs):  # *args & **kwargs  
	return render(request, "about.html", {})   # a string of HTML code

def faqs_view(request, *args, **kwargs):  # *args & **kwargs  
	return render(request, "faqs.html", {})   # a string of HTML code	

def apps1_view(request, *args, **kwargs):  # *args & **kwargs  
	return render(request, "apps1.html", {})   # a string of HTML code	

def apps_view(request):
	my_form = ToDoForm()
	if request.method == "POST":
		my_form = ToDoForm(request.POST)
		if my_form.is_valid():
			print(my_form.cleaned_data)
			movies_info.objects.create(**my_form.cleaned_data)
		else:
			print(my_form.errors)
	context = {
		 "form": my_form
		}
	return render(request, "todo_create.html", context)


def movies_info_view(request):
	my_form = MOVIESinfoForm()
	if request.method == "POST":
		my_form = MOVIESinfoForm(request.POST)
		if my_form.is_valid():
			print(my_form.cleaned_data)
			MOVIESinfo.objects.create(**my_form.cleaned_data)
		else:
			print(my_form.errors)
	context = {
		 "form": my_form
		}
	return render(request, "movies_info_create.html", context)