# Third Party Stuff
from django.urls import (
    include,
    path,
    re_path, )
from django.views import defaults as dj_default_views
from rest_framework import routers
from django.contrib import admin

# CRM Service Stuff
from crm_service import settings
from customers import views
from base import views as base_views


handler500 = base_views.server_error

router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]

if settings.DEBUG:  # pragma: no cover
    # Live reloading
    urlpatterns += [
        re_path(r'^400/$', dj_default_views.bad_request, kwargs={'exception': Exception("Bad Request!")}),
        re_path(r'^403/$', dj_default_views.permission_denied, kwargs={'exception': Exception("Permission Denied!")}),
        re_path(r'^404/$', dj_default_views.page_not_found, kwargs={'exception': Exception("Not Found!")}),
        re_path(r'^500/$', handler500),
    ]
