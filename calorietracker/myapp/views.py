from django.shortcuts import render,redirect
from .models import Food,Consume
# Create your views here.
def index(request):

    if request.method=="POST":
        # Access to whatever value the user have selected(its just a plain text)
        food_consumed=request.POST['food_consumed']
        # We have to get the object by the name that we have selected
        consume=Food.objects.get(name=food_consumed)
        # Get the user that is currently logged in 
        user=request.user
        # We have created an instance
        consume=Consume(user=user,food_consumed=consume)
        consume.save()
        foods=Food.objects.all()
        consumed_food= Consume.objects.filter(user=request.user)
    else:
        foods=Food.objects.all()
        consumed_food= Consume.objects.filter(user=request.user)
    return render(request,'myapp/index.html',{'foods':foods,'consumed_food':consumed_food})


def delete_consume(request,id):
    consumed_food=Consume.objects.get(id=id)
    if request.method=="POST":
        consumed_food.delete()
        return redirect('/')
    return render(request,"myapp/delete.html")
