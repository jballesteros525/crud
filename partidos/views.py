from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import PartidosForm
from .models import Partidos
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def singup(request):

    if request.method =='GET':
        return render(request,'singup.html',{
        'form':UserCreationForm
        })
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('partidos')
            except IntegrityError:
                return render(request,'singup.html',{
                    'form': UserCreationForm,
                    "error":'User alredy exists'
                })
            return render(request,'singup.html',{
                'form':UserCreationForm,
                "error":'Password do no match'
            })                
@login_required
def partidos(request):
    partidos = Partidos.objects.filter(user=request.user, datacompleted__isnull=True)
    return render(request,'partidos.html', {'partidos':partidos})
@login_required
def partidos_completed(request):
    partidos = Partidos.objects.filter(user=request.user, datacompleted__isnull=False)
    return render(request,'partidos.html', {'partidos':partidos})
@login_required
def create_partidos(request):
    if request.method =='GET':
        return render(request, 'create_partidos.html',{
        'form':PartidosForm
    })
    else:
        try:
            form = PartidosForm(request.POST)
            new_Partidos = form.save(commit=False)
            new_Partidos.user = request.user
            new_Partidos.save()        
            return redirect('partidos')
        except ValueError:
            return render(request,'create_partidos.html',{
                'form':PartidosForm,
                'error': 'Please provide valid date'
            })

@login_required
def complete_partidos(request, partidos_id):
    partidos = get_object_or_404(Partidos, pk=partidos_id, user=request.user)
    if request.method =='POST':
        partidos.datecompleted = timezone.now()
        partidos.save()
        return redirect('partidos')

@login_required
def delete_partidos(request, partidos_id):
    partidos = get_object_or_404(Partidos, pk=partidos_id, user=request.user)
    if request.method =='POST':      
        partidos.delete()
        return redirect('partidos')

@login_required
def partidos_detail(request, partidos_id):
    if request.method == 'GET':
        partidos = get_object_or_404(Partidos, pk=partidos_id, user=request.user)
        form = PartidosForm(instance=partidos)
        return render(request, 'partidos_detail.html',{'partidos':partidos, 'form':form})
    else:
        try:
            partidos = get_object_or_404(Partidos, pk=partidos_id, user=request.user)
            form = PartidosForm(request.POST, instance=partidos)
            form.save()
            return redirect('partidos')
        except ValueError:
            return render(request, 'partidos_detail.html',{'partidos':partidos, 'form':form, 'error':"Error updating partidos"})   

@login_required
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method=='GET':
        return render(request, 'signin.html',{
        'form':AuthenticationForm
    })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
    if user is None:    
        return render(request, 'signin.html',{
        'form':AuthenticationForm,
        'error':'Username or password is incorrect'
    })
    else:
        login(request, user)
        return redirect('partidos')


