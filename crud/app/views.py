from django.shortcuts import render
from django.urls import is_valid_path
from .import forms
from .models import Student

# Create your views here.
def index(request):
    student_list = Student.objects.order_by("first_name")
    diction = {'title':"Index", 'student_list': student_list}
    return render(request, 'app/index.html', context=diction)

def student_form(request):
    form = forms.StudentForm()

    if request.method == "POST":
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction = {'title' : "Student Form", "Student_form" : form}
    return render(request, 'app/student_form.html', context=diction)

def student_info(request,student_id):
    student_info = Student.objects.get(pk=student_id)
    diction = {'student_info':student_info}
    return render(request, 'app/student_info.html', context=diction)


def student_update(request,student_id):
    student_info = Student.objects.get(pk=student_id)
    form = forms.StudentForm(instance=student_info)

    if request.method == "POST":
        form = forms.StudentForm(request.POST, instance=student_info)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction = {'students_form':form}
    return render(request,'app/student_update.html', context=diction)

def student_delete(request,student_id):
    student = Student.objects.get(pk=student_id).delete()
    diction = {'delete_message': "Delete Done"}
    return render(request, 'app/student_delete.html', context=diction)