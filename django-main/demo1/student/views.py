from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm  # Assuming you have a form for Student

# View to list all students
def student_list(request):
    students = Student.objects.all()  # Fetch all students from the database
    return render(request, 'students/student_list.html', {'students': students})

# View to add a new student
def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect to the student list after saving
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

# View to edit an existing student
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)  # Get the student by primary key
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form=StudentForm(request.POST,instance=student)
            if form.is_valid():

              form.save()
              return redirect('student_list')  # Redirect to the student list after saving
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})

# View to delete a student
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)  # Get the student by primary key
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')  # Redirect to the student list after deletion
    return render(request, 'students/student_confirm_delete.html', {'student': student}) 
