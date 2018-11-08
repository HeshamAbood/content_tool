import sqlite3

conn = sqlite3.connect("database.db")
c=conn.cursor()


class ServiceProvider:

    def __init__(self, spid, email, status, notificationEmail, notifyStatus=False):
        self.spid=spid
        self.email=email
        self.status=status
        self.notificationEmail=notificationEmail
        self.notifyStatus=notifyStatus

    def sendNotifyEmail(self):
        pass

    def getSPServices(self):
        sql="SELECT * FROM serviceinfo where spid={}".format(self.spid)
        n=c.execute(sql)
#       check for empty result and return 0

        return n

    def update(self):
        return c.execute("UPDATE ServiceProvider SET email={}, status={}, notificationEmail={}, notifyStatus={} where spid={}"
                 .format(self.email,self.status,self.notificationEmail,self.notifyStatus,self.spid))

    def save(self):
        return c.execute("INSERT INTO  ServiceProvider  VALUES({},{},{},{},{})"
                 .format(self.spid,self.email,self.status,self.notificationEmail,self.notifyStatus))

    def delete(self):
        return c.execute("DELETE FROM ServiceProvider where spid={}".format(self.spid))


