from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group,User
# Create your models here.
class GroupProfileInfo(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    group_pic = models.ImageField(upload_to='group_profile_pics/', default='default_pic/default_pic.jpg', blank=True)
    biography = models.TextField(max_length=200, blank=False)
    fee = models.IntegerField(default=0,null=False)

class GroupRequestInfo(models.Model):
    created = models.DateTimeField(default=timezone.now)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    rejected = models.DateTimeField(blank=True, null=True)
    from_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='group_requests_sent')
    to_admin = models.ForeignKey(User,on_delete=models.CASCADE,related_name='group_requests_received')

class GroupPost(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(blank=False, null=False)
    created_date = models.DateTimeField(
        default=timezone.now)

class GroupInvitation(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='group_invitation_received')
    from_admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='group_invitation_sent')
    created = models.DateTimeField(default=timezone.now)
    rejected = models.DateTimeField(blank=True, null=True)

def __str__(self):
    return self.group.name