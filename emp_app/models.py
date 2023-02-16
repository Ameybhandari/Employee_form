from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    
    def __str__(self):
        return "%s" %(self.name)

class Role(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class Employee(models.Model):

    # cascade = when the parent is deleted the child object is also deleted 

    # Suppose a post has comments; when the Post is deleted, all the comments on that Post 
    # will automatically delete. We don't want a comment saving in the database when the 
    # associated Post is deleted.


    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    
    def __str__(self):
        #return "%s %s %s %s %s %s %s" %(self.first_name, self.last_name, self.salary, self.bonus, self.dept, self.role, self.phone)
        return "%s %s %s" %(self.first_name, self.last_name, self.role)

