import json
import requests
import pytz
import application.Config.config as _config
Conf = _config.config

class JoinController(object):
    def __init__(self,msg):
        try: 
            if msg.type == 26:
                TOGROUP = msg.message.to
                txt = msg.message.text.lower()
                _txt = txt.strip()
                if _txt == '=: invit' and msg.message.to == str(msg.autoload._config._allow_group()):
                    JoinController.AutoJoinGroup(msg)
                elif _txt == 'login':
                    JoinController.Login(msg)
                elif _txt == 'update':
                    JoinController.Update(msg)
                elif _txt == 'total':
                    JoinController.Total(msg)

        except Exception as err:
            print('error ',err)

    def Total(self):
        try: 
            # gid = self.message.to
            gid = self.mybot.getGroupIdsJoined()
            members = len(gid)
            if members <= 100:
            	print('',members)
            else:
            	print('MAX USER')
        except Exception as err:
            print('error ',err)

    def AutoJoinGroup(self):
        try: 
            gid = self.mybot.getGroupIdsJoined()
            members = len(gid)
            if members <= 100:
                group_invit = self.mybot.getGroupIdsInvited()
                if len(group_invit) > 0:
                    for e in group_invit:
                        _invit = self.mybot.acceptGroupInvitation(e)
                        gid = e
                        v = str(Conf._version())
                        res = requests.get(str(self.autoload._config._url_api())+"/get_user_filter.php?gid="+gid+"&p="+str(self.autoload._config._name()))
                        result = res.json()
                        if len(result) == 1:
                            if result[0]['groupline_key'] == gid:
                                if result[0]['groupline_access'] == 'active':
                                    print('active')
                                    if result[0]['groupline_version'] == v:
                                        print('active working')
                                        self.mybot.sendMessage(e,"บอทกลับมาทำงานแล้ว ผลจะมาในรอบถัดไป")
                                    elif result[0]['groupline_version'] != v:
                                        self.mybot.sendMessage(e,"บอทกลับมาทำงานแล้ว แต่ดูเหมือนกันมีข้อมูลไม่ตรงกัน กรุณา พิม update เพื่อปรับข้อมูลให้ตรง")
                                        print('active and change version for work')
                                elif result[0]['groupline_access'] == 'padding':
                                    print('show msg install')
                                    self.mybot.sendMessage(e,"กรุณาพิม\n\nhy:active\n\nเพื่อเปิดใช้งานบอท")
                                elif result[0]['groupline_access'] == 'missing':
                                    print('you move bot another group')
                                    self.mybot.sendMessage(e,"กลุ่มนี้ได้ถูกแย้งย้ายแล้ว")
                                elif result[0]['groupline_access'] == 'stop':	
                                    print('expire date')
                                    self.mybot.sendMessage(e,"วันใช้งานหมดแล้ว ติดต่อ line://ti/p/~@mybot เพื่อใช้งานต่อ")
                            else:
                                print('false')
                        else:
                            print('not register')
                            self.mybot.sendMessage(e,"ดูเหมือนว่าจะยังไม่ได้ลงทะเบียนบอท\nกรุณาพิม\n\nLogin\n\nเพื่อลงทะเบียนบอท")
                
        except Exception as err:
            print('error ',err)

    def Login(self):
        try: 
            gid = self.message.to
            ginfo = self.mybot.getGroup(gid)
            res = requests.get(str(self.autoload._config._url_api())+"/insert_group_login.php?gid="+gid+"&p="+str(self.autoload._config._name())+"&v="+str(self.autoload._config._version())+"&name="+ginfo.name)
            result = res.json()
            if result['status'] == True : # ยังไม่มีกลุ่ม 
                self.mybot.sendMessage(self.message.to,"✅ลงทะเบียนสำเร็จ")
                # group = self.mybot.getGroup(self.message.to)
                self.mybot.sendMessage(self.message.to, "กรุณาพิม\n\nuwin:active\n\nเพื่อเปิดใช้งานบอท")
            else :
                self.mybot.sendMessage(self.message.to,"❌ไม่ต้องลงทะเบียนซ้ำ")
                # group = self.mybot.getGroup(self.message.to)
        except Exception as err:
            print('error ',err)

    def Update(self):
        try: 
            gid = self.message.to
            res = requests.get(str(self.autoload._config._url_api())+"/update.php?gid="+gid+"&v="+str(self.autoload._config._version())+"&p="+str(self.autoload._config._name()))
            result = res.json()
            if result['status'] == True : # ยังไม่มีกลุ่ม 
                self.mybot.sendMessage(self.message.to,"✅เปลี่ยนตัวบอทสำเร็จ")
                group = self.mybot.getGroup(self.message.to)
            else :
                self.mybot.sendMessage(self.message.to,"❌เกิดข้อผิดพลาด")
                group = self.mybot.getGroup(self.message.to)
        except Exception as err:
            print('error ',err)




