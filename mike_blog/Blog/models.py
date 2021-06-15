from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from .utils import sendTransaction
import hashlib

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(blank=True)
    published_date = models.DateTimeField(blank=True)
    hash = models.CharField(max_length=32, default=None, null=True)
    txId = models.CharField(max_length=66, default=None, null=True)

    def __str__(self):
        return self.title

    def save(self):
        if 'hack' in self.text:
            raise Exception('Error, you can t public post with the word hack')
        return super(Post, self).save()

    def writeOnChain(self):
        self.hash= hashlib.sha256(self.text.encode('utf-8')).hexdigest()
        self.txId = sendTransaction(self.hash)
        self.save()

