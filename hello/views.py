from django.shortcuts import render
from django.shortcuts import redirect
from .models import Friend
from .forms import HelloForm

def index(request):
    # num = Friend.objects.all().count()
    # first = Friend.objects.all().first()
    # last = Friend.objects.all().last()
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

#Create Model
def create(request):
    params = {
        'title':'Create',
        'form':HelloForm(),
    }
    if (request.method == 'POST'):
        name = request.POST['name']
        mail = request.POST['mail']
        gender = 'gender' in request.POST
        age = int(request.POST['age'])
        birth = request.POST['birthday']
        friend = Friend(name=name, mail=mail, gender=gender, \
            age=age, birthday=birth)
        friend.save()
        return redirect(to='/hello')
    return render(request, 'hello/create.html', params)

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