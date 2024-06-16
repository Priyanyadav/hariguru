from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.urls import reverse
from . models import product,customer,order,orderpurchase,orderreturn,employee,inventory


def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:  # noqa: E722
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

def showcust(request):
    cuss= True
    cus = customer.objects.all()
    context = {'segment': 'hh','h':cus,'cust':cuss}
    html_template = loader.get_template('home/show.html')
    return HttpResponse(html_template.render(context, request))

def showorder(request):
    cuss= True
    cus = order.objects.all()
    context = {'segment': 'oo','o':cus,'ooo':cuss}
    html_template = loader.get_template('home/show.html')
    return HttpResponse(html_template.render(context, request))

def showop(request):
    cuss= True
    cus = orderpurchase.objects.all()
    context = {'segment': 'op','p':cus,'opo':cuss}
    html_template = loader.get_template('home/show.html')
    return HttpResponse(html_template.render(context, request))

def showreturn(request):
    cuss= True
    cus = orderreturn.objects.all()
    context = {'segment': 'or','r':cus,'ore':cuss}
    html_template = loader.get_template('home/show.html')
    return HttpResponse(html_template.render(context, request))
    
def deletecus(request,id):
    pi = get_object_or_404(customer, pk=id)
    if request.method == 'GET':
        pi.delete()
        return redirect("/custshow")
    return render(request, 'page-404.html', {'customer': customer})
    
    
def custadd(request):
    if request.method == 'POST':
        cname = request.POST['name']
        mobile = request.POST['mobile']
        address = request.POST['address']
        email = request.POST['email']
        password = request.POST['password']
        reg = customer.objects.create(cname=cname,mobile=mobile,address=address,email=email,password=password)
        reg.save()
        return redirect("/custshow")
    context = {'segment': 'hh'}
    html_template = loader.get_template("home/custcreate.html")
    return HttpResponse(html_template.render(context, request))

def custupdate(request,pk):
    pi = get_object_or_404(customer, id=pk)
    if request.method == 'POST':
        pi.cname = request.POST.get('name') if request.POST.get('name') else pi.cname
        pi.mobile = request.POST.get('mobile') if request.POST.get('mobile') else pi.mobile
        pi.address = request.POST.get('address') if request.POST.get('address') else pi.address
        pi.email = request.POST.get('email') if request.POST.get('email') else pi.email
        pi.password = request.POST.get('password') if request.POST.get('password') else pi.password
        pi.save()
        return redirect("/custshow")
    context = {'segment': 'hh','cust':pi}
    html_template = loader.get_template("home/custupdate.html")
    return HttpResponse(html_template.render(context, request))

def orupdate(request, pk):
    order_instance = get_object_or_404(order, id=pk)
    
    if request.method == 'POST':
        product_id = request.POST.get('product')
        if product_id:
            product_instance = get_object_or_404(product, id=product_id)
            order_instance.proid = product_instance
        
        cust_id = request.POST.get('name')
        if cust_id:
            pro_instance = get_object_or_404(customer, id=cust_id)
            order_instance.custid = pro_instance
        
        order_instance.status = request.POST.get('status', order_instance.status)
        order_instance.amuont = request.POST.get('price', order_instance.amuont)
        
        order_instance.save()
        return redirect("/ordershow")
    
    context = {'segment': 'oo', 'cust': order_instance}
    html_template = loader.get_template("home/orderup.html")
    return HttpResponse(html_template.render(context, request))

def orpupdate(request, pk):
    pur_instance = product.objects.all()
    order_instance = get_object_or_404(orderpurchase, id=pk)
    
    if request.method == 'POST':
        product_id = request.POST.get('product')
        if product_id:
            product_instance = get_object_or_404(product, id=product_id)
            order_instance.proid = product_instance
            
        order_instance.status = request.POST.get('status', order_instance.status)
        order_instance.price = request.POST.get('price', order_instance.price)
        
        order_instance.save()
        return redirect("/pshow")
    
    context = {'segment': 'op', 'cust': order_instance,'pro': pur_instance}
    html_template = loader.get_template("home/orderreup.html")
    return HttpResponse(html_template.render(context, request))

def reurntadd(request, pk):
    pur_instance = product.objects.all()
    order_instance = get_object_or_404(orderpurchase, id=pk)
    
    if request.method == 'POST':
        product_id = request.POST.get('product')
        if product_id:
            product_instance = get_object_or_404(product, id=product_id)
            order_instance.proid = product_instance
            
        order_instance.status = request.POST.get('status', order_instance.status)
        order_instance.price = request.POST.get('price', order_instance.price)
        
        order_instance.save()
        return redirect("/pshow")
    
    context = {'segment': 'op', 'cust': order_instance,'pro': pur_instance}
    html_template = loader.get_template("home/orderreup.html")
    return HttpResponse(html_template.render(context, request))

def oradd(request):
    products = product.objects.all()
    
    if request.method == 'POST':
        product_id = request.POST.get('product')
        status = request.POST.get('status')
        price = request.POST.get('price')
        
        # Get the selected product instance
        selected_product = product.objects.get(id=product_id)
        
        # Create a new instance of OrderPurchase
        new_order = orderpurchase.objects.create(
            proid=selected_product,
            status=status,
            price=price
        )
        new_order.save()
        return redirect("/pshow")
    
    context = {'segment': 'op', 'pro': products}
    return render(request, "home/orderrein.html", context)


def showemp(request):
    empp = True
    emp = employee.objects.all()
    context = {'segment': 'emp','emp':emp,'empp':empp}
    html_template = loader.get_template('home/show.html')
    return HttpResponse(html_template.render(context, request))
    
def deleteemp(request,id):
    pi = get_object_or_404(employee, pk=id)
    if request.method == 'GET':
        pi.delete()
        return redirect("/empshow")
    return render(request, 'page-404.html', {'customer': customer})
    
    
def empadd(request):
    if request.method == 'POST':
        ename = request.POST['name']
        mobile = request.POST['mobile']
        payroll = request.POST['payroll']
        email = request.POST['email']
        password = request.POST['password']
        skill = request.POST['skill']
        jdate = request.POST['jdate']
        reg = employee.objects.create(email=email,password=password,ename=ename,emp_skill=skill,emp_joindate=jdate,mobile=mobile,payroll=payroll)
        reg.save()
        return redirect("/empshow")
    context = {'segment': 'emp'}
    html_template = loader.get_template('home/empcreate.html')
    return HttpResponse(html_template.render(context, request))

def empupdate(request,pk):
    pi = get_object_or_404(employee, id=pk)
    if request.method == 'POST':
        pi.ename = request.POST.get('name') if request.POST.get('name') else pi.ename
        pi.mobile = request.POST.get('mobile') if request.POST.get('mobile') else pi.mobile
        pi.payroll = request.POST.get('payroll') if request.POST.get('payroll') else pi.payroll
        pi.email = request.POST.get('email') if request.POST.get('email') else pi.email
        pi.password = request.POST.get('password') if request.POST.get('password') else pi.password
        pi.emp_skill = request.POST.get('skill') if request.POST.get('skill') else pi.emp_skill
        pi.emp_joindate = request.POST.get('jdate') if request.POST.get('jdate') else pi.emp_joindate
        pi.save()
        return redirect("/empshow")
    context = {'segment': 'emp','cust':pi}
    html_template = loader.get_template('home/empupdate.html')
    return HttpResponse(html_template.render(context, request))

def showpro(request):
    pro = True
    prod = product.objects.all()
    context = {'segment': 'pro','prod':prod,'pro':pro}
    html_template = loader.get_template('home/show.html')
    return HttpResponse(html_template.render(context, request))

def proadd(request):
    if request.method == 'POST':
        pname = request.POST['name']
        img = request.FILES.get('image', False)
        price = request.POST['price']
        weigth = request.POST['weigth']
        reg = product.objects.create(pname=pname,pro_img=img,price=price,weigth=weigth)
        reg.save()
        return redirect("/proshow")
    context = {'segment': 'pro'}
    html_template = loader.get_template("home/procreate.html")
    return HttpResponse(html_template.render(context, request))

def deletepro(request,id):
    pi = get_object_or_404(product, pk=id)
    if request.method == 'GET':
        pi.delete()
        return redirect("/proshow")
    return render(request, 'page-404.html', {'customer': customer})

def proupdate(request,pk):
    pi = get_object_or_404(product, id=pk)
    if request.method == 'POST':
        pi.pname = request.POST.get('name') if request.POST.get('name') else pi.pname
        pi.pro_img = request.FILES.get('image') if request.FILES.get('image') else pi.pro_img
        pi.price = request.POST.get('price') if request.POST.get('price') else pi.price
        pi.weigth = request.POST.get('weigth') if request.POST.get('weigth') else pi.weigth
        pi.save()
        return redirect("/proshow")
    context = {'segment': 'hh','cust':pi}
    html_template = loader.get_template("home/proupdate.html")
    return HttpResponse(html_template.render(context, request))

def showi(request):
    pro = True
    prod = inventory.objects.all()
    context = {'segment': 'ii','iiii':prod,'iii':pro}
    html_template = loader.get_template('home/show.html')
    return HttpResponse(html_template.render(context, request))

def iadd(request):
    pro = product.objects.all()
    if request.method == 'POST':
        products = request.POST['product']
        mdate = request.POST['jdate']
        qty = int(request.POST['qty'])
        name = request.POST['name']
        try:
            # Try to get the existing inventory entry for the product
            inventory_entry = inventory.objects.get(proid_id=products, batchno=name)
            # If the entry exists, increase the quantity
            inventory_entry.qty += qty
            inventory_entry.save()
            return redirect("/ishow")
        except inventory.DoesNotExist:
            # If the entry does not exist, create a new one
            inventory_entry = inventory.objects.create(proid_id=products, mfgdate=mdate, batchno=name, qty=qty)
            return redirect("/ishow")
    context = {'segment': 'ii','pro':pro}
    html_template = loader.get_template("home/icreate.html")
    return HttpResponse(html_template.render(context, request))

def deletei(request,id):
    pi = get_object_or_404(inventory, pk=id)
    if request.method == 'GET':
        pi.delete()
        return redirect("/ishow")
    return render(request, 'page-404.html', {'customer': customer})

def proi(request, pk):
    pi = get_object_or_404(inventory, id=pk)
    if request.method == 'POST':
        product_id = request.POST.get('product')
        batch_no = request.POST.get('name')
        mfgdate = request.POST.get('jdate')
        qty = int(request.POST.get('qty'))

        if product_id:
            product_instance = get_object_or_404(product, id=product_id)
            pi.proid = product_instance

        pi.mfgdate = mfgdate
        pi.qty = qty
        pi.batchno = batch_no
        pi.save()
        return redirect("/ishow")
    context = {'segment': 'ii', 'cust': pi}
    return render(request, "home/iupdate.html", context)
