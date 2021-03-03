from django.contrib.auth import authenticate, login as djangologin,logout as djangologout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.




def login (request):
#-----------------------------------------
# este metodo verifica se esta auth = request.user.is_authenticated()

    next = request.GET.get('next')
    if request.method != 'POST':
        return render(request,'gos/paginas/login1.html',{'next':next})
    username = request.POST.get('username')
    password = request.POST.get('password')
    next     = request.POST.get('next')
    user = authenticate(username=username,password =password)
    if user:  #reforçar futuramente a segurança
        djangologin(request,user)
        if next:
            #return HttpResponse('algo')
            return HttpResponseRedirect(next)
        return HttpResponseRedirect('/admin/')
    if not user:
        falha = True
        return render(request,'gos/paginas/login1.html',{'falha':falha})