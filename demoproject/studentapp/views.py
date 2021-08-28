from django.shortcuts import redirect, render
from studentapp.models import student
from studentapp.forms import StudentForm

from django.core.paginator import Paginator

# Create your views here.
def home(request):
    context={'title':'Home'}
    return render(request,'home.html',context)


def index(request):
    std=student.objects.order_by('-id')
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



