from django.http import HttpResponse
from .core.dataset import DataSet
from .core.sql.SQLExec import SQLExec
from .core.sql.SQLQuery import SQLQuery
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def search(request):
    if request.method == 'GET':
        return HttpResponse("Got get")
    elif request.method == 'POST':
        params = json.loads(request.body.decode("utf-8"))
        ds = DataSet()
        ds.init(params)
        query = SQLQuery()
        ds.generateQuery(query)
        sql = query.build()
        sqlExec = SQLExec()
        results = sqlExec.exec(query)
        return HttpResponse(results)