from django.shortcuts import render
from django.shortcuts import redirect
from .models import Friend
from .forms import FriendForm
from django.views.generic import ListView
from django.views.generic import DetailView
from .forms import FindForm
from django.db.models import Q
from django.db.models import Count,Sum,Avg,Min,Max
from .forms import CheckForm


#トップページ・index
def index(request):
    data = Friend.objects.all()
    re1 = Friend.objects.aggregate(Count('age'))
    re2 = Friend.objects.aggregate(Sum('age'))
    re3 = Friend.objects.aggregate(Avg('age'))
    re4 = Friend.objects.aggregate(Min('age'))
    re5 = Friend.objects.aggregate(Max('age'))
    msg = 'count:' +str(re1['age__count']) \
        + '<br>Sum:' +str(re2['age__sum']) \
        + '<br>Average:' +str(re3['age__avg']) \
        + '<br>Min:' +str(re4['age__min']) \
        + '<br>Max:' +str(re5['age__max']) 
    params = {
        'title':'Hello!!',
        'lead':'Django演習をしています。ここには見出しのテキストを入れてみています。<br> \
        改行タグを効かせたい場合は「|safe」を使うそうです。',
        'message': msg,
        # 'form':HelloForm(),
        'data': data,
    }
    return render(request, 'hello/index.html', params)

#フレンドリストの作成
def create(request):
    if (request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title':'Page CreateFriends',
        'form':FriendForm(),
    }
    return render(request, 'hello/create.html', params)

#フレンドリストの編集
def edit(request, num):
    obj = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title':'Page EditFriends',
        'id':num,
        'form':FriendForm(instance=obj),
    }
    return render(request, 'hello/edit.html', params)

#フレンドリストの削除
def delete(request, num):
    friend = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend.delete()
        return redirect(to='/hello')
    params = {
        'title':'Page Delete',
        'id': num,
        'obj': friend,
    }
    return render(request, 'hello/delete.html', params)

#Friendをジェネリックビューで表示する
class FriendList(ListView):
    model = Friend

class FriendDetail(DetailView):
    model = Friend

#フレンドの検索
def find(request):
    if (request.method == 'POST'):
        msg = request.POST['find']
        form = FindForm(request.POST)
        sql = 'select * from hello_friend'
        if (msg != ''):
            sql += ' where ' + msg
        data = Friend.objects.raw(sql)
        msg = sql
        # find = request.POST['find']
        # list = find.split()
        # data = Friend.objects.all()[int(list[0]):int(list[1])]
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
        'title':'Page FindFriends',
        'message':msg,
        'form': form,
        'data': data,
    }
    return render(request, 'hello/find.html', params)

def check(request):
    params = {
    'title':'Page Check',
    'message':'check validation.',
    'form': FriendForm(),
}
    if (request.method == 'POST'):
        obj = Friend()
        form = FriendForm(request.POST, instance=obj)
        params['form'] = form
        if (form.is_valid()):
            params['message'] = 'OK!'
        else:
            params['message'] = 'no good.'
    return render(request, 'hello/check.html', params)


#     sql += ' where ' + msg
# data = Friend.objects.raw(sql)
# msg = sql
# find = request.POST['find']
# list = find.split()
# data = Friend.objects.all()[int(list[0]):int(list[1])]
# else:
#     msg = 'search words...'
#     form = FindForm()
#     data = Friend.objects.all()