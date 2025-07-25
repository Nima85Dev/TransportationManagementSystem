from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ProfileModel(models.Model):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    ProfileImage = models.ImageField(upload_to="ProfileImages/", null=True, blank= True)

    Man = 1
    Woman = 2
    status_choices = (
        (Man, "Male"),
        (Woman, "Female"),
    )

    Gender = models.IntegerField(choices=status_choices, default=Man)  # default Male
    Credit = models.IntegerField(default=0)
