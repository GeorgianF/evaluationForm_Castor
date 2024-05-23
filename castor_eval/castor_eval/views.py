from django.shortcuts import render

# render the dashboard page
def dashboard(request):
    return render(request, 'dashboard.html')