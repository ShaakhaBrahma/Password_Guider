from django.shortcuts import render, redirect
import re
from cryptography.fernet import Fernet
key = Fernet.generate_key()
f=Fernet(key)
# Create your views here.
def view(request):
	if request.method=="GET":
		return render(request, "homepage.html")
		
	if request.method=="POST":
		firstname = request.POST.get('firstname')
		lastname = request.POST.get('lastname')
		middlename = request.POST.get('middlename')
		phonenumber = request.POST.get('phonenumber')
		email = request.POST.get('email')
		place = request.POST.get('place')
		dateofbirth = request.POST.get('dateofbirth')
		listofdata=[firstname, lastname, middlename, phonenumber, email, place, dateofbirth]
		encrypted=[]
		basefile=open("base.txt", 'wb')
		proxy=open("proxy.txt",'a')
		for item in listofdata:
			proxy.write(item)
			proxy.write('\n')
		#basefile.save()
		for message in listofdata:
			encrypted.append(f.encrypt(message.encode()))
		for item in encrypted:
			basefile.write(item)
			basefile.write(bytes('\n'.encode()))
		basefile.close()	
		return redirect('home:display')

def display(request):
			if request.method =="GET":
				items=[]
				basefile=open("base.txt", 'rb')

				for item in basefile:
					x=f.decrypt(item)
					x=x.decode('utf-8')
					x=str(x)
					items.append(x)
				list0fpass=[items[0].capitalize()+'@123',items[0].capitalize()+'@'+items[6][:4],items[0].capitalize()+'@'+items[3][:5]]
				context = {'items': items,'passwords':list0fpass}
				return render(request, "display.html", context)
			if request.method == "POST":
				password = request.POST.get('password')
				items=[]
				basefile=open("base.txt", 'rb')
				for item in basefile:
					x=f.decrypt(item)
					x=x.decode('utf-8')
					x=str(x)
					items.append(x)
				list0fpass=[items[0].capitalize()+'@123',items[0].capitalize()+'@'+items[6][:4],items[0].capitalize()+'@'+items[3][:5]]
				
				#checkForStrength(password)
				x=True
				check=True
				if(password in list0fpass):
					check=False

				while x:
					if (len(password)>6 and len(password)<12) and re.search("[a-z]",password) and re.search("[A-Z]",password) and re.search("[0-9]",password) and re.search("[!@#$%^&_]",password) and check==True:
						break
					else:
						x=False
					'''elif re.search("[a-z]",password):
						break
					elif re.search("[0-9]",password):
						break	
					elif re.search("[A-Z]",password):
						break
					elif re.search("[$#@!&^%]",password):
						break'''
					
				context = {'items': items,'item':password,'passwords':list0fpass,'boolean':x}
				return render(request, "display.html", context)
#def checkForStrength(passw)            