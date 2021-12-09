from django.contrib.auth.signals import user_logged_in, user_login_failed
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import Group
from .models import studentgriev , contactus , facgrieve
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.db import IntegrityError
from django.shortcuts import get_object_or_404



def index(request):
    return render(request,'index.html')
    #return HttpResponse("Homepage!")


def stusignup(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if not pass1 == pass2:
            messages.error(request,"Please enter same password!")
        else:

            try:
                myuser = User.objects.create_user(username=name,password=pass1,email=email)
            
                myuser.name = name
                myuser.email = email
                myuser.password = pass1
                myuser.save()

                group = Group.objects.get(name='Student')
                myuser.groups.add(group)

                return redirect('studentloginpage')

            except IntegrityError as e:
                messages.warning(request,"User Already Exists !")
                return render(request,"stusignup.html")
    
    return render(request,'stusignup.html')


#def is_student(user):
 #   return user.groups.filter(name='Student')     

#@user_passes_test(is_student)
def stuloginpage(request):
    if request.method == 'POST':
        user_email = request.POST['email']
        pass1 = request.POST['password']

        try:    
            user = User.objects.get(email=user_email,password=pass1)

            if user.groups.filter(name = 'Student').exists():
                if user is not None:
                    login(request,user)
                    return redirect('homepage')
                    #messages.success(request,'Login Succcessful')

                else:
                    messages.info(request, "Username OR Password is INCORRECT")
            else:
                return HttpResponse("You aren't a Student !")
        except:
            messages.warning(request,"Invalid Login !")
            return render(request,"stulogin.html")

    return render(request,'stulogin.html')

def stulogout(request):
    logout(request)
    return redirect('selectlogintype')

def facsignup(request):
    if request.method == "POST":
        myusername = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if not pass1 == pass2:
            #messages.warning(request,"Please enter same password!")
            return render(request,'facsignup.html')
        else:

            try:
                myuser = User.objects.create_user(username=myusername,password=pass1,email=email)

                myuser.name = myusername
                myuser.email = email
                myuser.password = pass1
                myuser.save()

                group = Group.objects.get(name='Faculty')
                myuser.groups.add(group)


                return redirect('facultyloginpage')
            except IntegrityError as e:
                messages.warning(request,"User Already Exists !")
                return render(request,"facsignup.html")
                

    return render(request,'facsignup.html')

def facloginpage(request):
    if request.method == 'POST':
        user_email = request.POST['email']
        pass1 = request.POST['password']
        
        try:
            myuser = User.objects.get(email=user_email,password=pass1)
    
            if myuser.groups.filter(name = 'Faculty').exists():    
                if myuser is not None:
                    login(request,myuser)
                    return redirect('facgrievpage')
                    #messages.success(request,'Login Succcessful')

                else:
                    return redirect('facultyloginpage')
                    #messages.error(request, "Invalid Login")
            else:
                return HttpResponse("You are not Autherised !")
            
        except:
            messages.warning(request,"Invalid Login !")
            return render(request,"faclogin.html")

    return render(request,'faclogin.html')



def stugrievpage(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            contactnum = request.POST['contactnum']
            email = request.POST['email']
            grievance = request.POST['message']
        

            griv = studentgriev()
            griv.name = name
            griv.contactnum = contactnum
            griv.email = email
            griv.grievance = grievance
            griv.save()
        return render(request,'stugrievances.html')
    except:
        messages.warning(request,"Oops Try Again !")
        return render(request,"stugrievances.html")

def managestugriev(request):
    current_user = "devangmahimkar206@nhitm.ac.in"
    from_stugrievance = studentgriev.objects.filter(email = current_user)
    from_facgriev = facgrieve.objects.filter(solution = current_user)
    return render(request,'manageGriev.html',{"data_form_stu":from_stugrievance,"data_from_fac":from_facgriev})

    


def facgrievpage(request):
    if request.method == 'POST':
        Solution = request.POST['solution']

        comment = facgrieve()
        comment.solution = Solution
        comment.save()

    grievance_data =  studentgriev.objects.all()
    return render(request,'facgrievances_1.html',{"data":grievance_data})    

def chooselogin(request):
    return render(request,'Welcome.html')
    

def contactuspage(request):
    if request.method == 'POST':
        ctname = request.POST['name']
        ctemail = request.POST['email']
        ctsubject = request.POST['subject']
        ctmessage = request.POST['message']

       # print(ctname,ctemail,ctsubject,ctmessage)

        ctus = contactus()
        ctus.ctname = ctname
        ctus.ctemail = ctemail
        ctus.ctsubject = ctsubject
        ctus.ctmessage = ctmessage
        ctus.save()

    return render(request,'contactus.html')
    

def aboutus(request):
    return render(request,'about.html')


def registerpage(request):
    return render(request,'register.html')

