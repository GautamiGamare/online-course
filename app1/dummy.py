from app1.models import courseModel,studentModel,stud_course
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.http import HttpResponse
from app1.courseForm import courseForms,studentForm
from django.db.utils import IntegrityError

res = courseModel.objects.all()
for x in res:
    print(x.id)
    print(x.course_name)
