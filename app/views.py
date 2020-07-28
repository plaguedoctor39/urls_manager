import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render


def file_list(request, date=None):
    template_name = 'index.html'

    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    list_dir = os.listdir('files')
    files = []

    for file in list_dir:
        file_stat = os.stat(f'files/{file}')
        ctime_td = datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=file_stat.st_ctime)
        mtime_td = datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=file_stat.st_mtime)

        files.append({'name': f'{file}',
                      'ctime': ctime_td,
                      'mtime': mtime_td})
        print(ctime_td)

    context = {
        'files': files,
        'date': date  # Этот параметр необязательный
    }
    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    with open(f'files/{name}', 'r') as f:
        content = f.read()
    return render(
        request,
        'file_content.html',
        context={'file_name': f'files/{name}', 'file_content': f'{content}'}
    )
