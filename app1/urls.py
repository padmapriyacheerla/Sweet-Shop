from django.urls import path
from .views import *


urlpatterns = [
    path('', Home),
    path('Register', Register),
    path('Login', Login),
    path('Logout', Logout),
    path('Send-Message', Contact_Us),
    path('Menu', Menu),
    path('Admin-Login', Admin_Login),
    path('DashBoard', DashBoard),
    path('Sweet_Management', Sweet_Management),
    path('Contact_Management', Contact_Management),
    path('Admin_Management', Admin_Management),
    path('Add-Sweets', Add_Sweets),
    path('Edit-Sweets/<int:s_id>', Edit_Sweets),
    path('Delete-Sweets/<int:s_id>', Delete_Sweets),
    path('Delete-Users/<int:u_id>', Delete_Users),
    path('Edit-Users/<int:u_id>', Edit_Users),
    path('Delete-Message/<int:m_id>', Delete_Message),
    path('Admin-Register', Admin_Register),
    path('Admin-Delete/<int:a_id>', Delete_Admin),
    path('Admin-Logout', Admin_Logout),
    path('Submit-Order', Submit_Order),
    path('Sweet_Orders', Order_List),
    path('Delete-Order', Delete_Order)
]
