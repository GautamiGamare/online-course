from django.db import models

class courseModel(models.Model):
    cid = models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=10,unique=True)
    faculty_name=models.CharField(max_length=20)
    starting_date = models.DateField()
    course_time = models.TimeField(default=False)
    fee = models.IntegerField()
    Duration = models.IntegerField()

class studentModel(models.Model):
    sid = models.AutoField(primary_key= True)
    Student_name=models.CharField(max_length=20)
    Contact_Number = models.IntegerField()
    email = models.EmailField(max_length=20)
    Password = models.CharField(max_length=20)
    #Student_Course = models.ManyToManyField(courseModel)

class stud_course(models.Model):
    id = models.AutoField(primary_key=True)
    sid = models.IntegerField()
    cid = models.IntegerField()