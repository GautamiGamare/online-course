from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.http import HttpResponse
from app1.models import courseModel,studentModel
from app1.courseForm import courseForms,studentForm

def admin_login(req):
    return render(req, 'admin_login.html')

def login_check(req):
    user = req.POST.get('username')
    pas = req.POST.get('pass')
    print(user)
    print(pas)
    if user == 'Gautami' and pas == 'Gautami':
        return render(req, 'admin_welcome.html', {'name': user})
    else:
        return render(req, 'admin_login.html', {'error': 'Username or Password is incorrect'})

def admin_welcome(req):
    return render(req, 'admin_welcome.html')

def view_classes(req):
    res = courseModel.objects.all()
    return render(req,'view_classes.html',{'data':res})

def add_new_class(req):
    return render(req,'add_new_class.html',{'form':courseForms()})

def save_course(req):
    sf = courseForms(req.POST)
    if sf.is_valid():
        print('valid')
        sf.save()
        #res = Stocker.objects.all()
        return redirect('view_classes')
    else:
        print('Invalid')
        return render(req,'add_new_class.html',{'form':sf})

class update(UpdateView):
    template_name = 'update.html'
    model = courseModel
    fields = '__all__'
    success_url = '/view_classes/'

def delete(req):
    num = req.GET.get('no')
    courseModel.objects.filter(cid=num).delete()
    return redirect('view_classes')
#---------------------------STUDENT-----------------------------

def student(req):
    return render(req,'student.html')

def student_login(req):
    return render(req,'student_login.html')

def student_regis(req):
    return render(req,'student_regis.html',{'form':studentForm()})

def student_valid(req):
    uname = req.POST.get('username')
    pas = req.POST.get('pass')
    a = studentModel.objects.filter(Student_name=uname)
    b = studentModel.objects.filter(Password=pas)
    if a and b:
        #res = studentModel.objects.filter(Student_name=uname).all()
        # print(res)
        return render(req, 'student_welcome.html')
    else:
        return render(req, 'student_login.html', {'error': 'Username or Password is incorrect'})
    return None

def student_welcome(req):
    res = studentModel.objects.all()
    return render(req,'student_welcome.html',{"stud":res})

def save_student(req):
    sf = studentForm(req.POST)
    if sf.is_valid():
        print('valid')
        sf.save()
        # res = Stocker.objects.all()
        return redirect('student_login')
    else:
        print('Invalid')
        return render(req, 'student_regis.html', {'form': sf})

def student_welcome(req):
    #nm = studentModel.objects.all()
    return render(req,'student_welcome.html')

def entrol_course(req):
    res = courseModel.objects.all()
    return render(req, 'entrol_course.html', {'data': res})

def view_entrolled_courses(req):
    return None

def cancel_entrolled_courses(req):
    return None

def entrol(req):
    num =req.GET.get('no')

    id = studentModel.objects.only('sid')
    #for x in id:
     #   print(x.sid)
    #print("getting num ",num)
    #print(sid)
    #print(sid)
    res =studentModel.Student_Course(num,)
    return HttpResponse(id)