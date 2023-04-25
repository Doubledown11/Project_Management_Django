from django.contrib import admin

# Register your models here.
from .models import Client, User, Project, Task, Employee, Comment, Hour, Cost, Entry, Team, Event
admin.site.register(Client)
admin.site.register(User)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Employee)
admin.site.register(Comment)
admin.site.register(Hour)
admin.site.register(Cost)
admin.site.register(Entry)
admin.site.register(Event)
admin.site.register(Team)




