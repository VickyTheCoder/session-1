from django.shortcuts import render
from django.http import Http404

# Create your views here.
def homepage(request):
    if request.method == 'GET':
        return render(request=request,
                      template_name='index.html')
    raise Http404("Invalid Request")

