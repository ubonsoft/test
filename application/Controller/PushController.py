import json
import time as t
from datetime import datetime
import pytz
import requests
import application.Config.config as _config
Conf = _config.config
import application.View.Theme as Theme
Theme = Theme.Theme

class PushController(object):
    def __init__(self,msg):
        try: 
            if msg.type == 26:
                TOGROUP = msg.message.to
                txt = msg.message.text.lower()
                txt_ = txt.strip()
                if txt_ == '=: push_uwin789' and msg.message.to == str(msg.autoload._config._allow_group()):
                    t.sleep(20)
                    tz_NY = pytz.timezone('Asia/Bangkok') 
                    datetime_NY = datetime.now(tz_NY)
                    HH = datetime_NY.strftime("%H")
                    MM = datetime_NY.strftime("%M")
                    PushController._Push(msg)
                if txt_ == '.uwin' :
                    tz_NY = pytz.timezone('Asia/Bangkok') 
                    datetime_NY = datetime.now(tz_NY)
                    HH = datetime_NY.strftime("%H")
                    MM = datetime_NY.strftime("%M")
                    PushController._Push(msg)
                elif txt_ == '=: push_overtime_uwin789' and msg.message.to == str(msg.autoload._config._allow_group()):
                    tz_NY = pytz.timezone('Asia/Bangkok') 
                    datetime_NY = datetime.now(tz_NY)
                    HH = datetime_NY.strftime("%H")
                    MM = datetime_NY.strftime("%M")
                    PushController._PushOverTime(msg)
        except Exception as err:
            print('error ',err)


    def _Push(self):
        try: 
            print(str(self.autoload._config._name()))
            tz_NY = pytz.timezone('Asia/Bangkok') 
            # show footer time
            now1 = datetime.now(tz_NY)
            month_name = 'x มกราคม กุมภาพันธ์ มีนาคม เมษายน พฤษภาคม มิถุนายน กรกฎาคม สิงหาคม กันยายน ตุลาคม พฤศจิกายน ธันวาคม'.split()[now1.month]
            thai_year = now1.year + 543
            time_str = now1.strftime('%H:%M:%S')
            show_date = "%d %s %d"%(now1.day, month_name, thai_year) # 30 ตุลาคม 2560 # disabled -> 20:45:30

            datetime_NY = datetime.now(tz_NY)
            HM = datetime_NY.strftime("%H:%M")
            time = requests.get(str(self.autoload._config._url_api())+'/uwin789/time.json')
            _time = time.json()
            result = ''
            maxloop = 1
            while True :
              print("pre load")
              t.sleep(1)
              print("suf load")
              print(maxloop)
              res = requests.get(str(self.autoload._config._url_loop_api())+'/uwin789_50line.php?loop='+_time[HM])
              print(res.status_code)
              result = res.json()
              fix = ''
              for x in result:
                fix = str(x['lottery_loop_3unit'])
              if fix.strip() != '' and fix != 'xxx' and int(res.status_code) == 200:
                break
              if maxloop == 50:
                break
              maxloop += 1
            print(str(self.autoload._config._name()))
            users = requests.get(str(self.autoload._config._url_api())+'/get_users.php?v='+str(self.autoload._config._version())+'&p='+str(self.autoload._config._name()))
            _users = users.json()
            for _u in _users:
            	try:
                    text_header = ''
                    if _u['groupline_name'] != None:
                        text_header = str(_u['groupline_name'])
                    text_msg = ''
                    if _u['groupline_text'] != None:
                        text_msg = str(_u['groupline_text'])
                    text_view = str(_u['groupline_view'])
                    _block = str(_u['groupline_block'])
                    try:
                        text_header_filter = text_header.replace('?','')
                        if _u['groupline_theme'] == 'single':
                        	rwsult = Theme.show_1_loop(result,str(text_header_filter),show_date,_time,text_msg,str(text_view),_block)
                        elif _u['groupline_theme'] == '5line':
                        	rwsult = Theme.show_5_loop(result,str(text_header_filter),show_date,_time,text_msg,str(text_view),_block)
                        elif _u['groupline_theme'] == '10line':
                        	rwsult = Theme.show_multi_loop(result,str(text_header_filter),show_date,_time,text_msg,str(text_view),_block,10)
                        elif _u['groupline_theme'] == '15line':
                        	rwsult = Theme.show_multi_loop(result,str(text_header_filter),show_date,_time,text_msg,str(text_view),_block,15)
                        elif _u['groupline_theme'] == '20line':
                        	rwsult = Theme.show_multi_loop(result,str(text_header_filter),show_date,_time,text_msg,str(text_view),_block,20)
                        elif _u['groupline_theme'] == '25line':
                        	rwsult = Theme.show_multi_loop(result,str(text_header_filter),show_date,_time,text_msg,str(text_view),_block,25)
                        elif _u['groupline_theme'] == '30line':
                        	rwsult = Theme.show_multi_loop(result,str(text_header_filter),show_date,_time,text_msg,str(text_view),_block,30)
                        elif _u['groupline_theme'] == '40line':
                        	rwsult = Theme.show_multi_loop(result,str(text_header_filter),show_date,_time,text_msg,str(text_view),_block,40)
                        elif _u['groupline_theme'] == '50line':
                        	rwsult = Theme.show_multi_loop(result,str(text_header_filter),show_date,_time,text_msg,str(text_view),_block,50)
                        self.mybot.sendMessage(_u['groupline_key'], rwsult)
                    except Exception as err:
                        requests.get('http://at-mybot.me/api/py/forbot/missing.php?gid='+str(_u['groupline_key'])+'&p='+str(self.autoload._config._name())+'&v='+str(self.autoload._config._version()))
                        print('error PUSH',err)
            	except Exception as err:
                    print('error ',err)
        except Exception as err:
            print('error ',err)
    def _PushOverTime(self):
        try: 
            users = requests.get(str(self.autoload._config._url_api())+'/get_users.php?v='+str(self.autoload._config._version())+'&p='+str(self.autoload._config._name()))
            _users = users.json()
            for _u in _users:
            	try: 
            		if str(_u['groupline_over_alert']) == 'on':
            			self.mybot.sendMessage(_u['groupline_key'], "อีก 1 นาทีผลออก")
            	except Exception as err:
            		print('error ',err)
        except Exception as err:
            print('error ',err)



