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
from django.core.paginator import Paginator


#トップページ・index
def index(request, num=1):
  data = Friend.objects.all()
  page = Paginator(data, 3)
  params = {
    'title': 'Hello',
    'message':'',
    'data': page.get_page(num),
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