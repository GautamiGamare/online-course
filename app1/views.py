from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.http import HttpResponse
from app1.models import courseModel,studentModel,stud_course
from app1.courseForm import courseForms,studentForm
from django.db.utils import IntegrityError
from django.db.models import Q
from django.contrib import messages

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
    data = courseModel.objects.all()
    return render(req,'student.html',{'data':data})

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

def contact(req):
    return render(req,'contact.html')
#=====================================================================================================
#=====================================================================================================

def student_welcome(req):
    uname = req.POST.get('username')
    pas = req.POST.get('pass')
    course = courseModel.objects.all()
    try:
        result = studentModel.objects.get(Q(Student_name=uname,Password=pas))
        req.session['sid']=result.sid
        return render(req, 'student_welcome.html',{'data':result,'course':course})
    except studentModel.DoesNotExist:
        return render(req, 'student_login.html', {'error': 'Username or Password is incorrect'})

def entrol_course(req):
    res = courseModel.objects.all()
    return render(req, 'entrol_course.html', {'data': res})

def entrol(req):
    num =req.GET.get('no')
    sid= req.GET.get('sid')
    try:
        stud_course.objects.get(sid=sid,cid=num)
        messages.error(req,"Already Entrolled")
        return redirect('entrol_course')
    except stud_course.DoesNotExist:
        stud_course(sid=sid, cid=num).save()
        messages.success(req,"Entrolled Successfully")
        return redirect('entrol_course')

def view_entrolled_courses(req):
    sid = req.GET.get('sid')
    res = stud_course.objects.filter(sid=sid)
    coures = [courseModel.objects.get(cid=x.cid) for x in res]
    return render(req,'view_entrolled_courses.html',{'data':coures})

def cancel_entrolled_courses(req):
    sid = req.GET.get('sid')
    sc = stud_course.objects.filter(sid=sid)
    data =[courseModel.objects.get(cid=x.cid) for x in sc]
    return render(req, 'cancel_entrolled_courses.html',{'data': data})

def delete_course(request):
    cno = request.POST.get('cno')
    sid = request.POST.get('sid')
    stud_course.objects.get(cid=cno, sid=sid).delete()
    res = stud_course.objects.filter(sid=sid)
    data = [stud_course.objects.get(cid=x.cid) for x in res]
    return render(request, "cancel_entrolled_courses.html", {"data": data})

#    cid = req.GET.get('del')
#    sid = req.GET.get('sid')
#    stud_course.objects.get(cid=cid,sid=sid).delete()
#    res = stud_course.objects.filter(sid=sid)
#    data = [courseModel.objects.get(cid=x.cid) for x in res]
#    return render(req,'cancel_entrolled_courses.html',{'data':data})

def student_logout(req):
    del req.session['sid']
    return redirect('student_login')