# NEW AP
import application.Controller.PushController as PushController # 11.03.63 AP
import application.Controller.AutoSystemController as AutoSystemController # 12.03.63 AP
import application.Controller.JoinController as JoinController # 12.03.63 AP
import application.Controller.ServiceController as ServiceController # 13.03.63 AP
import application.Controller.HelpController as HelpController # 13.03.63 AP

class _loadController(object):
    def __init__(self,msg):
        PushController.PushController(msg)
        AutoSystemController.AutoSystemController(msg)
        JoinController.JoinController(msg)
        ServiceController.ServiceController(msg)
        HelpController.HelpController(msg)