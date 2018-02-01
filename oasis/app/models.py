# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date
from django.db import models

class Txn(models.Model):
	BatchID = models.CharField(max_length=60)
	RowNumInFile = models.IntegerField()
	TxnID = models.CharField(max_length=100)
	AccountID = models.CharField(max_length=50)
	TxnTypeCode = models.CharField(max_length=50)
	PaymentType = models.CharField(max_length=50,default=None)
	Channel = models.CharField(max_length=50,default=None)
	IsForeignTxn = models.CharField(max_length=1)
	IsCashTxn = models.CharField(max_length=1)
	CashInAmount = models.DecimalField(max_digits=19, decimal_places=2)
	CashOutAmount = models.DecimalField(max_digits=19, decimal_places=2,default=None)
	TransferInAmount = models.DecimalField(max_digits=19, decimal_places=2,default=None)
	TransferOutAmount = models.DecimalField(max_digits=19, decimal_places=2,default=None)
	Amount = models.DecimalField(max_digits=19, decimal_places=2,default=None)
	BaseCurrency = models.CharField(max_length=10,default=None)
	CheckNumber = models.CharField(max_length=150,default=None)
	EnteredDate = models.DateField(default=None)
	EffectiveDate = models.DateField(default=date.today)
	ReversalDate = models.DateField(default=None)
	OrginalITxnCode = models.CharField(max_length=50,default=None)
	ApplicationID = models.CharField(max_length=20,default=None)
	SourceSystem = models.CharField(max_length=20)
	UserDefined1 = models.CharField(max_length=255,default=None)
	UserDefined2 = models.CharField(max_length=255,default=None)
	UserDefined3 = models.CharField(max_length=255,default=None)
	UserDefined4 = models.CharField(max_length=255,default=None)
	UserDefined5 = models.CharField(max_length=255,default=None)

	def __unicode__(self):
		return self.TxnID