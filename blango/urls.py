import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
import blango_auth.views
from blog.views import post_table

# print(f"Time zone: {settings.TIME_ZONE}")


"""blango URL Configuration

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
from django.urls import path, include
from blog.views import IndexTemplateView, post_detail, index, get_ip
from django_registration.backends.activation.views import RegistrationView
from blango_auth.forms import BlangoRegistrationForm

# it's better to make separate urls file for each app 
urlpatterns = [
    path('admin/', admin.site.urls),
    # path("", IndexTemplateView.as_view(), name="index"),
    path("", index, name="index"),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path(
    "accounts/register/",
    RegistrationView.as_view(form_class=BlangoRegistrationForm),
    name="django_registration_register",
),
    
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", blango_auth.views.profile, name="profile"),
    path('post/<str:slug>/', post_detail, name="blog-post-detail"),
    path("post-table/",post_table, name="blog-post-table"),
    path("ip/", get_ip),
    path("api/v1/", include("blog.api.urls")),
    

]
if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


