from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.views.generic import UpdateView

from .models import Student
from django.shortcuts import render
from django.template import loader

# ------------------------------------------------------------
# LIST and DETAIL VIEW
# Description : List and detail view
# ------------------------------------------------------------


#Generate all entry from database via STUDENT model
#Show counter, to show how many entries is in the database

def list(request):
    all_students = Student.objects.all()
    context = { 'all_students': all_students}

    return render(request, 'crud/list.html', context)



#When the Reference is called for an entry, details are shown. Through this function
def detail(request, student_id):
    print student_id
    obj = Student.objects.get(id = int(student_id))
    student_first_name = obj.first_name
    student_middle_name = obj.middle_name
    student_last_name = obj.last_name
    student_course = obj.course
    student_gender = obj.gender

    return HttpResponse('<h2> Student Number ' + str(student_id) + '</br>' + 'Name: '+ str(student_first_name) + ' ' + str(student_middle_name) + ' ' + str(student_last_name) + '</br>' + 'Course: ' + str(student_course) + '</br>' + 'Gender' + str(student_gender) +'</h2>' + '</br>' + '<a href="/list/"> Go back </a>')




