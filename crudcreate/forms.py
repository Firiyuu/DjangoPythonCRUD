from crud.models import Student
from django import forms

#We make a form with the fields indicated via this class using the  model STUDENT
class NameForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'middle_name', 'course', 'gender', 'year')




