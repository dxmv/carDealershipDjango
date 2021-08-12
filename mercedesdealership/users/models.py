from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Custom user profile model with phone number field and city field.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone_regex=RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(validators=[phone_regex], max_length=16)
    city=models.CharField(max_length=200)


    def __str__(self):
        return self.user.username
