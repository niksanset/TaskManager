from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    priority = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True)
    status = models.CharField(max_length=255,blank=True)
    completed_at = models.DateTimeField(blank=True)
    image = models.ImageField(blank=True)


    def __str__(self):
        return f"{self.title}"


class ActionType(models.Model):
    action_name = models.CharField(max_length=255)
    

    def __str__(self):
        return f"{self.action_name}"


class Actions(models.Model):
    action = models.ForeignKey(ActionType, on_delete = models.CASCADE)
    made_at = models.DateTimeField(blank=True)


    def __str__(self):
        return f"{self.action}"
