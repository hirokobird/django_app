from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import TemplateView

from .forms import SessionForm

class HelloView(TemplateView):

    def __init__(self):
        self.params = {
            'title':'Hello！',
            'lead':'Django演習をしています。ここには見出しのテキストを入れてみています。<br> \
            プログラム同士の関係を理解するのがなかなか難しいです<br>  \
            改行タグを効かせたい場合は「|safe」を使うそうです。',
            'form': SessionForm(),
            'result':None
        }
    
    def get(self, request):
        self.params['result'] = request.session.get('last_msg', 'No message')
        return render(request, 'hello/index.html', self.params)
    
    def post(self, request):
        ses = request.POST['session']
        result = '<ol class="list-group"><b>selected:<b>'
        self.params['result'] = 'send:"' + ses + '"."'
        request.session['last_msg'] = ses
        self.params['form'] = SessionForm(request.POST)
        return render(request, 'hello/index.html', self.params)

def sample_middleware(get_response):

    def middleware(request):
        counter = request.session.get('counter', 0)
        request.session['counter'] = counter + 1
        response = get_response(request)
        print("count: " + str(counter))
        return response

    return middleware


# if ('check' in request.POST):
#     self.params['result'] = 'Checked!!'
# else:
#     self.params['result'] = 'not checked...'
# self.params['form'] = HelloForm(request.POST)
# return render(request, 'hello/index.html', self.params)


# msg = 'あなたは<b>' + request.POST['name'] + \
# '(' + request.POST['age'] + ')</b>さんです。 <br>メールアドレスは<b>' \
# + request.POST['mail'] + '</b>ですね。'
# self.params['message'] = msg
# self.params['form'] = HelloForm(request.POST)
# return render(request, 'hello/index.html', self.params)    