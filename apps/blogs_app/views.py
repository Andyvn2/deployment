from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *

def index(request):
	response = "Placeholder to later display all the Courses"
	
	return render(request, "blogs_app/index.html", {"courses": Course.objects.all()	})

def delete(request,id):
	print "start delete"
	print id
	A = Course.objects.get(id=id)
	A.delete()

	
	return redirect('/')

def confirm(request,id):
	return render(request, "blogs_app/delete.html", {"courses": Course.objects.get(id=id)})

def create(request):
	if request.method=="POST":
		errors = Course.objects.basic_validator(request.POST)
		if len(errors):
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags=tag)
		else:
			course_name=request.POST["course_name"]
			desc = request.POST["desc"]
			course = Course(course_name=course_name, desc=desc)
			course.save()
	return redirect('/')

# def news(request):
# 	response = "Placeholder for a new post"
# 	return HttpResponse(response)


# def create(request):
# 	print "create initiate"
# 	if request.method == "POST":
# 		print "*"*50
# 		print request.POST['name']
# 		print request.POST['desc']
# 		request.session['name']= request.POST['name']
# 		print '*'*50
# 		print request.session['name']
# 		return redirect('/')
# 	else:
# 		return redirect('/')



	# 	print "*"*50
	# 	print request.POST
 #        print request.POST['name']
 #        print request.POST['desc']
 #        request.session['name'] = "test"  # more on session below
	# 	print "*"*50
	# 	return redirect("/")
	# else:
	# 	return redirect("/")


# def show(request, number):
# 	print "running request"
# 	response = "Place holder to display blog" +" " ,  number
# 	return HttpResponse(response)

# def edit(request, number):
# 	print "running request edit"
# 	response = "Place holder to edit blog" + " ", number
# 	return HttpResponse(response)
 

# def destroy(request, number):
# 	return redirect("/")