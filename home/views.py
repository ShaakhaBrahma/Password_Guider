from django.shortcuts import render, redirect
from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
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
		
		for message in listofdata :
			
			encrypted.append(f.encrypt(message.encode()))
		basefile=open("base.txt", 'wb')
		for item in encrypted:
			basefile.write(item)
			basefile.write(bytes('\n'.encode()))
		#basefile.save()
		basefile.close()	
		return redirect('home:display')

def display(request):
			if request.method =="GET":
				items=[]
				basefile=open("base.txt", 'rb')
				for item in basefile:
					x=f.decrypt(item)
					items.append(x.decode())

				context = {'items': items}
				return render(request, "display.html", context)
			