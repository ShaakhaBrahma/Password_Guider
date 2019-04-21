from django.shortcuts import render, redirect
from cryptography.fernet import Fernet

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
		key = Fernet.generate_key()
		for message in listofdata :
			f = Fernet(key)
			encrypted.append(f.encrypt(message))
		basefile=open("base.txt", 'w')
		for item in encrypted:
			basefile.write(item)
			basefile.write('\n')
		#basefile.save()
		basefile.close()	
		return redirect('home:display')

def display(request):
			if request.method =="GET":
				items=[]
				basefile=open("base.txt", 'r')
				for item in basefile:
					items.append(item)
				context = {'items': items}
				return render(request, "display.html", context)
			