"""th URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# from Data_Interaction.admin import admin_site
from django.urls import path


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from Data_Interaction import views
from rest_framework.routers import DefaultRouter,SimpleRouter
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from django.urls import re_path as url 

from knox import views as knox_views

admin.site.site_header = 'VANTHAI'                    # default: "Django Administration"
admin.site.index_title = 'Site VANTHAI'                 # default: "Site administration"
admin.site.site_title = 'VANTHAI site admin' # default: "Django site admin"

router = DefaultRouter()
# # router = SimpleRouter()
# # router.register('api.check_list_category', views.check_list_category)
# router.register('user',views.UserViewSet)
# # router.register('usercheckmail',views.EmailViewSet)
# router.register('listproduct',views.ListProductViewSet)
# router.register('listcategory',views.CategoryProductViewSet)
router.register('admininfor',views.AdminInformationViewSet)
# router.register('personaltransactionhistory',views.PersonalTransactionHistoryViewSet)
# router.register('personalhistory',views.PersonalViewSet)
# # router.register('resetpassword',views.ResetPasswordViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('admin/', admin_site.urls),

    path('', include(router.urls)),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('createuser/',views.create_user),
    path('login/', views.login_api),
    path('keeplogin/', views.keep_login),
    path('changepassword/', views.change_password),
    path('changemoney/', views.change_money),
    path('transactionhistoryuser/', views.transaction_history_user),
    path('bankinfor/', views.bank_infor),
    path('sendrechargedata/', views.send_recharge_data),

    path('filteruser/', views.loc_usernam_vs_mail),
    path('sendotp/', views.gui_OTP_den_user),
    path('compareotp/', views.so_sanh_OTP),
    path('resetpassword/', views.reset_password),

    path('statistical_server_user/', views.statistical_server_user),
    path('statistical_server_money/', views.statistical_server_money),

    path('product_home_page/', views.product_home_page),
    path('api.check_list_category', views.check_list_category),
    path('api.check_list_product', views.check_list_product),
    path('api.check_list_product_one', views.check_list_product_one),
    path('api.check_money_user', views.check_money_user),


    path('buydata/', views.mua_hang),
    path('downloadfiletxt/', views.down_load_txt),
    # path('api/auth/login', knox_views.LoginView.as_view()),
    # path('api/logoutknox', knox_views.LogoutView.as_view()),
    # path('api/logoutknox', knox_views.LogoutView.as_view()),

    url(r'user/auth/', include('knox.urls')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
