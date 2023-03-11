from django.contrib import admin

# Register your models here.
from .models import Profile, Post, jobboards,,joblistings,eventlistings

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(jobboards)
admin.site.register(eventlistings)
admin.site.register(joblistings)
