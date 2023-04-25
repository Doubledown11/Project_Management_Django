#project_app/forms.py

from django import forms
from .models import Comment, Entry, Task, Employee, Project, Client, Cost, Team, Hour, Event 
from django.forms import ModelForm, DateInput


#  A form for the input required for the commenting functionality.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        labels = {'body': 'Enter text'}


#  A form for the input required for the commenting functionality.
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry 
        fields = ['text']
        labels = {'text':'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}


#  A form for the input required for employee class related functionality.
class EmployeeForm(forms.ModelForm):
    class Meta: 
        model = Employee 
        fields = ['emp_Fname', 'emp_Lname', 'emp_address', 'emp_phone', 'task_ID']
        labels = ['Employee First Name', 'Employee Last Name', 'Employee Phone Number', 'Assigned Task']


#  A form for the input required for project class related functionality.
class ProjectForm(forms.ModelForm): 
    class Meta: 
        model = Project
        fields = ['project_name', 'client_name']
        labels = ['Project Name', 'Client Name']


#  A form for the input required for employee task related functionality.
class TaskForm(forms.ModelForm): 
    class Meta: 
        model = Task 
        fields = ['task_name', 'task_description']
        labels = ['Enter Name of Task', 'Description of Task']


#  A form for the input required for client class related functionality.
class ClientForm(forms.ModelForm): 
    class Meta: 
        model = Client 
        fields = ['name', 'phone_no', 'email', 'address', 'city', 'province', 'postal_code']
        labels = ['Enter Client Name', 'Phone Number', 'Email', 'Address', 'City', 'Province', 'Postal Code']


#  A form for the input required for cost class related functionality.
class CostForm(forms.ModelForm):
    class Meta: 
        model = Cost 
        fields = ['name', 'Price_per', 'quantity', 'tot_cost', 'project_ID']
        labels = {'Enter Cost Name', 'Cost per Unit','How many (qty)', 'Total Cost', 'ID of relevant project'}


#  A form for the input required for cost class related functionality.
class TeamForm(forms.ModelForm):
    class Meta: 
        model = Team 
        fields = ['project_id', 't_name','status']
        labels = {'Enter project ID', 'Team Name','Status'}


# A form for the creation of events in our calendar.
# Currently non-operational.
class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)
