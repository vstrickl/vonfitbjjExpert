from django.shortcuts import render

# Create your views here.
def quiz_i(request):

    header = 'Quiz Area'
    sub_header = 'Testing Development area for Vonfitbjj Quizzes!'
    body = 'This is where your quiz options would go.'

    context = {
        'header':header,
        'sub_header':sub_header,
        'body':body
    }
    
    return render(request, 'quizzes.html', context)