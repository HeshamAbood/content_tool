class ContentInfo():

    def __init__(self, contentId, contentName, serviceId, validTime, expireTime, createTime, contentType,
                 contentStatus):
        self.contentId = contentId
        self.contentName = contentName
        self.serviceId = serviceId
        self.validTime = validTime
        self.expireTime = expireTime
        self.createTime = createTime
        self.contentType = contentType
        self.contentStatus = contentStatus

    def __init__(self):
        self.contentStatus = 1

    def save(self):
        pass

    def delete(self):
        pass
    def add(self):
        pass
