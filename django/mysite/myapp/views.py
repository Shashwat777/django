from django.shortcuts import render , render_to_response
from django.views.decorators.csrf import csrf_exempt
from  .models import contact2

# Create your views here.

def index2(request):

    return render_to_response('index2.html')
@csrf_exempt
def contact(request):
    if request.method=='POST':
        sub=request.POST.get('subject')
        email=request.POST.get('email')
        message=request.POST.get('message')
        c=contact2(email=email,subject=sub,message=message)
        c.save()

        return render(request,'contact.html')
    else:
        return render(request, 'contact.html')
def portfolio(request):

    return render_to_response('portfolio.html')
def about_me(request):

    return render_to_response('about_me.html')
