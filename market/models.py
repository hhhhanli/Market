from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=32,unique=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    height = models.PositiveIntegerField(default="30",blank=True,null=True,editable=False)
    width = models.PositiveIntegerField(default="30",blank=True,null=True,editable=False)
    # picture_url = models.CharField(default="http://ershou.u.qiniudn.com/Android_1480732854630_186265.jpg?imageView2/5/w/800/h/800",max_length=128,blank=True)
    avatar = models.ImageField(upload_to='profile',default="profile/default.png",height_field='height',width_field='width',blank=True)

    is_manager = models.BooleanField(default=False)
    grade = models.CharField(blank=True,max_length=4)
    campus = models.CharField(blank=True,max_length=20)

    def __str__(self):
        return self.user.username


class Goods(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512,blank=True)
    trade_location = models.CharField(max_length=32)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    picture_url = models.CharField(default="/market/media/profile/default.png",max_length=128,blank=True)
    picture = models.ImageField(upload_to='goods',blank=True,null=True)
    seller = models.ForeignKey(UserProfile,blank=True,null=True,on_delete=models.CASCADE)
    discount = models.IntegerField(default=0,blank=True)
    goods_phone = models.IntegerField(null=True,blank=True)
    goods_qq = models.IntegerField(null=True,blank=True)
    publish_time = models.DateField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    goods = models.ForeignKey(Goods,blank=True,null=True,on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile,blank=True,null=True,on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    comment_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content


class InstationMessage(models.Model):
    receiver = models.ForeignKey(UserProfile, related_name='receiver_id',on_delete=models.CASCADE)
    sender = models.ForeignKey(UserProfile, related_name='sender_id',on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    send_time = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.content
