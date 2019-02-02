import operator
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from Agentdesks.views import GetPropertyfromRequirements, GetRequirementsfromProperty



urlpatterns = [
        url(r'^get-properties/$', GetPropertyfromRequirements.as_view(), name = 'Agentdesks-get-properties'),
        url(r'^get-requirements/$', GetRequirementsfromProperty.as_view(), name = 'Agentdesks-get-requirements'),
]
