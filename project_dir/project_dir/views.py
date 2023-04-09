from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Comment, Client, Entry, Task, Cost, Hour, project_priority, Employee
from .forms import CommentForm, EntryForm, EmployeeForm, ProjectForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    """The home page for the project management app."""
    return render(request, 'project_app/index.html')



def projects(request): 
    """Show projects from projects table"""
    project_list = Project.objects.order_by("project_name")
    context = {'projects' : project_list}
    return render(request, 'project_app/projects.html', context)

def project(request, project_ID): 
    """Show a single project and its entries"""
    project_ = Project.objects.get(id=project_ID)
    context = {'projects': project_}
    return render(request, 'project_app/project.html', context)

def new_project(request): 
    """Adds a new project"""
    if request.method != 'POST':
        # No new data submitted; create a blank form.
        form = ProjectForm()
    else:
        # POST data submitted; process data.
        form = ProjectForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_app:projects')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'project_app/new_project.html', context)










def costs(request): 
    """Shows costs associated with projects"""
    cost_list = Cost.objects.order_by("cost_ID")
    context = {'costs': cost_list}
    return render(request, 'project_app/costs.html', context)

def hours(request): 
    """Shows hours associated with employees. 
    Later will associate with projects, and include analytics."""
    hour_list = Cost.objects.order_by("cost_ID")
    context = {'hours': hour_list}
    return render(request, 'project_app/hours.html', context)

def comments(request): 
    """A page for comments to be added by the PM"""
    comment_list = Comment.objects.order_by('updated_date')
    context = {'comments' : comment_list}
    return render(request, 'project_app/comments.html', context)


def clients(request): 
    """A page to be used for holding client information"""
    client_list = Client.objects.order_by("client_ID")
    context = {'clients': client_list}
    return render(request, 'project_app/clients.html', context)



def tasks(request): 
    """A page used to contain information about employee"""
    task_list = Task.objects.order_by('-task_ID')
    context = {'tasks': task_list}
    return render(request, 'project_app/emp_tasks.html', context)


#def task(request, task_ID):
    """Show a single employee and their tasks."""
    employee = Employee.objects.get(task_ID=task_ID)
    emp_tasks = employee.task_Set.order_by('-date_added')
    context = {'employees': employee, 'tasks': emp_tasks}
    return render(request, 'project_app/task.html', context)
 




def employees(request): 
    """A page used to contain information about employee"""
    employee_list = Employee.objects.order_by('-emp_Fname')
    context = {'employees': employee_list}
    return render(request, 'project_app/employees.html', context)


def employee(request, emp_ID):
    """Show a single employee and their data."""
    employee_ = Employee.objects.get(id=emp_ID)
    context = {'employees': employee_}
    return render(request, 'project_app/employee.html', context)

def new_employee(request): 
    """Adds a new employee"""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EmployeeForm()
    else:
        # POST data submitted; process data.
        form = EmployeeForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_app:employees')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'project_app/new_employee.html', context)







def comment(request,comment_ID): 
    """Show a single comment, and its entry"""
    com = Comment.objects.get(comment_ID=comment_ID)
    entry = com.entry_set.order_by('-date_added')
    context = {'comment': com, 'entries': entry}
    return render(request, 'project_app/comment.html', context)


def new_comment(request): 
    """Add a new comment."""
    if request.method != 'POST': 
        # No data submitted, create a blank form.
        form = CommentForm() 

    else: 
        # POST data submitted; process data. 
        form = CommentForm(data = request.POST)
        if form.is_valid(): 
            form.save() 
            return redirect('project_app:comments')
        

    # Display a blank or invlaid form. 
    context = {'form': form}
    return render(request, 'project_app/new_comment.html', context)



def new_entry(request, comment_ID):
    """Add a new entry for a particular comment."""
    comment = Comment.objects.get(comment_ID= comment_ID)
    
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.comment = comment
            new_entry.save()
            return redirect('project_app:comment', comment_ID=comment_ID)
               
    # Display a blank or invalid form.
    context = {'comment': comment, 'form': form}
    return render(request, 'project_app/new_entry.html', context)


##############Not fin

def edit_entry(request, entry_id):
    """Edit an existing entry."""

    entry = Entry.objects.get(id = entry_id)
    comment = entry.comment    
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_app:comment', comment_ID=Comment.comment_ID)    
    context = {'entry': entry, 'comment': comment, 'form': form}
    return render(request, 'project_app/edit_entry.html', context)


def new_employee(request): 
    """Adds a new employee"""

    if request.method != 'POST': 
        # No data submitted, create a blank form.
        form = EmployeeForm() 

    else: 
        # POST data submitted; process data. 
        form = EmployeeForm(data = request.POST)
        if form.is_valid(): 
            form.save() 
            return redirect('project_app:employee')
        

    # Display a blank or invlaid form. 
    context = {'form': form}
    return render(request, 'project_app/new_employee.html', context)


