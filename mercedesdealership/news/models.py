from django.db import models
from django.contrib.auth.models import User
from PIL import Image
class News(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    date=models.DateField(auto_now_add=True)
    post=models.TextField()
    image=models.ImageField(upload_to="news_pics/")
    likes=models.ManyToManyField(User,related_name="likes")
    likes_number=models.IntegerField()
    def save(self,*args,**kwargs):
        super(News, self).save(*args, **kwargs)
        image=Image.open(self.image.path,"r")
        SIZE=1620,1080
        if image and image.width>1620 or image.height>1080:
            image.resize(SIZE)
            image.save(self.image.path)



