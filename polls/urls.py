from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('polls.views',
                       
    url(r'^$', 'index', name='polls_index'),
    url(r'^polls/(?P<poll_id>\d+)/$', 'detail', name='polls_detail'),
    url(r'^polls/(?P<poll_id>\d+)/results/$', 'results', name='polls_results'),
    # (r'^$', 'index'),
    # (r'^polls/(?P<poll_id>\d+)/$', 'detail'),
    # (r'^polls/(?P<poll_id>\d+)/results/$', 'results'),
    # (r'^polls/(?P<poll_id>\d+)/vote/$', 'vote'),

)
