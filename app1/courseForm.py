from django import forms
from app1.models import courseModel,studentModel
import re

class courseForms(forms.ModelForm):
    fee = forms.IntegerField(min_value=3000)
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

class studentForm(forms.ModelForm):
    class Meta:
        fields = ["Student_name","Contact_Number","Password","email"]
        model = studentModel

#class stud_courseForm(forms.ModelForm):
 #   class Meta:
  #      fields = ["Student_Course"]
   #     model = studentModel,courseModel

    #Student_Course = forms.CharField(widget=forms.)


