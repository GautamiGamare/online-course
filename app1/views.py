from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.http import HttpResponse
from app1.models import courseModel,studentModel,stud_course
from app1.courseForm import courseForms,studentForm
from django.db.utils import IntegrityError


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

def save_student(req):
    sf = studentForm(req.POST)
    if sf.is_valid():
        print('valid')
        sf.save()
        return redirect('student_login')
    else:
        print('Invalid')
        return render(req, 'student_regis.html', {'form': sf})
#=====================================================================================================
#=====================================================================================================

def student_welcome(req):
    uname = req.POST.get('username')
    pas = req.POST.get('pass')
    if studentModel.objects.filter(Student_name=uname) and studentModel.objects.filter(Password=pas):
        res = studentModel.objects.filter(Student_name=uname).only('Student_name')
        #sid = studentModel.objects.get('sid')
        print(res)
        return render(req, 'student_welcome.html',{'data':res})
    else:
        return render(req, 'student_login.html', {'error': 'Username or Password is incorrect'})

def entrol_course(req):
    sid = req.GET.get('no')
    s = studentModel.objects.filter(sid=sid).all()
    res = courseModel.objects.all()
    return render(req, 'entrol_course.html', {'data': res,'sid':s})

def entrol(req):
    num =req.GET.get('no')
    sid= req.GET.get('sid')
    stud_course(sid=sid,cid=num).save()
    sc = stud_course.objects.filter(sid=sid).only('cid')
    #sc = stud_course.objects.filter(sid=sid).only('cid')
    #coures = courseModel.objects.all()
    return render(req,'entrol_course.html',{'msg':'Entrolled Successfully','sid':sid,'data':sc})

def view_entrolled_courses(req):
    sid = req.GET.get('no')
    sc = stud_course.objects.filter(sid=sid).only('cid')
    coures = courseModel.objects.all()
    return render(req,'view_entrolled_courses.html',{'data':sc,'course':coures,'sid':sid})

def cancel_entrolled_courses(req):
    sid = req.GET.get('no')
    sc = stud_course.objects.filter(sid=sid).only('cid')
    coures = courseModel.objects.all()
    return render(req, 'cancel_entrolled_courses.html', {'data': sc, 'course': coures,"sid":sid})

def delete_course(req):
    num = req.GET.get('del')
    sid = req.GET.get('sid')
    stud_course.objects.filter(cid=num).delete()
    sc = stud_course.objects.filter(sid=sid).only('cid')
    #return render(req,'view_entrolled_courses.html',{'sid':sid,'data':sc})
    return redirect('cancel_entrolled_courses')