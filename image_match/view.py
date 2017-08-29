# -*- coding: utf-8 -*-

from django.http import *
from django.shortcuts import render
from goods.models import *
import json


def goods(request):
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Cat.objects.all()
    data = {}
    tree = []
    # 第一次迭代，生成一级分类
    for var in list:
        # 一级分类
        if var.parent == 0:
            for one_node in tree:
                if var.cat == one_node['catid']:
                    pass
            else:
                tree.append({'catid': var.cat, 'rank': 1, 'name': var.name, 'children': []})
        data[var.cat] = var.name
    # 第二次迭代，生成二级分类
    for var in list:
        # 二级分类
        for one_node in tree:
            if var.parent == one_node['catid']:
                for two_node in one_node['children']:
                    if var.cat == two_node['catid']:
                        pass
                else:
                    one_node['children'].append({'catid': var.cat, 'rank': 2, 'name': var.name, 'children': []})
    # 第三次迭代，生成三级分类
    for var in list:
        # 三级分类
        for one_node in tree:
            for two_node in one_node['children']:
                if var.parent == two_node['catid']:
                    for three_node in two_node['children']:
                        if var.cat == three_node['catid']:
                            pass
                    else:
                        two_node['children'].append({'catid': var.cat, 'rank': 3, 'name': var.name})
    ret = {
        'tree': json.dumps(tree),
        'cat': data
    }
    return render(request, 'goods.html', ret)


def lists(request):
    page = int(request.POST.get('p'))
    catid = int(request.POST.get('catid'))
    if catid <= 0:
        ret = {'code': 400, 'msg': '请先选择分类', 'data': []}
        return JsonResponse(ret)
    rank = int(request.POST.get('rank'))
    where = {}
    if rank == 1:
        where['one'] = catid
    elif rank == 2:
        where['two'] = catid
    elif rank == 3:
        where['three'] = catid
    # filter相当于SQL中的WHERE，可设置条件过滤结果
    size = 20
    start = 0 if page <= 1 else (page-1)*size
    end = start + size
    lists = Pic.objects.filter(**where)[start:end].values()
    ret = {'code': 200, 'msg': '', 'data': list(lists)}
    return JsonResponse(ret)

