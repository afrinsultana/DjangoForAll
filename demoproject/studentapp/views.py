from django.shortcuts import redirect, render
from studentapp.models import Student
from studentapp.forms import StudentForm

from django.core.paginator import Paginator

# Create your views here.
def home(request):
    context={'title':'Home'}
    return render(request,'home.html',context)


def index(request):
    std=Student.objects.order_by('-id')
    paginator=Paginator(std,8)
    page=request.GET.get('page')
    students=paginator.get_page(page)
    context={'students': students}
    return render(request,'studentapp/index.html',context)

def create_student(request):
    if request.method == "POST":
       form=StudentForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('index')
    else:
        form=StudentForm()

    context={'form':form}
    return render(request,'studentapp/create.html',context)

def edit_student(request,id):
    if request.method == "POST":
       student=Student.objects.get(pk=id)
       form=StudentForm(request.POST or None,instance=student)
       if form.is_valid():
           form.save()
           return redirect('index')
    else:
        student=Student.objects.get(pk=id)
        form=StudentForm(request.POST or None,instance=student)
        

    context={'form':form,'title':'edit'}
    return render(request,'studentapp/create.html',context)



