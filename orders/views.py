
import os
from unicodedata import category 
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from orders.forms import Register
#docarador para nuestra urls privadas
from  django.contrib.auth.decorators import login_required
from orders.models import menu,toppings,subs,pasta,salads,Dinner,Pedido
#from orders.carrito import carrito


# Create your views here.


def register(request):
  
    
    
    register_form = Register()
    
    if request.method == 'POST':
        register_form =Register(request.POST)
        
        if register_form.is_valid():
         register_form.save()
            
         return redirect("login")
        
    return render(request,'register.html',{
        'title': 'Register',
        'register_form': register_form
    })

def login_page(request):
 #vamos hacer la authenticacion del usuario
   
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.warning(request,'No te has registrado')


    return render(request,'login.html',{
    'Title':'Identificate'
})

@login_required(login_url="login")
def home(request):
     
     
       
     return render(request,"home.html")
 
#logout user
def logout_user(request):
    logout(request)
    return redirect('login')


#Aqui es el enlace de menu
@login_required(login_url="login")
def Menu(request):
    
  

    carta_menu = menu.objects.all()
    
    topping = toppings.objects.all()

    sub = subs.objects.all()
    
    past = pasta.objects.all()
    
    ensaladas = salads.objects.all()

    dinner_salads = Dinner.objects.all()
    
    imageness = menu.objects.raw("SELECT * FROM orders_menu WHERE id=1 ")
    imagenesss = menu.objects.raw("SELECT * FROM orders_menu WHERE id=2")
    
    return render(request,'menu.html',{
        'carta_menu': carta_menu,
        'topping':topping,
        'subs': sub,
        'pasta':past,
        'ensaladas': ensaladas,
        'Dinner': dinner_salads,
        'imagenes':imageness,
        'imageness':imagenesss
      
    })
#here direction
@login_required(login_url="login")
def direction(request):
    
     return render(request,"direction.html")

#here in hours
@login_required(login_url="login")
def hours(request):
  
    
    return render(request,'hours.html')

#here in silian vs regular
@login_required(login_url="login")
def vs(request):
  
    return render(request, 's_vs_regular.html')

#here in contact us
@login_required(login_url="login")
def contact(request):
    
    return render(request, 'contact.html')

@login_required(login_url="login")
def pedido(request):
   
    if request.method == 'POST':
        
        nombre_comida = request.POST['type_food']
        x = menu.objects.filter(type_food=nombre_comida)
        print(x)
        if len(list(x.values())) > 0:
            if request.POST['option'] == 's':
                precio = x[0].price1 * int(request.POST['number'])
            else:
                precio = x[0].price2  * int(request.POST['number'])
                    
            resultado = Pedido.objects.create(user=request.user.username, precio=precio, cantidad=request.POST['number'], categoria=request.POST['type_food'])

            
        medida = request.POST['option']
        resultado.save()
        print(nombre_comida)
        print(medida)
        return redirect(to='pedido')
    return render(request, 'pedido.html')


@login_required(login_url="login")
def aceptar_pedido(request):
    
    lista_ordenes = Pedido.objects.all()
    
    
    return render(request,'aceptar_pedido.html',{
        'lista_ordenes':lista_ordenes
    })


def delete_pedido(request, id):
        lista_pedidos = Pedido.objects.get(pk=id)
    
        lista_pedidos.delete()
    
        

        return redirect('aceptar_pedido')
    
    

