from django.forms import widgets
from rest_framework import serializers
from models import *

class UserListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        user_mapping = {user.git_id: user for user in instance}
        data_mapping = {item['id']: item for item in validated_data}

        # Perform creations and updates.
        ret = []
        for user, data in data_mapping.items():
            user = user_mapping.get(git_id, None)
            if user is None:
            	data['git_id']=data['id']
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(user, data))

        return ret

class UserSerializer(serializers.ModelSerializer):
	def create(self, validated_data):
		return GitUser.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.git_id=validated_data.get('git_id', instance.git_id)
		instance.login = validated_data.get('login', instance.login)
		instance.avatar_url=  validated_data.get('avatar_url', instance.avatar_url)
		instance.gravatar_id=  validated_data.get('gravatar_id', instance.gravatar_id)
		instance.url=  validated_data.get('url', instance.url)
		instance.html_url=  validated_data.get('html_url', instance.html_url)
		instance.followers_url = validated_data.get('followers_url', instance.followers_url)
		instance.following_url=  validated_data.get('following_url', instance.following_url)
		instance.gists_url=  validated_data.get('gists_url', instance.gists_url)
		instance.starred_url=  validated_data.get('starred_url', instance.starred_url)
		instance.subscriptions_url=  validated_data.get('subscriptions_url', instance.subscriptions_url)
		instance.organizations_url=  validated_data.get('organizations_url', instance.organizations_url)
		instance.repos_url=  validated_data.get('repos_url', instance.repos_url)
		instance.events_url=  validated_data.get('events_url', instance.events_url)
		instance.received_events_url=  validated_data.get('received_events_url', instance.received_events_url)
		instance.type=  validated_data.get('type', instance.type)   
		instance.site_admin =  validated_data.get('site_admin', instance.site_admin)
		instance.score =  validated_data.get('score', instance.score)
		instance.email =  validated_data.get('email', instance.email)
		instance.name =  validated_data.get('name', instance.email)
		instance.save()
		return instance

	class Meta:
		model = GitUser
		fields = ('login','git_id','avatar_url','gravatar_id','url','html_url','followers_url','following_url','gists_url','starred_url','subscriptions_url','organizations_url','repos_url','events_url','received_events_url','type','site_admin','score','email','name','repos','location','language','followers')
		depth = 1
