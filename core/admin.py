from django.contrib import admin
from .models import Profile,Post,LikePosts,FollowersCount

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePosts)
admin.site.register(FollowersCount)


