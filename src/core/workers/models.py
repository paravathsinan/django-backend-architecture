from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    category = models.ForeignKey("Category", on_delete = models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    