from  models.ContentInfo import *


class DynamicContent(ContentInfo):

    def __init__(self, contentId, contentName, serviceId, validTime, expireTime, createTime, contentType, contentStatus, dynamicContentId,remoteFile):
        super(ContentInfo, self).__init__(contentId, contentName, serviceId, validTime, expireTime, createTime, contentType, contentStatus)
        self.dynamicContentId=dynamicContentId
        self.remoteFile=remoteFile

    def getContentDetail(self):
        pass

    def recentAbnormal(self):
        pass

    def addRemoteContent(self, C):
        pass

    def updateRemoteContent(self):
        pass

    def deleteRemoteContent(self):
        pass

