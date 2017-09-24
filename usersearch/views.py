# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse

from django.contrib.auth.models import User, Group
from models import *
from rest_framework import viewsets
from serializers import UserSerializer
from django.views.generic import View
import requests
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
import sys
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = GitUser.objects.all()
    serializer_class = UserSerializer


class SerachUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = GitUser.objects.all()
    serializer_class = UserSerializer

class SerachUserView(View):
    #https://api.github.com/search/users?q=tom+repos:%3E42+followers:%3E1000
    def get(self, request, *args, **kwargs):
        git_baseurl="https://api.github.com/search/users?q="
        context={}
        git_baseurl= git_baseurl + (request.GET.get('name') if request.GET.get('name') else '')
        git_baseurl=git_baseurl+ ( "+type:"+request.GET.get('type') if request.GET.get('type') else '')
        #tin= request.GET['in']
        repos=request.GET.get('repos') if request.GET.get('repos') else 0
        location=request.GET.get('location') if request.GET.get('location') else ''
        language=request.GET.get('language') if request.GET.get('language') else ''
        created=request.GET.get('created') if request.GET.get('created') else ''
        followers=request.GET.get('followers') if request.GET.get('followers') else 0
        if repos != 0:
            git_baseurl=git_baseurl+"+repos:>"+str(repos)
        if location != '':
            git_baseurl=git_baseurl+"+location:"+location
        if language != '':
            git_baseurl=git_baseurl+"+language:"+language
        if created!='':
            git_baseurl=git_baseurl+"+created:"+created
        if followers!=0:
            git_baseurl= git_baseurl+"+followers:>"+followers
        print git_baseurl
        headers={'Accept':'application/vnd.github.v3.text-match+json'}
        r = requests.get(git_baseurl,headers=headers)
        response_users=r.json()['items']
        for r_user in response_users:
            r_user['repos']=repos
            r_user['location']=location
            r_user['language']=language
            r_user['created']=created
            r_user['followers']=followers
            r_user['name']=''
            r_user['email']=''
            for text_match in r_user['text_matches']:
                if text_match['property']=='name':
                    r_user['name']=text_match['fragment']
                elif text_match['property'] == 'email':
                    r_user['email']=text_match['fragment']
            r_user['git_id']=r_user['id']
            serializer = UserSerializer(data=r_user)
            try:
                gituser=GitUser.objects.get(git_id=r_user['id'])
                serializer.update(gituser,r_user)
                continue
            except:
                print("Unexpected error:", sys.exc_info()[0])
                print("Unexpected error:", sys.exc_info()[1])
                pass
            if serializer.is_valid():
               serializer.save()
            else:
                print "data not valid"
        return HttpResponse("")