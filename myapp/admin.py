from django.contrib import admin
from myapp.models import ContactForm
from myapp.models import House,Signup

# Register your models here.
class ContactFormAdmin(admin.ModelAdmin):
    list_display=('ContactForm_name','ContactForm_email','ContactForm_pnumber','ContactForm_message')

admin.site.register(ContactForm,ContactFormAdmin)

class HouseAdmin(admin.ModelAdmin):
    list_display=('House_title','House_des','House_image')

admin.site.register(House,HouseAdmin)



class SignupAdmin(admin.ModelAdmin):
    list_display=('username','fname','lname','email','password')

admin.site.register(Signup,SignupAdmin)

