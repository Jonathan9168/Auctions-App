from django.contrib.auth.models import AbstractUser
from django.db import models


# User Class
class User(AbstractUser, models.Model):
    city : str = models.CharField(max_length=120)
    dob : any= models.DateField(null=True)
    profile_picture : any= models.ImageField(upload_to='')

    def __str__(self):
        return self.email

    def to_dict(self):
        return {
            'id': self.id,
            'city': self.city,
            'dob': self.dob,
            'profile_picture': self.profile_picture.name,
            'email': self.email,
        }


# Item Class
class Item(models.Model):
    user : any = models.ForeignKey(User, on_delete=models.CASCADE)
    title : str= models.CharField(max_length=120)
    description : str= models.CharField(max_length=300)
    starting_price : int= models.DecimalField(decimal_places=2, max_digits=15, null=False)
    image  : any= models.ImageField(upload_to='')
    listing_time : any= models.DateTimeField(auto_now_add=True)
    auction_end_time : any= models.DateTimeField(null=False)

    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user.id,
            'title': self.title,
            'description': self.description,
            'starting_price': self.starting_price,
            'image': self.image.name,
            'listing_time': self.listing_time,
            'auction_end_time': self.auction_end_time,
        }


# Bid Class
class Bid(models.Model):
    user : any = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    item : str = models.ForeignKey(Item, blank=False, on_delete=models.CASCADE)
    price : int = models.DecimalField(decimal_places=2, max_digits=15, null=False)
    time_created : any= models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user.id,
            'item': self.item.id,
            'price': self.price,
            'time_created': self.time_created,
        }


# Question class
class Question(models.Model):
    user : any = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    item : str= models.ForeignKey(Item, blank=False, on_delete=models.CASCADE)
    question : str = models.CharField(max_length=120)
    time_created : any= models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        if hasattr(self, 'answer'):
            ans = self.answer.to_dict()
        else:
            ans = None
        return {
            'id': self.id,
            'user': self.user.id,
            'item': self.item.id,
            'question': self.question,
            'time_created': self.time_created,
            'answer':ans,
        }


# Answer class
class Answer(models.Model):
    user : any = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    answer_text : str= models.CharField(max_length=200)
    answered : bool = models.DateTimeField(auto_now_add=True)
    question  = models.OneToOneField(Question, on_delete=models.CASCADE, null=True)

    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user.id,
            'question': self.question.id,
            'answer_text': self.answer_text,
            'answered': self.answered,
        }
