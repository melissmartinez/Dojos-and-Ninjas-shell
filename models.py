from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    stacks = models.CharField(max_length=150)
    amount_cost = models.IntegerField()
    desc = models.TextField("old dojo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # def __repr__(self):
    #     return f"<Dojo object: {self.name} {self.state} {self.stack} {self.amount_cost}>"

class Ninja(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    any_experience = models.BooleanField()
    dojo = models.ForeignKey(Dojo, related_name='ninjas', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # def __repr__(self):
    #     return f"<Dojo object: {self.first_name} {self.last_name} {self.any_experience} {self.dojo}>"

