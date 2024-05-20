from django.shortcuts import render

# render the index page

def index(request):
    return render(request, './index.html')

