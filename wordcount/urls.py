#from django.contrib import admin
from django.urls import path

from . import views
#app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
#path('admin/',admin.site.urls),
path('', views.home,name='home'),
path('about/',views.about, name='about'),
path('count/',views.count,name='count'),
path('login/',views.login_request, name='login'),
path('register/',views.register, name='register'),
path("logout", views.logout_request, name="logout"),


#path('Egg/',views.Egg)

]

# Use include() to add paths from the catalog application
#from django.urls import include

#urlpatterns += [
    #path('catalog/', include('catalog.urls')),
#]

#Add URL maps to redirect the base URL to our application
#from django.views.generic import RedirectView
#urlpatterns += [
#    path('', RedirectView.as_view(url='catalog/', permanent=True)),
#]
