from django.shortcuts import render, redirect

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
		basefile=open("base.txt", 'w')
		for item in listofdata:
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
			if request.method == "POST":
				password = request.POST.get('password')
				items=[]
				basefile=open("base.txt", 'r')
				for item in basefile:
					items.append(item)
				context = {'items': items,'item':password}
				#checkForStrength(password)
				return render(request, "display.html", context)
            