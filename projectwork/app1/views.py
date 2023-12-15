from django.shortcuts import render, redirect
from app1.models import Contact
from app1.forms import ContactForm
# Create your views here.
def baseview(request):
	return render(request,'app1/base.html')

def homeview(request):
	return render(request,'app1/home.html')

def aboutview(request):
	return render(request,'app1/about us.html')

def servicesview(request):
	return render(request,'app1/services.html')

def galleryview(request):
	return render(request,'app1/gallery.html')

def contactview(request):
	form=ContactForm()
	if request.method=="POST":
		form=ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/users')
	return render(request,'app1/contact.html',{'form':form})

def usersview(request):
	c=Contact.objects.all()
	return render(request,'app1/users.html',{'c':c})