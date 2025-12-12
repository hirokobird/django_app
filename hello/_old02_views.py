from django.shortcuts import render
from django.shortcuts import redirect
from .models import Friend
from .forms import FriendForm
from django.views.generic import ListView
from django.views.generic import DetailView
from .forms import FindForm
from django.db.models import Q
# from .forms import HelloForm

#トップページ・index
def index(request):
    data = Friend.objects.all().values('id', 'name', 'gender', 'age')
    params = {
        'title':'Hello!!',
        'lead':'Django演習をしています。ここには見出しのテキストを入れてみています。<br> \
        プログラム同士の関係を理解するのがなかなか難しいです<br>  \
        改行タグを効かせたい場合は「|safe」を使うそうです。',
        # 'message': 'all friends',
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
        # name = request.POST['name']
        # mail = request.POST['mail']
        # gender = 'gender' in request.POST
        # age = int(request.POST['age'])
        # birth = request.POST['birthday']
        # friend = Friend(name=name, mail=mail, gender=gender, \
        #     age=age, birthday=birth)
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
        msg = 'search result:'
        form = FindForm(request.POST)
        find = request.POST['find']
        list = find.split()
        data = Friend.objects.filter(name__in=list)

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

# def __new_str__(self):
#     result = ''
#     for item in self:
#         result += '<tr>'
#         for k in item:
#             result += '<td>' + str(k) + '=' + str(item[k]) + '</td>'
#         result += '</tr>'
#     return result

# QuerySet.__str__ = __new_str__

    # if (request.method == 'POST'):
    #     num=request.POST['id']
    #     item = Friend.objects.get(id=num)
    #     params['data'] = [item]
    #     params['form'] = HelloForm(request.POST)
    # else:
    #     params['data'] = Friend.objects.all()