from django.shortcuts import render, redirect
from .models import Receipe
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login


def getReceipe(request):
    receipedata = Receipe.objects.all()

    if request.method == 'GET':
        st = request.GET.get('search')
        if st != None:
            receipedata = Receipe.objects.filter(receipe_name=st)

    context = {'receipedata': receipedata}
    return render(request, "Receipe.html", context)


def ReceipeForm(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES['receipe_image']

        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image
        )
        return redirect('/')
    return render(request, "receipeForm.html")


def deleteReceipe(req, id):
    deletereceipe = Receipe.objects.get(id=id)
    deletereceipe.delete()
    return redirect('/')


def updateReceipe(req, id):
    queryset = Receipe.objects.get(id=id)
    if req.method == "POST":
        data = req.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = req.FILES.get('receipe_image')

        print(receipe_name)
        print(receipe_description)
        print(receipe_image)

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/')

    context = {'updatereceipe': queryset}
    return render(req, "updateReceipe.html", context)


def registerUser(req):

    if req.method=='POST':
        first_name=req.POST.get('first_name')
        last_name=req.POST.get('last_name')
        username=req.POST.get('username')
        password=req.POST.get('password')

        print(first_name)
        print(last_name)
        print(username)
        print(password)

        user=User.objects.filter(username=username)

        if user.exists():
            return redirect("/")

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password
        )

        user.set_password(password)
        user.save()
        return redirect("/register")
    return render(req,"Register.html")

  
def loginUser(req):
    if req.method=='POST':
        username=req.POST.get('username')
        password=req.POST.get('password')

        print(username)
        print(password)
        user=authenticate(username=username,password=password)

        if user is None:
            return redirect("/")
        else:
            login(req,user)
            return redirect("/receipes")
            
    return render(req,"login.html")