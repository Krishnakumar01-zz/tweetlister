from django.shortcuts import redirect
from django.shortcuts import render,get_object_or_404
from .forms import ListForm
import requests
from requests_oauthlib import OAuth1
import unicodedata
import json

consumerkey="" 
consumersecret="" 
accesstoken=""
accesstokensecret="" 

auth=OAuth1(consumerkey,consumersecret,accesstoken,accesstokensecret)

def frontpage(request):
	if request.method=="POST":
		form = ListForm(request.POST)
		user=request.POST["user"]
		num=request.POST["number"]
		link="https://api.twitter.com/1.1/statuses/user_timeline.json?"+"screen_name="+str(user)+"&count="+str(num)
#		result = oauth_req( link, ' 953928076865318912-bWCCNMSpGcndaDHznEpz5fDTRLaq1d5', ' 3X1FkF3yxJ7Jdi6SSjTCdeXt6lqo0PXjqeWFOf2ZYgr9x' )
#		res=result.json()
		result=requests.get(link,auth=auth)
		res=result.json()
		act_res=[]
		for i in res:
			act_res.append(i["text"])
#		act_res=unicodedata.normalize('NFKD', res).encode('ascii','ignore')
		return render(request,'tweetlister/frontpage.html',{'form':form,'res':act_res})
	else:
		form = ListForm()
		return render(request,'tweetlister/frontpage.html',{'form':form})

