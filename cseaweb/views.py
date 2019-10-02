from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'home.html')
def events(request):
	return render(request,'events.html')
def gallery(request):
	return render(request,'gallery.html')
def team(request):
	return render(request,'team.html')