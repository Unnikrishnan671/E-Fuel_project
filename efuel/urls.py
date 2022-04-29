"""efuel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, include
from django.conf import settings
from django.conf.urls.static import static
from efuelapp import views

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^$', views.login, name='login'),
    re_path(r'^Registration/$',views.Registration,name='Registration'),

    re_path(r'^Owner_index/$', views.Owner_index, name='Owner_index'),
    re_path(r'^Owner_home/$',views.Owner_home,name='Owner_home'),
    re_path(r'^Owner_addbunk/$',views.Owner_addbunk,name='Owner_addbunk'),
    re_path(r'^Owner_view_booking/$',views.Owner_view_booking,name='Owner_view_booking'),
    re_path(r'^Owner_contact/$',views.Owner_contact,name='Owner_contact'),
    re_path(r'^Owner_addcategory$',views.Owner_addcategory,name='Owner_addcategory'),
    re_path(r'^Owner_addproduct/$',views.Owner_addproduct,name='Owner_addproduct'),
    re_path(r'^Owner_addpro/$',views.Owner_addpro,name='Owner_addpro'),
    re_path(r'^Owner_view_product/$',views.Owner_view_product,name='Owner_view_product'),
    re_path(r'^Owner_product_edit(?P<p_id>[0-9]+)/$',views.Owner_product_edit,name='Owner_product_edit'),
    re_path(r'^edit_product_details(?P<products_id>[0-9]+)$',views.edit_product_details,name='edit_product_details'),
    re_path(r'^delete_product(?P<p_id>[0-9]+)$',views.delete_product,name='delete_product'),
    
    re_path(r'^Owner_logout/$',views.Owner_logout,name='Owner_logout'),

    re_path(r'^User_index/$',views.User_index,name='User_index'),
    re_path(r'^User_home/$',views.User_home,name='User_home'),
    re_path(r'^User_about/$',views.User_about,name='User_about'),
    re_path(r'^User_allbunk/$',views.User_allbunk,name='User_allbunk'),
    re_path(r'^User_contact/$',views.User_contact,name='User_contact'),
    re_path(r'^User_shop/$',views.User_shop,name='User_shop'),
    re_path(r'^User_addcart/$',views.User_addcart,name='User_addcart'),
    re_path(r'^User_booking(?P<i_id>[0-9]+)/$',views.User_booking,name='User_booking'),
    re_path(r'^book_bunk/$',views.book_bunk,name='book_bunk'),
    re_path(r'^User_mybooking/$',views.User_mybooking,name='User_mybooking'),
    re_path(r'^User_payment_history/$',views.User_payment_history,name='User_payment_history'),
    re_path(r'^User_logout/$',views.User_logout,name='User_logout'),

    re_path(r'^SuperAdmin_index/$',views.SuperAdmin_index,name='SuperAdmin_index'),
    re_path(r'^SuperAdmin_home/$',views.SuperAdmin_home,name='SuperAdmin_home'),
    re_path(r'^SuperAdmin_bunkrequest/$',views.SuperAdmin_bunkrequest,name='SuperAdmin_bunkrequest'),
    re_path(r'^SuperAdmin_bunkbookings/$',views.SuperAdmin_bunkbookings,name='SuperAdmin_bunkbookings'),
    re_path(r'^SuperAdmin_ownerview/$',views.SuperAdmin_ownerview,name='SuperAdmin_ownerview'),
    re_path(r'^SuperAdmin_userview/$',views.SuperAdmin_userview,name='SuperAdmin_userview'),
    re_path(r'^SuperAdmin_logout/$', views.SuperAdmin_logout, name='SuperAdmin_logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
