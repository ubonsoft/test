from linepy import *
from datetime import datetime
# from time import sleep
import time
import json
import application.Controller._loadController as load
import application.Config.autoload as Autoload
_autoload = Autoload.autoload
import application.Config.config as Config
_config = Config.config
_autoload._config = _config
# mybot = LINE(_config._Email_Pass()[0],_config._Email_Pass()[1])
mybot = LINE(_config._token())
# tokens = "{token : "+mybot.authToken+"}"
# with open('tokens.json', 'w') as outfile:
#     json.dump(tokens, outfile)

mybotMID = mybot.profile.mid
mybotProfile = mybot.getProfile()
lineSettings = mybot.getSettings()
oepoll = OEPoll(mybot)

def logError(text):
    mybot.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
      
#==============================================================================#
def lineBot(op):
    try:
        op.mybot = mybot
        op.autoload = _autoload
        # example use => self.autoload._config._name()
        load._loadController(op)   
    except Exception as error:
        logError(error)
#==============================================================================#

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)


























