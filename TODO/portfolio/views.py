from django.shortcuts import render,redirect
from portfolio.models import contact
# Create your views here.
def index(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact.objects.create(
            Name=name,
            Email=email,
            message=message
        )
        return redirect('index')
    queryset = contact.objects.all()
    context = {
        'queryset': queryset
    }
        
    return render(request, 'portfolio/port.html',context)
