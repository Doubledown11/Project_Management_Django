from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Comment, Client, Entry, Task, Cost, Hour, project_priority, Employee
from .forms import CommentForm, EntryForm, EmployeeForm, ProjectForm, TaskForm, ClientForm, CostForm
from django.contrib.auth.decorators import login_required
import calendar
from calendar import HTMLCalendar
from datetime import datetime


# Create your views here.

#Views for extra pages
def index(request):
    """The home page for the project management app."""
    return render(request, 'project_app/index.html')

def cloud(request): 
    """The page where information on the AWS cloud is stored. 
    Essay
    Maybe diagrams
    """
    return render(request, 'project_app/cloud.html')


def cal(request, year, month): 
    """The page where the calendar for the application will be stored."""

    month = month.title() 
    # Convert month from name to number. 
    month_num = list(calendar.month_name).index(month)
    month_num = int(month_num)
    # Create calendar
    cal = HTMLCalendar().formatmonth(year, month_num)

    #Get current year 
    now = datetime.now()
    current_year = now.year

    #Get current time 
    time = now.strftime('%I:%M %p')

    return render(request, 
                'project_app/calendar.html', {
                'year':year, 
                'month': month, 
                "cal":cal,
                "current_year": current_year,
                'time': time, 
                })



#Views for Employees
@login_required
def employees(request): 
    """A page used to contain information about employee"""
    employee_list = Employee.objects.order_by('-emp_Fname')
    context = {'employees': employee_list}
    return render(request, 'project_app/employees.html', context)

def employee(request, emp_ID):
    """Show a single employee and their data."""
    employee_ = Employee.objects.get(id=emp_ID)
    context = {'employee': employee_}
    return render(request, 'project_app/employee.html', context)

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
            return redirect('project_app:employees')
        

    # Display a blank or invlaid form. 
    context = {'form': form}
    return render(request, 'project_app/new_employee.html', context)


def edit_employee(request, emp_ID):
    """Edit an existing entry."""
    employee = Employee.objects.get(id=emp_ID)    
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EmployeeForm(instance=employee)
    else:
        # POST data submitted; process data.
        form = EmployeeForm(instance=employee, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_app:employee', emp_ID=employee.id)    
    context = {'employee': employee, 'form': form}
    return render(request, 'project_app/edit_employee.html', context)






#Views for Projects
@login_required
def projects(request): 
    """Show projects from projects table"""
    project_list = Project.objects.order_by("project_name")
    context = {'projects' : project_list}
    return render(request, 'project_app/projects.html', context)


def project(request, project_ID): 
    """Show a single project and its entries"""
    project_ = Project.objects.get(id=project_ID)
    context = {'project': project_}
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


def edit_project(request, project_ID):
    """Edit an existing entry."""
    project = Project.objects.get(id=project_ID)    
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = ProjectForm(instance=project)
    else:
        # POST data submitted; process data.
        form = ProjectForm(instance=project, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_app:project', project_ID=project.id)    
    context = {'project': project, 'form': form}
    return render(request, 'project_app/edit_project.html', context)









#Views for Tasks
def tasks(request): 
    """A page used to contain information about employee"""
    task_list = Task.objects.order_by('task_name')
    context = {'tasks': task_list}
    return render(request, 'project_app/tasks.html', context)


def task(request, task_ID):
    """Show a single employee and their tasks."""
    task_ = Task.objects.get(id=task_ID)
    context = {'task': task_}
    return render(request, 'project_app/task.html', context)

def new_task(request): 
    """Adds a new Task"""
    if request.method != 'POST': 
        # No new data submitted. 
        form = TaskForm()
    else: 
        # POST (NEW) data submitted 
        form = TaskForm(data = request.POST)
        if form.is_valid(): 
            form.save() 
            return redirect('project_app:tasks')


    context = {'form': form}
    return render(request, 'project_app/new_task.html', context)


def edit_task(request, task_ID):
    """Edit an existing entry."""
    task = Task.objects.get(id=task_ID)    
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = TaskForm(instance=task)
    else:
        # POST data submitted; process data.
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_app:task', task_ID=task.id)    
    context = {'task': task, 'form': form}
    return render(request, 'project_app/edit_task.html', context)







#Views for costs
@login_required
def costs(request): 
    """Shows costs associated with projects"""
    cost_list = Cost.objects.order_by("name")
    context = {'costs': cost_list}
    return render(request, 'project_app/costs.html', context)


def cost(request, cost_ID):
    """Show a single employee and their tasks."""
    cost_ = Cost.objects.get(id=cost_ID)
    context = {'cost': cost_}
    return render(request, 'project_app/cost.html', context)

def new_cost(request): 
    """Adds a new Task"""
    if request.method != 'POST': 
        # No new data submitted. 
        form = CostForm() 
    else: 
        # POST (NEW) data submitted 
        form = CostForm(data = request.POST)
        if form.is_valid(): 
            form.save() 
            return redirect('project_app:costs')


    context = {'form': form}
    return render(request, 'project_app/new_cost.html', context)



def edit_cost(request, cost_ID):
    """Edit an existing entry."""
    cost = Cost.objects.get(id=cost_ID)    
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = CostForm(instance=cost)
    else:
        # POST data submitted; process data.
        form = CostForm(instance=cost, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_app:cost', cost_ID=cost.id)    
    context = {'cost': cost, 'form': form}
    return render(request, 'project_app/edit_cost.html', context)








#views for hours
def hours(request): 
    """Shows hours associated with employees. 
    Later will associate with projects, and include analytics."""

    hour_list = Hour.objects.order_by("work_completed")
    context = {'hours': hour_list}
    return render(request, 'project_app/hours.html', context)

def hour(request, hour_ID):
    """Show a single hour and their tasks."""
    cost_ = Hour.objects.get(id=hour_ID)
    context = {'costs': cost_}
    return render(request, 'project_app/hour.html', context)

def new_hour(request): 
    """Adds a new Task"""
    if request.method != 'POST': 
        # No new data submitted. 
        form = CostForm() 
    else: 
        # POST (NEW) data submitted 
        form = CostForm(data = request.POST)
        if form.is_valid(): 
            form.save() 
            return redirect('project_app:costs')


    context = {'form': form}
    return render(request, 'project_app/new_cost.html', context)





# Views for clients
@login_required
def clients(request): 
    """A page to be used for holding client information"""
    client_list = Client.objects.order_by("name")
    context = {'clients': client_list}
    return render(request, 'project_app/clients.html', context)

def client(request, client_ID): 
    """Show a single client and their information"""
    client_ = Client.objects.get(id=client_ID)
    context = {'client':client_}
    return render(request, 'project_app/client.html', context)

def new_client(request): 
    """Adds a new client"""
    if request.method != "POST": 
        # No new POST data submittede 
        form = ClientForm() 
    else: 
        # New (POST) data submitted. 
        form = ClientForm(data = request.POST)
        if form.is_valid(): 
            form.save() 
            return redirect('project_app:clients')


    context = {'form': form}
    return render(request, 'project_app/new_client.html', context)    


def edit_client(request, client_ID):
    """Edit an existing entry."""
    client = Client.objects.get(id=client_ID)    
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = ClientForm(instance=client)
    else:
        # POST data submitted; process data.
        form = ClientForm(instance=client, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_app:client', client_ID=client.id)    
    context = {'client': client, 'form': form}
    return render(request, 'project_app/edit_client.html', context)








 
# Views for comments
def comments(request): 
    """A page for comments to be added by the PM"""
    comment_list = Comment.objects.order_by('updated_date')
    context = {'comments' : comment_list}
    return render(request, 'project_app/comments.html', context)


def comment(request,comment_ID): 
    """Show a single comment, and its entry"""
    com = Comment.objects.get(id=comment_ID)
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


def edit_comment(request, comment_ID):
    """Edit an existing entry."""
    comment = Comment.objects.get(id=comment_ID)    
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = CommentForm(instance=comment)
    else:
        # POST data submitted; process data.
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_app:comment', comment_ID=comment.id)    
    context = {'comment': comment, 'form': form}
    return render(request, 'project_app/edit_comment.html', context)

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



