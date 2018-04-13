from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager): #validator class
    def basic_validator(self, postData):
        errors = []
        if len(postData['name']) < 5:
            errors.append ("Course name should be more than 5 characters")
        if len(postData['description']) < 15:
            errors.append ("Course description should be more than 15 characters")
        return errors

class Course(models.Model):
    name = models.CharField (max_length = 255)
    desc = models.TextField ()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager() # associating the validator

    def __str__(self):
        return self.name
