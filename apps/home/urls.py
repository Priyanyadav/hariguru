from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from apps.home import views

urlpatterns = [

    path('home/', views.index, name='home'),
    path('custshow', views.showcust, name='custshow'),
    path('custadd', views.custadd, name='custadd'),
    path('custdelete/<int:id>/',views.deletecus,name="custdelete"),
    path('custupdate/<int:pk>/',views.custupdate,name="custupdate"),
    
    path('generate_pdf/<int:order_id>/', views.generate_pdf, name='generate_pdf'),
     path('customer-report/', views.customer_report, name='customer_report'),
    
    
    path('empshow', views.showemp, name='empshow'),
    path('empadd', views.empadd, name='empadd'),
    path('empdelete/<int:id>/',views.deleteemp,name="empdelete"),
    path('empupdate/<int:pk>/',views.empupdate,name="empupdate"),
    path('ordershow', views.showorder, name='ordershow'),
    path('orderup/<int:pk>/',views.orupdate,name="orderup"),
    path('proshow', views.showpro, name='proshow'),
    path('proadd', views.proadd, name='proadd'),
    path('prodelete/<int:id>/',views.deletepro,name="prodelete"),
    path('proupdate/<int:pk>/',views.proupdate,name="proupdate"),
    path('rshow', views.showreturn, name='rshow'),
    path('pshow', views.showop, name='pshow'),
    path('padd', views.oradd, name='padd'),
    path('opupdate/<int:pk>/',views.orpupdate,name="opupdate"),
    path('ishow', views.showi, name='ishow'),
    path('iadd', views.iadd, name='iadd'),
    path('iupdate/<int:pk>/',views.proi,name="iupdate"),
    path('idelete/<int:id>/',views.deletei,name="idelete"),
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
