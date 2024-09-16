from django.shortcuts import render
from django.http import Http404
from django.middleware.csrf import get_token
# Create your views here.
def homepage(request):
    active_csrf_token = request.session.get('active_csrf_token', False)
    is_active = bool(active_csrf_token)
    if not is_active:
        csrf = get_token(request)
        request.session['active_csrf_token'] = csrf
    if request.method == 'GET':
        return render(request=request,
                      template_name='index.html',
                      context={
                                'is_active': is_active, 
                                'active_csrf_token': active_csrf_token 
                                }
                    )
    raise Http404("Invalid Request")

