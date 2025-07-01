 
from django.contrib import admin
from django.urls import path
# i add line 4 hear
from pro import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name = 'home' ),
    path('about-us/', views.aboutUs,name='about'),
    path('contact-us/',views.contact, name='contact'),
    path('save-contact/', views.savecontact , name='savecontact'),
    path('submit-review/',views.submitreview , name='submitreview'),
    path('thankyou/',views.thank_you_page,name = "thankyou"),
    path('zora/',views.zora, name="zora"),

]
