from django.shortcuts import render

# Create your views here.

def signupfunc(request):
    if request.method == 'POST':
        print('this is post method')
    else:
        print('this is not post method')
    return render(request, "signup.html", {'some':100})
