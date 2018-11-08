import sqlite3
from .models.ContentInfo import *
from .models.ServiceProvider import *
from .models.ServiceInfo import *

from csv import DictReader
from datetime import datetime
from pytz import UTC


DATETIME_FORMAT = '%Y-%m-%d %HH:%MM:%SS'

conn = sqlite3.connect("database.db")
c=conn.cursor()

def addSPs():
#    def __init__(self, spid, email, status, notificationEmail, notifyStatus=False):
    for row in DictReader(open('./spinfo.csv')):
        sp = ServiceProvider()
        sp.spid = row['spid']
        sp.email = row['email']
        sp.status = row['status']
        sp.notificationEmail = row['notificationEmail']
        sp.notifyStatus = row['notifyStatus']
        sp.save()

    c.commit()

def addServices():
# serviceId, serviceName, spId, sendingMode, sendingWeekDays, sendTime , status, notifyStatus

    for row in DictReader(open('./serviceinfo.csv')):
        s = ServiceInfo()
        s.serviceId = row['serviceId']
        s.serviceName = row['email']
        s.spId = row['status']
        s.sendingMode = row['sendingMode']
        s.sendingWeekDays = row['sendingWeekDays']
        s.status = row['status']
        s.notifyStatus = row['notifyStatus']
        rawSendTime = row['validTime']
        send = UTC.localize(
            datetime.strptime(rawSendTime, DATETIME_FORMAT))
        s.validTime = send
        s.sendTime = row['sendTime']

        s.addService()

    c.commit()


def addContents():
    #c.execute("INSERT INTO contentinfo VALUES(123, 'TEST', 123, validTime, expireTime, createTime, 1, 1)")

    for row in DictReader(open('./contentinfo.csv')):
        content = ContentInfo()
        content.contentId = row['contentId']
        content.contentName = row['contentName']
        content.serviceId = row['serviceId']
        content.contentType = row['contentType']
        content.contentStatus = row['contentStatus']

        rawValidTime = row['validTime']
        valid = UTC.localize(
            datetime.strptime(rawValidTime, DATETIME_FORMAT))
        content.validTime = valid
        rawExpireTime = row['validTime']
        expire = UTC.localize(
            datetime.strptime(rawExpireTime, DATETIME_FORMAT))
        content.expireTime = expire
        rawCreateTime = row['createTime']
        create = UTC.localize(
            datetime.strptime(rawCreateTime, DATETIME_FORMAT))
        content.createTime = create
        content.save()

    c.commit()


addSPs()
addContents()
c.close()