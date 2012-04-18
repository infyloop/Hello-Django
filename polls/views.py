# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response,  get_object_or_404
from django.core.urlresolvers import reverse
#from the polls directory models file to the class Poll
from polls.models import Poll, Choice
from forms import *

def index(request):
  latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
  return render_to_response('index.html',{'latest_poll_list': latest_poll_list})


def detail(request, poll_id):
  p = get_object_or_404(Poll, pk=poll_id)
  if request.method == 'POST':
    form = PollForm(request.POST, instance=p)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('polls_results', kwargs={'poll_id': p.id}))
  else:
      form = PollForm(instance=p)

  return render_to_response('detail.html', {
        'poll': p,
        'form': form,
        }, context_instance=RequestContext(request))


def results(request, poll_id):
  p = get_object_or_404(Poll, pk=poll_id)
  return render_to_response('results.html', {'poll': p})  

