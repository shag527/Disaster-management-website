from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from .models import User_request,dmt,Contact_Us,dnt
from twilio.rest import Client
from django.shortcuts import get_object_or_404


# Create your views here.

def home(request):
	return render(request,'home.html',{})


def send_sms_dnt(request):
	if request.method=='POST':
		area=request.POST.get('pincode')
		my_msg=request.POST.get('SMS_send')
		num=request.user.id
		userr=dnt.objects.get(dnt_id=num)
		account_sid=userr.dnt_account_sid
		auth_token=userr.dnt_auth_token
		my_twilio=userr.contact_number
		

		client=Client(account_sid,auth_token)
		numbers=User_request.objects.filter(pincode=area)
		for to_num in numbers:
			client.messages.create(to=to_num.contact_number,from_=my_twilio,body=my_msg)
			"""add +91 to phone num. and my_twilio only twilio number"""


		return render(request,'home.html',{})

	else:

		return render(request,'dnt_send_sms.html',{})

def send_sms_dmt(request):
	if request.method=='POST':
		area=request.POST.get('pincode')
		my_msg=request.POST.get('SMS_send')
		num=request.user.id
		userr=dmt.objects.get(dmt_id=num)
		account_sid=userr.dmt_account_sid
		auth_token=userr.dmt_auth_token
		my_twilio=userr.contact_number
		

		client=Client(account_sid,auth_token)
		numbers=User_request.objects.filter(pincode=area)
		for to_num in numbers:
			client.messages.create(to=to_num.contact_number,from_=my_twilio,body=my_msg)
			"""add +91 to phone num. and my_twilio only twilio number"""


		return render(request,'home.html',{})

	else:

		return render(request,'dmt_send_sms.html',{})





def userregister(request):
	if request.method=='POST':
		post=User_request()
		post.user_name=request.POST.get('person_name')
		post.location=request.POST.get('address')
		post.contact_number=request.POST.get('contact_number')
		post.gender=request.POST.get('sex')
		post.pincode=request.POST.get('pincode')
		post.date_of_birth=request.POST.get('date_of_birth')
		post.user_id=request.user.id
		post.save()
		return render(request,'home.html',{})

	else:

		return render(request,'userregister.html',{})

def dntregister(request):
	if request.method=='POST':
		post=dnt()
		post.dnt_name=request.POST.get('person_name')
		post.location=request.POST.get('address')
		post.contact_number=request.POST.get('contact_number')
		post.email=request.POST.get('email')
		post.pincode=request.POST.get('pincode')
		post.dnt_account_sid=request.POST.get('account_sid')
		post.dnt_auth_token=request.POST.get('auth_token')
		num=request.user.id
		post.dnt_id=num
		post.save()
		return redirect('dnt_sms')

	else:

		return render(request,'dntregister.html',{})


def usersignin(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("userregister")
    else:
        form = UserCreationForm()
    return render(request, 'usersignin.html', {'form': form})


def dntsignin(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("dnt_register")
    else:
        form = UserCreationForm()
    return render(request, 'dntsignin.html', {'form': form})

def dmtsignin(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("dmt_register")
    else:
        form = UserCreationForm()
    return render(request, 'dmtsignin.html', {'form': form})        

		


def dmtregister(request):
	if request.method=='POST':
		post=dmt()
		post.dmt_name=request.POST.get('person_name')
		post.location=request.POST.get('address')
		post.contact_number=request.POST.get('contact_number')
		post.email=request.POST.get('email')
		post.pincode=request.POST.get('pincode')
		post.dmt_account_sid=request.POST.get('account_sid')
		post.dmt_auth_token=request.POST.get('auth_token')
		num=request.user.id
		post.dmt_id=num
		post.save()
		return redirect('dmt_sms')

	else:

		return render(request,'dmtregister.html',{})





#def userlogin(request):
	#return render(request,'home.html',{})


def dntlogin(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request,'dnt_send_sms.html',{})
    else:
        form = UserCreationForm()
    return render(request, 'signin.html', {'form': form})	


def dmtlogin(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("dmt_register")
    else:
        form = UserCreationForm()
    return render(request, 'signin.html', {'form': form})	



def userprofile(request):
	return render(request,'user_profile.html',{'user':request.user})

def dmtprofile(request):
	return render(request,'home.html',{})

def dntprofile(request):
	return render(request,'home.html',{})	


