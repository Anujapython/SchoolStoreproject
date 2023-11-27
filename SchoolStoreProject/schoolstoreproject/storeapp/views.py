from django.contrib import messages, auth
from django.http import HttpResponse
from .models import logins, register, Course, Person
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PersonCreationForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def login1(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        s=logins(username=username,password=password)
        s.save()
        return redirect('/login')
    return render(request,'login.html')

def register1(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']
        p=register(username=username,password=password,password1=password1)
        p.save()
        return redirect('/new')
    return render(request,'register.html')

def new(request):
    form=PersonCreationForm()
    if request.method == 'POST':
        return redirect('/add')
    return render(request,'new.html',{'form':form})

def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        return redirect('/new3')
    return render(request, 'form.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        form.save()
        return redirect('/')
    return render(request, 'form.html', {'form': form})

# AJAX
def load_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).all()
    return render(request, 'course_options.html', {'courses': courses})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

def new3(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        return redirect('/')
    return render(request, 'new3.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('/')