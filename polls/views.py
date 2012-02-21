# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response,  get_object_or_404
from django.core.urlresolvers import reverse
#from the polls directory models file to the class Poll
from polls.models import Poll, Choice

def index(request):
  '''
  <explanation> 
  fetching polls from the database table Polls(models class Poll)  
  and then passing all the data to index.html for display on clients side.
  </explanation>
  output = ','.join([p.question for p in latest_poll_list])
  return HttpResponse(output)
  ordered by publish date, and only 5 items
  latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
  t = loader.get_template('polls/index.html')
  c = Context({
  what variables in the templates to what values you want to pass to them  
  'latest_poll_list': latest_poll_list
  })
  #return HttpResponse(t.render(c))
  '''

  latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
  return render_to_response('index.html',{'latest_poll_list': latest_poll_list})


def detail(request, poll_id):
  '''
  <explanation>
  the detail method would show the detail of the poll which user clicks, 
  for that purpose it has a poll_id parameter as input, it then passes this parameter to detail.html 
  which eventually shows the details of the polls (the four option to the questions and the radio box)

  the variable p is the primary key, as returned from the index page. 
  now that value is assigned to 'poll' in the next line.
  </explanation>
  '''
  p = get_object_or_404(Poll, pk=poll_id)
  return render_to_response('detail.html', {'poll': p},
                            context_instance=RequestContext(request))

def results(request, poll_id):
  p = get_object_or_404(Poll, pk=poll_id)
  return render_to_response('results.html', {'poll': p})  


def vote(request, poll_id):
  p = get_object_or_404(Poll, pk=poll_id)
  try:
    selected_choice = p.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    # Redisplay the poll voting form.
    return render_to_response('detail.html', {
        'poll': p,
        'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
  else:
    selected_choice.votes += 1
    selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))
