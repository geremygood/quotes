from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.conf import settings

from api.models import Quote

from django.http import HttpResponse

def index(request):
    latest_quote_list = Quote.objects.all().order_by('?')[:1]
    t = loader.get_template('index.html')
    c = Context({
        'latest_quote_list': latest_quote_list,
    })
    return HttpResponse(t.render(c))

def detail(request, api_quote_id):
    q = get_object_or_404(Quote, pk=api_quote_id)
    return render_to_response('detail.html', {'quote': q})
