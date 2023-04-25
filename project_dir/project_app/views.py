from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Comment, Client, Entry, Task, Cost, Hour, Employee, Team, Event
from .forms import CommentForm, EntryForm, EmployeeForm, ProjectForm, TaskForm, ClientForm, CostForm, TeamForm, EventForm
from django.contrib.auth.decorators import login_required
import calendar
from calendar import HTMLCalendar
from datetime import datetime, date, timedelta
from django.urls import reverse


from io import BytesIO
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

from .utils import Calendar
from django.utils.safestring import mark_safe


# import matplotlib.pyplot as plt
import base64



# Create your views here.

# View and functions for calendar.
def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    
    ##### Seems to only return todays date regardless of button presses
    ### Next/prev month 
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('project_app:calendar'))
    return render(request, 'project_app/event.html', {'form': form})


class CalendarView(generic.ListView):
    model = Event
    template_name = 'project_app/calendar_.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)

        # Allows the user to change month to month on the calendar
        prev_month_ = prev_month(d)
        next_month_ = next_month(d)
        context['prev_month'] = prev_month_
        context['next_month'] = next_month_


        return context




#View for home page
def index(request):
    """The home page for the project management app."""
    return render(request, 'project_app/index.html')


#Views for Employees
@login_required
def employees(request): 
    """A page used to contain information about employee"""
    employee_list = Employee.objects.order_by('-emp_Fname')
    context = {'employees': employee_list}
    return render(request, 'project_app/employees.html', context)


@login_required
def employee(request, emp_ID):
    """Show a single employee and their data."""
    employee_ = Employee.objects.get(id=emp_ID)
    context = {'employee': employee_}
    return render(request, 'project_app/employee.html', context)


@login_required
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


@login_required
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





#Views for Teams
def teams(request): 
    """Show teams from projects table"""
    team_ = Team.objects.order_by("t_name")
    context = {'team' : team_}
    return render(request, 'project_app/teams.html', context)


def team(request, team_ID):
    """Show a single topic and its entries."""
    team_ = Team.objects.get(id=team_ID)
    context = {'team': team_}
    return render(request, 'project_app/team.html', context)


def new_team(request): 
    """Adds a new team"""
    if request.method != 'POST':
        # No new data submitted; create a blank form.
        form = TeamForm()
    else:
        # POST data submitted; process data.
        form = TeamForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_app:teams')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'project_app/new_team.html', context)


def edit_team(request, team_ID):
    """Edit an existing team."""
    team = Team.objects.get(id=team_ID)    
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = TeamForm(instance=project)
    else:
        # POST data submitted; process data.
        form = TeamForm(instance=project, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_app:team', team_ID=team.id)    
    context = {'team': team}
    return render(request, 'project_app/edit_team.html', context)





#Views for Projects
@login_required
def projects(request): 
    """Show projects from projects table"""
    project_list = Project.objects.order_by("project_name")
    context = {'projects' : project_list}
    return render(request, 'project_app/projects.html', context)


@login_required
def project(request, project_ID): 
    """Show a single project and its entries"""
    project_ = Project.objects.get(id=project_ID)
    context = {'project': project_}
    return render(request, 'project_app/project.html', context)


@login_required
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


@login_required
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
@login_required
def tasks(request): 
    """A page used to contain information about employee"""
    task_list = Task.objects.order_by('task_name')
    context = {'tasks': task_list}
    return render(request, 'project_app/tasks.html', context)


@login_required
def task(request, task_ID):
    """Show a single employee and their tasks."""
    task_ = Task.objects.get(id=task_ID)
    context = {'task': task_}
    return render(request, 'project_app/task.html', context)


@login_required
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


@login_required
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


@login_required
def cost(request, cost_ID):
    """Show a single employee and their tasks."""
    cost_ = Cost.objects.get(id=cost_ID)
    context = {'cost': cost_}
    return render(request, 'project_app/cost.html', context)


@login_required
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


@login_required
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
@login_required
def hours(request): 
    """Shows hours associated with employees. 
    Later will associate with projects, and include analytics."""

    hour_list = Hour.objects.order_by("work_completed")
    context = {'hours': hour_list}
    return render(request, 'project_app/hours.html', context)


@login_required
def hour(request, hour_ID):
    """Show a single hour and their tasks."""
    cost_ = Hour.objects.get(id=hour_ID)
    context = {'costs': cost_}
    return render(request, 'project_app/hour.html', context)


@login_required
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


@login_required
def client(request, client_ID): 
    """Show a single client and their information"""
    client_ = Client.objects.get(id=client_ID)
    context = {'client':client_}
    return render(request, 'project_app/client.html', context)


@login_required
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


@login_required
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
@login_required
def comments(request): 
    """A page for comments to be added by the PM"""
    comment_list = Comment.objects.order_by('updated_date')
    context = {'comments' : comment_list}
    return render(request, 'project_app/comments.html', context)


@login_required
def comment(request,comment_ID): 
    """Show a single comment, and its entry"""
    com = Comment.objects.get(id=comment_ID)
    entry = com.entry_set.order_by('-date_added')
    context = {'comment': com, 'entries': entry}
    return render(request, 'project_app/comment.html', context)


@login_required
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


@login_required
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


@login_required
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





# def plot(request):
#     x = [1, 2, 3, 4, 5]
#     y = [1, 4, 9, 16, 25]

#     fig, ax = plt.subplots()
#     ax.bar(x, y)

#     # Optional: chart title and label axes.
#     ax.set_title("Square Numbers", fontsize=24)
#     ax.set_xlabel("Value", fontsize=14)
#     ax.set_ylabel("Square of Value", fontsize=14)
    
#     # Create a bytes buffer for saving image
#     figbuffer = BytesIO()
#     plt.savefig(figbuffer, format='png', dpi=300)
#     image_base640=base64.b64encode(figbuffer.getvalue())
#     image_base64 = image_base640.decode('utf-8')
#     figbuffer.close()    
#     context={'image_base64':image_base64 }
#     return render(request,'project_app/plot.html',context)






##############Not fin
@login_required
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



