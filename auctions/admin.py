from django.contrib import admin
from auctions.models import User, Item, Bid, Question, Answer

# Register your models here.
admin.site.register(User)
admin.site.register(Item)
admin.site.register(Bid)
admin.site.register(Question)
admin.site.register(Answer)