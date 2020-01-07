from django.shortcuts import render, redirect

from .models import *



def test(request):
    if request.method == 'POST':
        img = request.FILES.get('img-file')
        hello = Image.objects.create(img=img)
        
        imgs = Image.objects.all()
        print(imgs)
        context = {'object': imgs }
        return render(request, 'index.html', context)
    return render(request, 'index.html')