import os

from clips import Environment
from django.shortcuts import render


# Create your views here.
def home(request):

    header = 'Welcome to Your AI Expert'
    sub_header = 'Testing Development area for an Expert AI System for Vonfitbjj!'
    body = 'This is where the functionality of the code would go.'

    # Create a CLIPS environment
    environment = Environment()

    # Load and run the CLIPS environment
    module_dir = os.path.dirname(__file__)
    clips_file = os.path.join(module_dir, 'rules.clp')
    environment.load(clips_file)

    # Run the CLIPS environment
    environment.run()

    # Retrieve message facts from CLIPS
    messages = [fact['text'] for fact in environment.facts() if fact.template.name == "message"]

    # Join messages into a single string
    body = '\n'.join(messages)

    context = {
        'header':header,
        'sub_header':sub_header,
        'body':body
    }
    
    return render(request, 'home.html', context)