from django import forms
from app1.models import courseModel,studentModel
import re

class courseForms(forms.ModelForm):
    fee = forms.IntegerField(min_value=3000)
    course_time = forms.TimeField()
    starting_date = forms.CharField(widget=forms.DateInput(attrs={'type': 'date'}), label="Starting Date")

    def clean_course_name(self):
        name = self.cleaned_data['course_name']
        res = re.findall(r'^[A-Z a-z]*$', name)
        if res:
            return name
        else:
            print(forms.ValidationError)
            raise forms.ValidationError("Invalid Name")

    def clean_faculty_name(self):
        name=self.cleaned_data['faculty_name']
        res = re.findall(r'^[A-Z a-z]*$', name)
        if res:
            return name
        else:
            print(forms.ValidationError)
            raise forms.ValidationError("Invalid Name")

    def clean_Duration(self):
        dur= self.cleaned_data['Duration']
        if dur>=30 and dur<=90:
            return dur
        else:
            print(forms.ValidationError)
            raise forms.ValidationError('Minimum Duration is 30 days and maximum is 90 days')

    class Meta:
        fields = '__all__'
        model = courseModel
        widgets = {
            "course_name" : forms.TextInput(attrs={'id':'cname','onblur':"ajaxCheck('http://127.0.0.1:8000/check_cname/','cname','cn')"})
        }

class studentForm(forms.ModelForm):
    def clean_Student_name(self):
        name = self.cleaned_data['Student_name']
        res = re.findall(r'^[A-Z a-z]*$', name)
        if res:
            return name
        else:
            print(forms.ValidationError)
            raise forms.ValidationError("Invalid Name")

    class Meta:
        fields = ["Student_name","Contact_Number","Password","email"]
        model = studentModel
        widgets = {
            'Student_name': forms.TextInput(attrs={'id': 'one'}),
            'Contact_Number':forms.NumberInput(attrs={'id': 'two','onblur':"ajaxCheck('http://127.0.0.1:8000/check_number/','two','Two')"}),
            'Password': forms.PasswordInput(attrs={'id':'three'}),
            'email': forms.EmailInput(attrs={'id':'four','onblur':"ajaxCheck('http://127.0.0.1:8000/check_email/','four','email')"}),
        }


