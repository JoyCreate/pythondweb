from django.conf.urls import *
from django.http import HttpResponse
from TestModel.models import Test
# 数据库操作
def testdb(request):
    test1 = Test(name='runoob')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")
def selectdb(request):
    response=''
    response1=''
    list=Test.objects.all()
    response2=Test.objects.filter(id=1)
    response3=Test.objects.get(id=1)
    Test.objects.order_by('name')[0:2]
    Test.objects.order_by('id')
    Test.objects.filter(name="runoob").order_by("id")
    # 输出所有数据
    for var in list:
        response1 += var.name + " "
        response = response1
    return HttpResponse("<p>" + response + "</p>")

def updatedb(request):
    test1 = Test.objects.get(id=1)
    test1.name = 'Google'
    test1.save()
    # 另外一种方式
    #Test.objects.filter(id=1).update(name='Google')
    # 修改所有的列
    # Test.objects.all().update(name='Google')
    return HttpResponse("<p>修改成功</p>")

def deletedb(request):
    test1 = Test.objects.get(id=2)
    test1.delete()
    # 另外一种方式
    # Test.objects.filter(id=1).delete()
    # 删除所有数据
    # Test.objects.all().delete()
    return HttpResponse("<p>删除成功</p>")