from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    stacks = models.CharField(max_length=150)
    amount_cost = models.IntegerField()
    desc = models.TextField("old dojo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Ninja(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    any_experience = models.BooleanField()
    dojo = models.ForeignKey(Dojo, related_name='ninjas', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
