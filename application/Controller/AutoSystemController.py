import json
from json import dumps
import requests
import application.Config.config as _config
Conf = _config.config

class AutoSystemController(object):
    def __init__(self,msg):
        try: 
            if msg.type == 26:
                TOGROUP = msg.message.to
                txt = msg.message.text.lower()
                _txt = txt.strip()
                # if _txt == '=: getuser' and msg.message.to == str(msg.autoload._config._allow_group()):
                if _txt == '.: load':
                    AutoSystemController.getGroups(msg)
        except Exception as err:
            print('error ',err)

    def getGroups(self):
        try: 
            group_join = self.mybot.getGroupIdsJoined()
            print("total Group="+str(len(group_join)))
            for i in range(len(group_join)):
                ginfo = self.mybot.getGroup(group_join[i])
                _name = ginfo.name
                print('finish='+str(_name))
                _pictureStatus = ginfo.pictureStatus
                _members = len(ginfo.members)
                _person = ginfo.members
                url = 'http://at-mybot.me/api/py/forbot/manager_bot/groups.php'
                headers = {'content-type': "application/x-www-form-urlencoded",'cache-control': "no-cache",'postman-token': "ded67b5e-39f4-a37c-dffa-d735f6734a04"}
                data_json =  '{}'
                data_set = json.loads(data_json)
                for ii in _person:
                    Pname = ii.displayName.replace('"', "")
                    data_add = { ii.mid :{'mid': ii.mid, 'name': Pname,'picture':ii.pictureStatus,'status':ii.statusMessage}}
                    data_set.update(data_add)
                data_set = dumps(data_set)
                requests.post(url, data={'gid':str(group_join[i]),'name' :str(_name),'products':str(self.autoload._config._name()),'members':str(_members),'version':str(self.autoload._config._version()),'picture' : str(_pictureStatus),'_json': str(data_set)}, headers=headers,timeout=5)
        except Exception as err:
            print('error ',err)
        