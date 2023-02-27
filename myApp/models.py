from django.db import models

# Create your models here.

class Transalations(models.Model):
    language = models.CharField(max_length=200, default="")
    family_type = models.CharField(max_length=200, default="")
    description = models.TextField()

    def __str__(self) -> str:
        return self.language

class ProgressStatesTransalation(models.Model):
    language = models.CharField(max_length=200, default="")
    description = models.TextField(default="") 

    def __str__(self) -> str:
        return self.language



class FamilyType(models.Model):
    f_specifications = models.ManyToManyField(Transalations)


class ProgressState(models.Model):
    specifications = models.ManyToManyField(ProgressStatesTransalation)
    state_name = models.CharField(max_length=200, default="")

    def __str__(self) -> str:
        return self.state_name


class Offer(models.Model):
    offer_name = models.CharField(max_length=200, default="", null=True, blank=True)
    calculation = models.CharField(max_length=200, default="")
    low = models.IntegerField(default=0)
    high = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.offer_name



class Family(models.Model):
    initial1 = models.CharField(max_length=200, default="")
    initial2 = models.CharField(max_length=200, default="")
    name = models.CharField(max_length=200, default="")
    family_type = models.ForeignKey(FamilyType, on_delete=models.CASCADE)
    family_area = models.FloatField()
    progress_state = models.ForeignKey(ProgressState, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    

class Notification(models.Model):
    fcm_token = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.fcm_token
