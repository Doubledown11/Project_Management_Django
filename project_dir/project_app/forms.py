#project_app/forms.py

from django import forms
from .models import Comment, Entry, Task, Employee, Project, Client, Cost, Hour

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        labels = {'body': 'Enter text'}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry 
        fields = ['text']
        labels = {'text':'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}


class EmployeeForm(forms.ModelForm):
    class Meta: 
        model = Employee 
        fields = ['emp_Fname', 'emp_Lname', 'emp_address', 'emp_phone', 'task_ID']
        labels = ['Employee First Name', 'Employee Last Name', 'Employee Phone Number', 'Assigned Task']


class ProjectForm(forms.ModelForm): 
    class Meta: 
        model = Project
        fields = ['project_name', 'client_name']
        labels = ['Project Name', 'Client Name']


class TaskForm(forms.ModelForm): 
    class Meta: 
        model = Task 
        fields = ['task_name', 'task_description']
        labels = ['Enter Name of Task', 'Description of Task']


class ClientForm(forms.ModelForm): 
    class Meta: 
        model = Client 
        fields = ['name', 'phone_no', 'email', 'address', 'city', 'province', 'postal_code']
        labels = ['Enter Client Name', 'Phone Number', 'Email', 'Address', 'City', 'Province', 'Postal Code']


class CostForm(forms.ModelForm):
    class Meta: 
        model = Cost 
        fields = ['name', 'Price_per', 'quantity', 'tot_cost', 'project_ID']
        labels = {'Enter Cost Name', 'Cost per Unit','How many (qty)', 'Total Cost', 'ID of relevant project'}