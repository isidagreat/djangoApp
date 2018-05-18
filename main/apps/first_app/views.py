from django.shortcuts import render,HttpResponse, redirect
# the index function is called when root is visited
def index(request):
	response = "Blogs Place Holder Coming Soon"
	return HttpResponse(response)

def new(request):
	response = "This a place holder where blog sign up will live"
	return HttpResponse(response)

def create(request):
	return redirect(index)

def show(request, number):
	response='Place holder for blog ' + number
	return HttpResponse(response)

def edit(request, number):
	response='Place holder for blog ' + number + ' edit page'
	return HttpResponse(response)

def destroy(request, number):
	return redirect(index)