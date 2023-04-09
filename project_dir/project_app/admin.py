from django.contrib import admin

# Register your models here.
from .models import project_priority, Client, User, Project, Task, Employee, Comment, Hour, Cost, Entry 
admin.site.register(project_priority)
admin.site.register(Client)
admin.site.register(User)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Employee)
admin.site.register(Comment)
admin.site.register(Hour)
admin.site.register(Cost)
admin.site.register(Entry)


