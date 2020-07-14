from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Home
from . forms import MemberFrom
from django.contrib import messages

# Create your views here.
def home(request):
	home = Home.objects.all()
	return render(request,'home.html',{'all':home})

def join(request):
	if request.method == 'POST':
		form = MemberFrom(request.POST or None)
		if form.is_valid():
			form.save()
		messages.success(request,('success'))
		return redirect('home')


	else:		
		return render(request,'join.html',{})
