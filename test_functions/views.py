from django.shortcuts import render
from django.views import generic
from django.views import View
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

class IndexView(generic.TemplateView):
    template_name = "test_functions/index.html"

class IndexView(View):
    def get(self, request, *args, **kwargs):
        # 相应地处理GET请求
        print('path info is : ', request.path_info)
        print('method is : ', request.method)
        print('querystring is : ', request.GET)
        print('full path is :', request.get_full_path())
        print('客户端IP is :', request.META['REMOTE_ADDR'])

        total_sum = 0
        for key, value in request.GET.items():
            try:
                total_sum += float(value)
            except ValueError:
                continue

        return HttpResponse(f'test request, your sum is {total_sum}')
