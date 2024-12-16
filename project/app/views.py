from django.shortcuts import render
from .models import Data
from django.db.models import Q
# Create your views here.



def index(request):
  if 'search' in request.GET:
    search = request.GET['search']
    multiple_search = Q(Q(f_name__icontains=search) | Q(l_name__icontains=search))
    data = Data.objects.filter(multiple_search)
  else:
    data = Data.objects.all()
  context = {'data':data}
  return render(request, 'main/index.html', context)

