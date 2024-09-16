from django.http import JsonResponse
from Story.models import Content
# Create your views here.
def set_session(request):
    status = 0
    if request.method == 'POST':
        if 'title' in request.POST:
            status += 1
            request.session['title'] = request.POST.get('title')
        if 'story' in request.POST:
            status += 1
            request.session['story'] = request.POST.get('story')
    status = f"{status} parameter(s) updated" if status > 0 else "Zero parameters updated"
    return JsonResponse({'status': status})

def save(request):
    if request.method == 'POST':
        title = request.session.get('title')
        story = request.session.get('story')
        try:
            c = Content(title=title, story=story)
            1/0
            c.save()
        except Exception as e:
            status = "DB update failed"
            code = 500
            return JsonResponse({'error': status}, status=code)
        else:
            status = "Story updated"
            code = 200
    return JsonResponse({'status': status}, status=code)
