from __future__ import unicode_literals

from django.db import models
import re,bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
# Create your models here.
class UserManager (models.Manager):
    def valid_registration (self,postData):
        errors = []
        if len(postData['first_name']) < 1:
            errors.append ("Your first name should be more than 1 character long")
        if not NAME_REGEX.match(postData['first_name']):
            errors.append ('Your first name must not contain numbers.')
        if len(postData['last_name']) < 1:
            errors.append ("Your last name should be more than 1 character long")
        if not NAME_REGEX.match(postData['last_name']):
            errors.append ('Your last name must not contain numbers.')
        if len(postData['password']) < 8:
            errors.append ("Your Password must be at least 9 characters long")
        if not EMAIL_REGEX.match(postData['email']):
            errors.append ('Please enter a valid email address.')
        if User.objects.filter(email = postData['email']):
            errors.append ('This email is already in use. Please log in instead.')
        if not postData['password'] == postData['pwd_confirm']:
            errors.append ('The password and password confirmation must match')
        return errors

    def valid_login (self,postData):
        errors =[]
        if not EMAIL_REGEX.match(postData['email']):
            errors.append ('Please enter a valid email address.')
        if len(postData['password']) < 8:
            errors.append ("Your Password must be at least 9 characters long")
        try:
            user = User.objects.get(email = postData['email'])
            if bcrypt.checkpw(postData['password'].encode(),user.password.encode()):
                return errors
            errors.append("The password does not match.")
        except User.DoesNotExist:
            errors.append("The email address does not match our database, please register instead.")
        return errors


class User (models.Model):
    first_name = models.CharField (max_length = 255)
    last_name = models.CharField (max_length = 255)
    email = models.EmailField (max_length = 255)
    password = models.CharField (max_length = 255)
    created_at = models.DateTimeField (auto_now_add = True)
    updated_at = models.DateTimeField (auto_now = True)
    objects = UserManager()

    def __str__(self):
        return self.first_name

class Book (models.Model):
    name = models.CharField (max_length = 255)
    author = models.CharField (max_length = 255)
    created_at = models.DateTimeField (auto_now_add = True)
    updated_at = models.DateTimeField (auto_now = True)

    def __str__(self):
        return self.name

class Review (models.Model):
    comment = models.TextField ()
    rating = models.IntegerField ()
    reviews = models.ForeignKey (Book, related_name = 'books')
    reviewed_by = models.ForeignKey (User, related_name = 'reviewer')
    created_at = models.DateTimeField (auto_now_add = True)
    updated_at = models.DateTimeField (auto_now = True)