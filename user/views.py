from rest_framework.decorators import api_view
from rest_framework.response import Response

from user.models import User

from user.serializers import UserSerializer


@api_view(['GET'])
def get_user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_user(request):
    print(request.data)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=200, data={"message": "插入数据成功"})
    else:
        return Response(status=200, data={"message": "传入数据格式不正确"})


@api_view(['GET', 'DELETE'])
def user_detail(request, id):
    try:
        u = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=200, data={"message": "该id用户不存在"})
    if request.method == 'GET':
        ser = UserSerializer(u)
        return Response(data=ser.data)
    if request.method == 'DELETE':
        u.delete()
        return Response(status=200, data={"message": "删除成功"})


@api_view(['POST'])
def mod_user(request):
    print(request.data)
    uid = request.data.get("id")
    name = request.data.get("name")
    age = request.data.get("age")
    gender = request.data.get("gender")
    print(User.objects.filter(id=uid).query)
    User.objects.filter(id=uid).update(name=name, age=age, gender=gender)
    return Response(status=200, data={"message": "插入数据成功"})
    # return Response(status=200, data={"message": "插入数据错误"})
