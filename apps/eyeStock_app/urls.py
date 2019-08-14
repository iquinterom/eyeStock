from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.welcome),
    url(r'^registration$',views.registration),
    url(r'^dashboard$',views.dashboard),
    url(r'^login$',views.login),
    url(r'^process_login$',views.process_login),
    url(r'^checkout$',views.checkout),
    url(r'^products$',views.products),
    url(r'^add_product$',views.add_product),
    url(r'^add_vehicle$',views.add_vehicle),
    url(r'^employee_form$',views.employee_form),
    url(r'^add_employee$',views.add_employee),
    url(r'^employee_list$',views.employee_list),
    url(r'^logout$',views.logout),

]