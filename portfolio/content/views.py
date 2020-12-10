from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms

def content_index(request):
    if request.method == 'GET':
        form = forms.MessageForm()
        return render(request, 'content/index.html',{'forms':form})
    elif request.method == 'POST':
        form = forms.MessageForm(data=request.POST)
        if form.is_valid():
            form.save()
