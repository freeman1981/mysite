from django.conf.urls import url, include
from myapp.api import EntryResource, UserResource
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(EntryResource())

urlpatterns = [
    # The normal jazz here...
    url(r'^api/', include(v1_api.urls)),
]
