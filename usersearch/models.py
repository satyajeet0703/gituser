# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import rangevaluesfilterspec
class GitUser(models.Model):
	def image_tag(self):
		return u'<img src="%s" style="height: 100px;" />' % self.avatar_url
	image_tag.short_description = 'Thumbnail'
	image_tag.allow_tags = True
	"""docstring for ClassName"""
	login = models.CharField(max_length=200)
	git_id= models.IntegerField()
	avatar_url= models.URLField(max_length=200)
	gravatar_id= models.CharField(max_length=100,blank=True)
	url= models.URLField(max_length=200)
	html_url= models.URLField(max_length=200)
	followers_url = models.URLField(max_length=200)
	following_url= models.URLField(max_length=200)
	gists_url= models.URLField(max_length=200)
	starred_url= models.URLField(max_length=200)
	subscriptions_url= models.URLField(max_length=200)
	organizations_url= models.URLField(max_length=200)
	repos_url= models.URLField(max_length=200)
	events_url= models.URLField(max_length=200)
	received_events_url= models.URLField(max_length=200)
	type= models.CharField(max_length=200, blank=True, default='User')
	site_admin = models.BooleanField(default=False)
	repos=models.IntegerField(default=0)
	location=models.CharField(max_length=200,blank=True)
	language=models.CharField(max_length=200,blank=True)
	followers=models.IntegerField(default=0)
	email=models.CharField(max_length=200,blank=True)
	name=models.CharField(max_length=200,blank=True)
	score = models.FloatField()
	created = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.login
	def __unicode__(self):
		return self.login

		
# Create your models here.
