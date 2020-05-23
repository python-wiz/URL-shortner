from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import integrator
import re


def sanitize(request, inp):
    if re.search('[\'"?\\#-]', inp):
        return True
    else:
        return False
    raise ValueError

# Create your views here.
def home(request):
    return render(request, 'main/index.html')

def cust(request,id_=''):
  if 'go' == str(id_):
    return redirect('https://www.google.com/')
  elif 'yo' == str(id_):
    return redirect('https://www.youtube.com/')
  else:
    return HttpResponse('Not found')


def short(request):
  url = request.GET.get('main_url')
  short = request.GET.get('short')
  
  #sanitize
  t=False
  t=sanitize(request,url)
  t2=sanitize(request,short)
  if t or t2:
    return render(request, 'main/index.html', {'err':'Sorry, but we don\'t support \' " ? \\ # - till now'})
  
  In = integrator()
  sh,msg = In.insert(url,short)
  if sh:
    return render(request, 'main/success_pg.html', {'res': sh, 'domain': request.get_host()} )
  else:
    return render(request, 'main/index.html', {'err':'Please try again.\n'+msg})
    #return HttpResponse('Error occured, try again pls')

def red(request,sh):
  In =integrator()
  t=False
  t=sanitize(request, sh)
  if t:
    return render(request, 'main/index.html', {'err':'Sorry, but we don\'t support \' " ? \\ # - till now'})
  url=In.find(sh)
  if url:
    print('red')
    return redirect(url)
  else:
    return render(request, 'main/index.html', {'err':'Something went wrong, please try again'})