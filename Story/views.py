from django.http import JsonResponse

# Create your views here.
def set_session(request):
    status = 0
    print(request.POST.get('title',888))
    if request.method == 'POST':
        if 'title' in request.POST:
            status += 1
            request.session['title'] = request.POST.get('title')
        if 'story' in request.POST:
            status += 1
            request.session['story'] = request.POST.get('story')
    status = f"{status} parameter(s) updated" if status > 0 else "Zero parameters updated"
    return JsonResponse({'status': status})