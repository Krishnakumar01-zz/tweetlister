from django.shortcuts import render
from .forms import ListForm
import requests
from requests_oauthlib import OAuth1
import unicodedata
import json

consumerkey="jSV1ahhGyePTTjYETSIl6sjky" 
consumersecret="BsXvfsHJ9ZmZdYuMeuCRxfC1Hzk0anoVZYZFn1YVSlfAvGXzF1" 
accesstoken="960492725949919233-GUXFFZyKTVdke5LDAMoTke7PWjB1aBY"
accesstokensecret="YsE36OJMkhe8dpLkayywyqp3f76ik5Ty11GqKbzZ19lc5" 

auth=OAuth1(consumerkey,consumersecret,accesstoken,accesstokensecret)

def frontpage(request):
	if request.method=="POST":
		form = ListForm(request.POST)
		user=request.POST["user"]
		link="https://api.twitter.com/1.1/statuses/user_timeline.json?"+"screen_name="+str(user)+"&count=10"
		result=requests.get(link,auth=auth)
		res=result.json()
		act_res=[]
		for i in res:
			act_res.append(i["text"])
		return render(request,'tweetlister/frontpage.html',{'form':form,'res':act_res})
	else:
		form = ListForm()
		return render(request,'tweetlister/frontpage.html',{'form':form})

