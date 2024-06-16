import random
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from apps.home.models import customer, order, product,orderpurchase,orderreturn,feedback
from apps.user.forms import RegistrationForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth import logout
from django.template import loader
from django.contrib.auth import views as auth_views

# Create your views here.


# Authentication
def registration(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      print('Account created successfully!')
      return redirect('/accounts/login/')
    else:
      print("Registration failed!")
  else:
    form = RegistrationForm()
  
  context = {'form': form}
  return render(request, 'accounts/sign-up.html', context)

def handleLogin(request):
    if request.method == 'POST':
        em = request.POST['email']
        pwd = request.POST['password']

        chkeml = customer.objects.filter(email=em)

        if len(chkeml) > 0:
            if chkeml[0].password == pwd:
                request.session['id'] = chkeml[0].id 
                request.session['cname'] = chkeml[0].cname
                request.session['email'] = chkeml[0].email
                messages.info(request,"successful Loged In")
                return redirect("index")
            else:
                messages.info(request,"wrong Password")
                return render(request,"pages/index.html")  
        else:
            messages.info(request,"invalid credentils, please try again")
            return render(request,'pages/index.html')
    return render(request,'accounts/sign-in.html')

def LogOut(request):
    if 'id' in request.session:
        del request.session['id']
        del request.session['cname'] 
        del request.session['email']
        return redirect('index')
    else:
        return redirect('index')  
     
class UserLoginView(auth_views.LoginView):
  template_name = 'accounts/sign-in.html'
  success_url = '/'

class UserPasswordResetView(auth_views.PasswordResetView):
  template_name = 'accounts/password_reset.html'
  form_class = UserPasswordResetForm

class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
  template_name = 'accounts/password_reset_confirm.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(auth_views.PasswordChangeView):
  template_name = 'accounts/password_change.html'
  form_class = UserPasswordChangeForm

def user_logout_view(request):
  logout(request)
  return redirect('/accounts/login/')


# Pages
def index(request):
  return render(request, 'pages/index.html')

def contact_us(request):
  return render(request, 'pages/contact-us.html')

def about_us(request):
  return render(request, 'pages/about-us.html')

def author(request):
  pro = True
  prod = product.objects.all()
  context = {'segment': 'pro','prod':prod,'pro':pro}
  html_template = loader.get_template('pages/author.html')
  return HttpResponse(html_template.render(context, request))
 
def woodybook(request,pk):
    pi = product.objects.get(id=pk)
    qty = request.GET.get('quantity')
    pri = request.GET.get('amount')
    iid = random.randint(1204784, 1218000)
    cn =  customer.objects.get(id=request.session['id'])
    status = "Place"
    order.objects.create(id=iid,amuont=pri,custid=cn,status=status,proid=pi,qty=qty)
    messages.info(request,"Booking successful")
    return render(request,'pages/index.html')
def orreturn(request, pk):
  order_instance = get_object_or_404(order, id=pk)
  order_return = orderreturn.objects.create(orderid=order_instance, price=order_instance.amuont)
  messages.info(request, "Return request has been created.")
  return render(request, 'pages/index.html')

def feedbackk(request):
    if request.method == 'POST':
        pi = get_object_or_404(customer, id=request.session.get('id'))
        produt = request.POST.get('review')
        
        if produt:  # Check if produt is not None or empty
            order_return = feedback.objects.create(review=produt, custid=pi)
            messages.info(request, "Thank you for giving feedback.")
        else:
            messages.error(request, "Please provide a valid review.")
    else:
        messages.error(request, "Invalid request method.")
    
    return render(request, 'pages/index.html')
  
def delorder(request,pk):
    pi = order.objects.get(id=pk)
    pi.delete()
    return redirect("/profiles")

def presentation(request):
  return render(request, 'sections/presentation.html')

def profile(request):
  pi = get_object_or_404(customer, id=request.session['id'])
  return render(request, 'pages/author2.html',{'cust':pi})

def profiles(request):
    order_id = request.session.get('id')
    pi = order.objects.filter(custid=order_id)
    return render(request, 'pages/indexs.html', {'cust': pi})
    