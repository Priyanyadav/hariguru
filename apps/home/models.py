# -*- encoding: utf-8 -*-

from django.db import models

class customer(models.Model):
     cname = models.CharField(max_length=20)
     email = models.EmailField(default='example@example.com')
     mobile = models.BigIntegerField(null=True,blank=True)
     password = models.CharField(max_length=20)
     address = models.CharField(max_length=100)
     def __str__(self):
        return self.cname

class product(models.Model):
     pname = models.CharField(max_length=20)
     price = models.BigIntegerField(null=True,blank=True)
     weigth = models.BigIntegerField()
     pro_img = models.ImageField(upload_to='pics/', default='NULL')
     def __str__(self):
        return self.pname
  
class order(models.Model):
     status = models.CharField(max_length=20)
     custid = models.ForeignKey(customer,on_delete=models.CASCADE)
     proid = models.ForeignKey(product,on_delete=models.CASCADE)
     qty = models.CharField(max_length=2,default='1')
     amuont = models.DecimalField(max_digits=10, decimal_places=2)
     def __str__(self):
        return self.custid 
     
class orderreturn(models.Model):
     orderid = models.ForeignKey(order,on_delete=models.CASCADE)
     price = models.DecimalField(max_digits=10, decimal_places=2)
     def __str__(self):
        return self.orderid 
     
class orderpurchase(models.Model):
     proid = models.ForeignKey(product,on_delete=models.CASCADE)
     status = models.CharField(max_length=20)
     price = models.DecimalField(max_digits=10, decimal_places=2)
     def __str__(self):
        return self.proid 
     
class payment(models.Model):
     orderid = models.ForeignKey(order,on_delete=models.CASCADE)
     method = models.CharField(max_length=20,default='COD')
     price = models.DecimalField(max_digits=10, decimal_places=2)
     def __str__(self):
        return self.orderid
     
class invoice(models.Model):
     custid = models.ForeignKey(customer,on_delete=models.CASCADE)
     orderid = models.ForeignKey(order,on_delete=models.CASCADE)
     method = models.CharField(max_length=20,default='COD')
     price = models.DecimalField(max_digits=10, decimal_places=2)
     def __str__(self):
        return self.id

class inventory(models.Model):
     mfgdate = models.DateField()
     proid = models.ForeignKey(product,on_delete=models.CASCADE)
     qty = models.BigIntegerField(null=True,blank=True)
     batchno = models.BigIntegerField(null=True,blank=True)
     def __str__(self):
        return self.proid    
     
class employee(models.Model):
     ename = models.CharField(max_length=20)
     email = models.EmailField(max_length=30)
     payroll = models.DecimalField(max_digits=10, decimal_places=2)
     mobile = models.BigIntegerField(null=True,blank=True)
     password = models.CharField(max_length=20)
     emp_joindate = models.DateField()
     emp_skill = models.CharField(max_length=100)
     def __str__(self):
        return self.ename
     
     
class feedback(models.Model):
     custid = models.ForeignKey(customer,on_delete=models.CASCADE)
     review = models.CharField(max_length=100)
     def __str__(self):
        return self.custid