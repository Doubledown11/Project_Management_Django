from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Comment, Client, Entry, Task, Cost, Hour, project_priority, Employee
from .forms import CommentForm, EntryForm, EmployeeForm, ProjectForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    """The home page for the project management app."""
    return render(request, 'project_app/index.html')



