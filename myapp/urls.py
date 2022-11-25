from django.urls import path,include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import ContactListFormView, ContactDetailFormView

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('price',views.price,name='price'),
    path('house',views.house,name='house'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('showp',views.showp,name='showp'),
    path('editpage/<int:pk>',views.editpage,name='editpage'),
    path('updatedata/<int:pk>',views.updatedata,name='updatedata'),
    path('deletedata/<int:pk>',views.deletedata,name='deletedata'),
    path('newdetail/<new_slug>',views.newdetail,name='newdetail'),
    path("api/crud",ContactListFormView.as_view()),
    path("api/crud/<int:pk>",ContactDetailFormView.as_view()),
    

    
    
]



if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)