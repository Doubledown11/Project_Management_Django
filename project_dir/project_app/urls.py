from django.urls import path, include 
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'project_app'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    #paths for projects
    path('projects/', views.projects, name='projects'),
    path('projects/<int:project_ID>', views.project, name='project'),
    path('new_project/', views.new_project, name='new_project'),
    path('edit_project/<int:project_ID>/', views.edit_project, name='edit_project'),

    #paths for employees
    path('employees/', views.employees, name='employees'),
    path('employees/<int:emp_ID>', views.employee, name='employee'),
    path('new_employee/', views.new_employee, name='new_employee'),
    path('edit_employee/<int:emp_ID>/', views.edit_employee, name='edit_employee'),


    #paths for clients
    path('clients/', views.clients, name='clients'),
    path('client/<int:client_ID>', views.client, name = 'client'),
    path('new_client/', views.new_client, name='new_client'),
    path('edit_client/<int:client_ID>/', views.edit_client, name='edit_client'),

    #paths for costs
    path('costs/', views.costs, name='costs'),
    path('costs/<int:cost_ID>', views.cost, name='cost'),
    path('new_cost/', views.new_cost, name='new_cost'),
    path('edit_cost/<int:cost_ID>/', views.edit_cost, name='edit_cost'),


    #paths for tasks
    path('tasks/', views.tasks, name='tasks'),
    path('task/<int:task_ID>', views.task, name='task'),
    path('new_task/', views.new_task, name='new_task'),
    path('edit_task/<int:task_ID>/', views.edit_task, name='edit_task'),


    #Paths for comments
    path('comments/', views.comments, name='comments'),
    path('comment/<int:comment_ID>', views.comment, name='comment'),
    path('new_comment/', views.new_comment, name='new_comment'),
    path('edit_comment/<int:comment_ID>/', views.edit_comment, name='edit_comment'),

    

    #Paths for extra pages
    path('cloud/', views.cloud, name="cloud"),

    #Path for calendar
    path('cal/<int:year>/<str:month>/', views.cal, name = 'cal'),
   



    #paths for hours 
    # path('hours/', views.hours, name='hours'),
    # path('hours/<int:cost_id>', views.hour, name='hour'),
    # path('new_cost/', views.new_hour, name='new_hour'),
    # Will have to go through and include FK data in the templates associated with hours. 
    # Needed for analytics information. 
]



urlpatterns += staticfiles_urlpatterns()