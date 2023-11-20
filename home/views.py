from django.shortcuts import render

# Create your views here.
def home(request):

    header = 'Welcome to Your AI Expert'
    sub_header = 'Testing Development area for an Expert AI System for Vonfitbjj!'
    body = 'This is where the functionality of the code would go.'

    context = {
        'header':header,
        'sub_header':sub_header,
        'body':body
    }
    
    return render(request, 'home.html', context)