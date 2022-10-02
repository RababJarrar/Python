from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['fname']) < 2:
            errors["fname"] = "first name should be at least 2 characters"
        if len(postData['lname']) < 2:
            errors["lname"] = "last name should be at least 2 characters"
        if len(postData['pass1']) < 8:
            errors["pass1"] = "Password should be at least 8 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if postData['pass1'] != postData['pass2']:
            errors["pass2"] = "Please ensure your password matches the confirmation!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

