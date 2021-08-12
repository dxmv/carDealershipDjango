from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Car(models.Model):
    name=models.CharField(max_length=200)
    year=models.IntegerField()
    mileage=models.IntegerField()
    horse_power=models.IntegerField()
    city=models.CharField(max_length=50)
    seats=models.IntegerField()
    doors=models.IntegerField()
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.TextField()
    colors=[
        ("BL","Black"),
        ("RD","Red"),
        ("WH","White"),
        ("OT","Other"),
    ]
    color=models.CharField(max_length=2,choices=colors,default="BL")
    transmisions=[
        ("MA","Manual"),
        ("AU","Automatic"),
    ]

    transmision=models.CharField(max_length=2,choices=transmisions,default="MA")
    TYPE_CHOICES=[
        ("CP","Coupe"),
        ("HB","Hatchback"),
        ("CB","Cabrio"),
        ("SD","Sedan"),
        ("WG","Wagon"),
        ("SV","SUV"),
        ("VN","Van"),
    ]
    body_type=models.CharField(max_length=2,choices=TYPE_CHOICES,default="CP")
    FUEL_CHOICE=[
        ("DI","Diesel"),
        ("GA","Gasoline"),
        ("EL","Electric"),
        ("HY","Plug-in Hybrid"),
    ]
    fuel_type=models.CharField(max_length=2,choices=FUEL_CHOICE,default="DI")
    image=models.ImageField(upload_to="car_pics/")
    price=models.IntegerField()
    favourites=models.ManyToManyField(User,related_name="favourite")

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        SIZE=1620,1080
        if self.image:
            img=Image.open(self.image.path)
            img.thumbnail(SIZE)
            img.save(self.image.path)




