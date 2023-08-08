from django.db import models

class wgshare(models.Model):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField()
    details = models.CharField("Details", max_length=1024)
    cost = models.CharField(max_length=20)
    registrationDate = models.DateField("Registration Date", auto_now_add=True)

    def __str__(self):
        return self.name
    

