from django.db import models
from datetime import datetime
# Create your models here.
class   Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

class Login(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

class Follow(models.Model):
    follower = models.ForeignKey(Register, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(Register, on_delete=models.CASCADE, related_name='following')
    created_at = models.DateTimeField(default=datetime.now, blank=True)

class Notification(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

class Message(models.Model):
    sender = models.ForeignKey(Register, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Register, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

class Report(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

class ReportComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
class ReportLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
        
class ReportFollow(models.Model):
    follower = models.ForeignKey(Register, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(Register, on_delete=models.CASCADE, related_name='following')
    created_at = models.DateTimeField(default=datetime.now, blank=True)
            
class ReportMessage(models.Model):
    sender = models.ForeignKey(Register, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Register, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

class ReportPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now, blank=True)


