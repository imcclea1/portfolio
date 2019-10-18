from django.shortcuts import render

# Create your views here.
from .models import Job
def home(request):
    jobs = Job.objects #this is how you get all of the jobs from the database
    return render(request, 'jobs/home.html', {'jobs': jobs})