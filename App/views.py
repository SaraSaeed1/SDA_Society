from django.shortcuts import render,redirect
from django.contrib import messages
from . models import *

def index(request):
    context={
        'bootcamp':Bootcamp.objects.all()
    }
    return render(request,"index.html", context)



def bootcamp (request, _id):
    context ={
        'bootcamp': Bootcamp.objects.get(id=_id),
        'champion' : Champion.objects.all()
    }
    return render (request, 'bootcamp.html', context)



def reg_log(request):
    context={
        'bootcamp':Bootcamp.objects.all()
    }
    return render(request,"reg_log.html", context)



def registration(request):
    if request.method=='POST':
        errors = Student.objects.registration_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/reg_log')
        else:
            _hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            _newStudent = Student.objects.create(
                fname = request.POST['fname'],
                lname = request.POST['lname'],
                email = request.POST['email'],
                bootcamp=Bootcamp.objects.get(id=request.POST['bootcamp']),
                password = _hash
            )
            _newStudent.save()
            request.session['student_id'] = _newStudent.id
            return redirect('/home_student')
    else:
        return redirect ('/reg_log')



def login(request):
    if request.method == 'POST':
        errors = Student.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/reg_log')
        else:
            log_Student=Student.objects.get(email__iexact=request.POST['email'])
            request.session['student_id'] = log_Student.id
            return redirect('/home_student')
    else:
        return redirect('/reg_log')



def profile(request):
    if not 'student_id' in request.session:
        return redirect('/')
    context = {
        'bootcamp' : Bootcamp.objects.all(),
        "student" : Student.objects.get(id=request.session['student_id'])
    }
    return render(request, "student/profile.html", context)



def home_student(request):
    if not 'student_id' in request.session:
        return redirect('/')
    context = {
        'bootcamp':Bootcamp.objects.all(),
        "student" : Student.objects.get(id=request.session['student_id'])
    }
    return render(request, "student/home_student.html", context)


def info_bootcamp(request, _id):
    if not 'student_id' in request.session:
        return redirect('/')
    context = {
        "student" : Student.objects.get(id=request.session['student_id']),
        'bootcamp': Bootcamp.objects.get(id=_id),
        'champion' : Champion.objects.all()
    }
    return render (request, 'student/info_bootcamp.html', context)


def go_add_project(request):
    if not 'student_id' in request.session:
        return redirect('/')
    context = {
        "student" : Student.objects.get(id=request.session['student_id'])
    }
    return render(request, "student/add_project.html",context)



def new_project(request):
    if request.method=='POST':
        student= Student.objects.get(id=request.session['student_id'])
        project=Project.objects.create(
            title = request.POST['title'],
            desc = request.POST['desc'],
            url = request.POST['url'],
            student = student
        )
        project.save()
    return redirect ('/profile')


def remove_project(request, _id):
    project = Project.objects.get(id=_id)
    student = request.session['student_id']
    if student == project.student.id:
        project.delete()
    return redirect('/profile')



def go_edit_project(request, _id):
    if not 'student_id' in request.session:
        return redirect('/')
    context = {
        "student": Student.objects.get(id=request.session['student_id']),
        'project': Project.objects.get(id=_id)
    }
    return render(request, "student/edit_project.html", context)



def edit_project(request, _id):
    if 'student_id' not in request.session:
        return redirect('/')
    
    project=Project.objects.get(id=_id)
    if request.session['student_id'] != project.student.id:
        return redirect('/profile')
    
    if request.method == 'POST':
        updates=project
        updates.title=request.POST['title']
        updates.desc=request.POST['desc']
        updates.url=request.POST['url']
        updates.save()
        return redirect('/profile')
    return redirect('/profile')



def go_edit_profile(request):
    if not 'student_id' in request.session:
        return redirect('/')
    context = {
        "student": Student.objects.get(id=request.session['student_id']),
    }
    return render(request, "student/edit_profile.html", context)


def edit_profile(request,_id):
    if 'student_id' not in request.session:
        return redirect('/')
    
    student=Student.objects.get(id=_id)
    if request.session['student_id'] != student.id:
        return redirect('/profile')
    
    if request.method == 'POST':
        updates=student
        updates.fname=request.POST['fname']
        updates.lname=request.POST['lname']
        updates.save()
        return redirect('/profile')
    return redirect('/profile')





def go_profile(request,_id):
    if 'student_id' not in request.session:
        return redirect('/reg_log')
    student=Student.objects.get(id=_id)
    if request.session['student_id'] == student.id:
        return redirect('/profile')
    else:
        context = {
        "this_student":Student.objects.get(id=request.session['student_id']),
        "student":student
        }
    return render(request, "student/profile_student.html", context)



def add_comment(request, _id):
    if 'student_id' not in request.session:
        return redirect('/reg_log')

    if request.method == 'POST':
        bootcamp = Bootcamp.objects.get(id=_id)
        student = Student.objects.get(id=request.session['student_id'])
        comment = Comment.objects.create(
            comment=request.POST['comment'],
            student=student,
            bootcamp=bootcamp
        )
        comment.save()
    return redirect(f'/info_bootcamp/{_id}')




def logout(request):
    del request.session['student_id']
    return redirect('/')