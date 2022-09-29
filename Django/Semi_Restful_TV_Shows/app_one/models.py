from django.db import models


class ShowManager(models.Manager):
        def basic_validator(self, postData):
            errors = {}
            # add keys and values to errors dictionary for each invalid field
            if len(postData['title']) <2:
                errors["title"] = "Title should be at least 2 characters"
            if len(postData['network']) < 3:
                errors["network"] = "Network should be at least 2 characters"
            if len(postData['desc']) < 10:
                errors["desc"] = "Network should be at least 10 characters"
            return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description=models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    objects=ShowManager()
    


