from django.shortcuts import render, redirect
from ..login_app.models import User

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def dashboard(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect("/login")
    user = User.objects.get(id = request.session['user_id'])
    context = {
    'user': user,
    }
    return render(request, 'main/dashboard.html', context)
