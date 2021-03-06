from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns('',
    url(r'^$', 'account.views.index',name="account"),
    url(r'^index/$', 'account.views.index', name="account_index"),
    url(r'^search/$', 'account.views.search', name="account_search"),
    url(r'^add/$', 'account.views.add',name="account_add"),
    url(r'^delete/(?P<user_id>\d+)/$', 'account.views.delete',name="account_delete"),
    url(r'^edit/(?P<user_id>\d+)/$', 'account.views.edit',name="account_edit"),
    
)