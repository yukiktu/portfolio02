from django.shortcuts import render
from datetime import datetime

# Create your views here.
def top(request):
    timestamp = datetime.now().strftime('%Y.%m.%d %H:%M:%S')
    print(timestamp)
    print("talk>views.py")
    return render(request, 'top.html', dict(timestamp=timestamp))
