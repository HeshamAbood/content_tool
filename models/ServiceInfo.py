
class ServiceInfo():
    
    def __init__(self, serviceId, serviceName, spId, sendingMode, sendingWeekDays, sendTime , status, notifyStatus=False):
        self.serviceId=serviceId
        self.serviceName=serviceName
        self.spId=spId
        self.sendingMode=sendingMode
        self.sendingWeekDays=sendingWeekDays
        self.sendTime=sendTime
        self.status=status
        self.notifyStatus=notifyStatus
        
    def addService(self):
        pass

    def updateService(self):
        pass

    def deleteService(self):
        pass

    def abnormalDynamicContent(self):
        pass

    def noContentuploaded(self):
        pass

