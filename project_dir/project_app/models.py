# Create your models here.
from django.db import models

# Must organize models.py such that the entities are input heirarchically.
# If the entities are written in the wrong sequeunce, a function which may 
# rely on another would result in a NameError.


class project_priority(models.Model): 
    """
    entity for the project with the current highest priority
    """ 

    current_priority = models.CharField(max_length=100, null=False, primary_key=True, unique=True)
    count_tot_project = models.IntegerField(null = False)
    #Counts the number of employees not currently assigned to a project. 
    employees_available = models.IntegerField(null = True)


# class project_status(models.Model): 
#     """ 
#     Entity for the status of the projects
#     """
#     status_id = models.IntegerField(null=False, primary_key=True, unique=True, default=1)
#     status_code = models.CharField(max_length=100, null=False)

     

class Client(models.Model): 
    """
    entity for the clients of the firm
    """
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, null=False)
    phone_no = models.IntegerField(null=True)
    email = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null = False)
    city = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=20)

   
class User(models.Model): 
    """
    entity for the various users of the system
    """
    id = models.AutoField(primary_key=True, unique=True)
    Fname = models.CharField(max_length=20, null = False)
    Lname = models.CharField(max_length=20, null=False)  



class Project(models.Model): 
    """
    Entity for projects. 
    """

    id = models.AutoField(primary_key=True, unique=True)
    project_name = models.CharField(max_length=100, null=True)
    start_date = models.DateField(auto_now_add=True)
    hourly_rate = models.IntegerField(null = True)
    pm_id = models.ForeignKey(User, on_delete=models.CASCADE)
    #status_code = models.ForeignKey(project_status, on_delete=models.CASCADE)
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE)


    #ADDING A SECTION FOR PROJECT_NAME 
    #IF NAME IS FOUND TO BE NULL, THEN THE PROJECT_NAME ATTRIBUTE WILL BE EQUAL TO 
    # ITS ID CONCATENATED TO THE 'PROJECT NAME'.
    @property 
    def display_name_or_name(self): 
        return self.project_name if self.project_name else "Project ID: " + self.project_ID

    def __str__(self): 
        #Returns a string representation of the model
        return self.text
    

class Task(models.Model): 
    """
    entity for the tasks.
    """

    id = models.AutoField( primary_key=True, unique=True)
    task_name = models.CharField(max_length=100, null=False)
    #status_id = models.ForeignKey(project_status, on_delete=models.CASCADE)
    #project_ID = models.ForeignKey(Project, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now=True)
    task_description = models.TextField(null = True)

    class Meta: 
        verbose_name_plural = 'emp_tasks'

    def __Str__(self): 
        """Returns a string representation of the object."""
        return f"{self.task_description[:50]}..."


class Employee(models.Model): 
    """
    entity for the various employees in the organization.
    """
    emp_Fname = models.CharField(max_length=100, null=True)
    id = models.AutoField(primary_key=True, default=1000)
    emp_Lname = models.CharField(max_length=100, null=True)
    emp_address = models.CharField(max_length=100, null=True)
    emp_phone = models.IntegerField(null = True)
    task_ID = models.ForeignKey(Task, on_delete=models.CASCADE, null = True)

    def __str__(self):
    # Return a string representation of the model
        return self.emp_Fname + ' ' + self.emp_Lnam



class Comment(models.Model): 
    """
    entity for additional comments

    accessed by only PM?
    """
    id = models.AutoField(primary_key=True, unique=True)
    body = models.CharField(max_length=1000)
    #task_ID = models.ForeignKey(tasks, on_delete=models.CASCADE)
    #submitted_by = models.ForeignKey(User, models.CASCADE)
    #Date needs to be updated each time the comment is accessed. 
    #auto_now = True should work
    updated_date = models.DateTimeField(auto_now=True)



# class teams(models.Model): 
#     """
#     entity for the various sub-teams which may have formed
#     """
#     team_id = models.IntegerField(null=False, primary_key=True, unique=True)
#     project_id = models.ForeignKey(projects, on_delete=models.CASCADE)
#     t_name = models.CharField(max_length=100, null=False)




class Hour(models.Model): 
    """
    entity used to represent the daily hour log
    """

    id = models.AutoField(primary_key=True, unique=True)
    date = models.DateField(max_length=50, auto_now_add=True)
    # make sure date functionality works for log in and log out. 
    start_time = models.DateTimeField(auto_now_add=True)
    # may remove the work completed and log in and out times from app.
    work_completed = models.CharField(max_length=1000, null=False)
    task_ID = models.ForeignKey(Task, on_delete=models.CASCADE)
    project_ID = models.ForeignKey(Project, on_delete=models.CASCADE)
    # maybe change users and employees to different tables. 
    employee_ID = models.ForeignKey(User, on_delete=models.CASCADE)




class Cost(models.Model): 
    """Entity allows tracking of the projct costs"""

    id = models.AutoField(primary_key=True, unique=True) 
    name = models.CharField(max_length=100, null=True)
    Price_per = models.IntegerField(null=False)
    quantity = models.IntegerField(null=False)
    tot_cost = models.IntegerField(null=False)
    project_ID = models.ForeignKey(Project, on_delete=models.CASCADE)



class Entry(models.Model): 
    """Allows the user to add 'entries' into the comment class."""

    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now=True)

    class Meta: 
        verbose_name_plural = 'myentries'

    def __str__(self): 
        """Returns a string representation of the model"""

        return f"{self.text[:50]}..."





















