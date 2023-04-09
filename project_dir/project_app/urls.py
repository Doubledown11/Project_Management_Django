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

    #paths for employees
    path('employees/', views.employees, name='employees'),
    path('employees/<int:product_id>', views.employee, name='employee'),
    path('new_employee/', views.new_employee, name='new_employee'),

    #paths for clients
    path('clients/', views.clients, name='clients'),
    path('clients/<int:client_id>', views.client, name = 'client'),
    path('new_client', views.new_client, name='new_client'),

    #paths for costs
    path('costs/', views.costs, name='costs'),
    path('costs/<int:cost_id>', views.cost, name='cost'),
    path('new_cost/', views.new_cost, name='new_cost'),

    #Bug with tasks page, wont display bootstrap, database fields?
    path('tasks/', views.tasks, name='tasks'),
    path('task/<int:task_ID>', views.task, name='task'),
    path('new_task/', views.new_task, name='new_task'),


    #Paths for comments
    path('comments/', views.comments, name='comments'),
    path('comments/<int:comment_ID>', views.comment, name='comment'),
    path('new_comment/', views.new_comment, name='new_comment'),

    path('new_entry/<int:comment_ID>', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),


    #Paths for extra pages
    path('cloud/', views.cloud, name="cloud"),




    #paths for hours 
    # path('hours/', views.hours, name='hours'),
    # path('hours/<int:cost_id>', views.hour, name='hour'),
    # path('new_cost/', views.new_hour, name='new_hour'),
    # Will have to go through and include FK data in the templates associated with hours. 
    # Needed for analytics information. 
]



urlpatterns += staticfiles_urlpatterns()