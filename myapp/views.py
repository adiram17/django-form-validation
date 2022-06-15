from django.shortcuts import render, redirect
from .forms import PersonalForm 

def home(request):
    if request.method == "POST" :
        form = PersonalForm(request.POST)
        if form.is_valid():
            #valid
            return redirect('success')
        else:
            #invalid
            return render(request, 'home.html', { 'form' : form })
    else:
        form  = PersonalForm()
        return render(request, 'home.html', { 'form' : form })

def success(request):
    return render(request, 'success.html', {})
