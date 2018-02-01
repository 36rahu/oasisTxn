# -*- coding: utf-8 -*-
import json

from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import HttpResponse
from django.forms.models import model_to_dict
from models import Txn
# Create your views here.
from datetime import datetime
from datetime import date
from decimal import Decimal

class DatetimeEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, datetime):
			return obj.strftime('%Y-%m-%dT%H:%M:%SZ')
		elif isinstance(obj, date):
			return obj.strftime('%Y-%m-%d')
			# Let the base class default method raise the TypeError
		return json.JSONEncoder.default(self, obj)

class GetTxnID(APIView):
	
	def get(self, request,format=None):
		txn_id = request.GET.get('id', '')
		txn_object = Txn.objects.get(TxnID=txn_id)
		txn_data = model_to_dict(txn_object)
		txn_data_ = dict((k,str(v)) if isinstance(v,Decimal) else (k,v) for k,v in txn_data.items())
		data = {'status':200,'data':txn_data_}
		return HttpResponse(json.dumps(data,cls=DatetimeEncoder),content_type="application/json")