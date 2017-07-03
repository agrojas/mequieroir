from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<id>[0-9]+)/results/$', views.results, name='results'),
    #   /1/proposal/4 y agregue la propuesta 4 al user 1
    url(r'^(?P<id>[0-9]+)/proposal/(?P<proposalId>[0-9]+)$', views.addProposal, name='addProposal'),
]
