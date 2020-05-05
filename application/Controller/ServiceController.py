from datetime import datetime
import pytz
import time as t
import application.Config.config as _config
Conf = _config.config
import json
import time as t
import requests

class ServiceController(object):
    def __init__(self,msg):
        if msg.type == 26:
            txt = msg.message.text.lower()
            txt_ = txt.strip()
            if txt_ == 'gid':
                ServiceController._GID(msg)
            elif txt_ == 'total':
                ServiceController._Total(msg)
            elif txt_ == 'luwin1':
                ServiceController._LEAVE(msg)
            elif txt_ == '@@' or txt_ == 'uwin@':
                ServiceController.TagMember(msg)
            elif txt_ == 'uwinw:on':
                ServiceController._SetWelcome_ON(msg)
            elif txt_ == 'uwinw:off':
                ServiceController._SetWelcome_OFF(msg)
            elif txt_ == 'uwin:start':
                ServiceController._Hon(msg)
            elif txt_ == 'uwin:stop':
                ServiceController._Hoff(msg)
            elif txt_ == 'uwin:active':
                ServiceController.bot_active(msg)
            elif txt_ == 'uwina:on':
                ServiceController.bot_alert_on(msg)
            elif txt_ == 'uwina:off':
                ServiceController.bot_alert_off(msg)
            elif txt_ == 'uwinb:on':
                ServiceController.bot_block_on(msg)
            elif txt_ == 'uwinb:off':
                ServiceController.bot_block_off(msg)
            elif txt_ == 'uwin:status':
                ServiceController.bot_status(msg)

            elif txt_ == 'uwin:s1':
                msg.loop = 'single'
                ServiceController._mode_(msg)
            elif txt_ == 'uwin:s5':
                msg.loop = '5line'
                ServiceController._mode_(msg)
            elif txt_ == 'uwin:s10':
                msg.loop = '10line'
                ServiceController._mode_(msg)
            elif txt_ == 'uwin:s15':
                msg.loop = '15line'
                ServiceController._mode_(msg)
            elif txt_ == 'uwin:s20':
                msg.loop = '20line'
                ServiceController._mode_(msg)
            elif txt_ == 'uwin:s25':
                msg.loop = '25line'
                ServiceController._mode_(msg)
            elif txt_ == 'uwin:s30':
                msg.loop = '30line'
                ServiceController._mode_(msg)
            elif txt_ == 'uwin:s40':
                msg.loop = '40line'
                ServiceController._mode_(msg)
            elif txt_ == 'uwin:s50':
                msg.loop = '50line'
                ServiceController._mode_(msg)
            elif txt_ == 'testspeed':
                ServiceController.test_speed(msg)
            elif txt_ == '@reset_bot':
                ServiceController._LEAVE_ALL(msg)
            else:
                another = txt_.split(' ')
                if another[0] == 'uwin':
                	if len(another) != 1:
                		msg.fixtext = another
                		ServiceController._updateText(msg)
                elif another[0] == 'บช':
                	if len(another) != 1:
                		msg.fixtext = another
                		ServiceController._updatBank(msg)
                	elif len(another) == 1:
                		ServiceController._showBank(msg)
        elif msg.type == 17:
            ServiceController._WALLCOME(msg)
        elif msg.type == 15:
            ServiceController._BYE(msg)

	#------------------------------------------------------------------#

    def test_speed(self):
        start = t.time()
        self.mybot.sendMessage(self.message.to, "Prosses...")
        elapsed_time = t.time() - start
        self.mybot.sendMessage(self.message.to,format(str(elapsed_time)))
        # self.mybot.sendImageWithURL(self.message.to, 'https://i.pinimg.com/564x/68/0f/54/680f54ab155687440a65a8d9d941ea3f.jpg')
    def _updatBank(self):
        try:
            alltext = ''
            for i in range(len(self.fixtext)):
            	if i != 0:
            		alltext+= ' '+str(self.fixtext[(i)])
            self.mybot.sendMessage(self.message.to, 'อัพเดท....')
            self.mybot.sendMessage(self.message.to, 'ข้อมูล บัญชีของท่านคือ')
            self.mybot.sendMessage(self.message.to, alltext)
            # Filter
            filter_text = requests.get(str(self.autoload._config._url_api())+'/filter_input/link.php?txt='+str(alltext).strip())
            _filter_text = filter_text.json()
            # update text
            url_ = str(self.autoload._config._url_api())+'/bank/update.php?gid='+str(self.message.to)+'&p='+str(self.autoload._config._name())+'&txt='+str(_filter_text['text']).strip()
            update_text = requests.get(url_)
            _update_text = update_text.json()
            if _update_text['status']:
            	self.mybot.sendMessage(self.message.to, "✅บันทึก เลข บัญชีแล้ว\nสามารถเรียกใช้โดยพิมว่า\nบช\n ครับ")
            else:
            	self.mybot.sendMessage(self.message.to, "❌เกิดข้อผิดพลาด กรุณาติดต่อผู้ให้เช่าบอท")
        except Exception as err:
            print('error ',err)
    def _showBank(self):
        try:
            url_ = str(self.autoload._config._url_api())+'/get_user_filter_multi.php?gid='+str(self.message.to)+'&p='+str(self.autoload._config._name())
            update_text = requests.get(url_)
            _update_text = update_text.json()
            if _update_text[0]['groupline_bank'] != None:
            	self.mybot.sendMessage(self.message.to, _update_text[0]['groupline_bank'])
            else:
            	self.mybot.sendMessage(self.message.to, "⚠ ยังไม่ได้ระบุ\n กรุณาส่ข้อมูลก่อน\nขั้นตอนใช่ข้อมูล \nพิม บช {เลข บช ที่ต้องการ}")
        except Exception as err:
            print('error ',err)
    def _Hon(self):
        try:
            url_ = str(self.autoload._config._url_api())+'/on_off/status.php?gid='+str(self.message.to)+'&p='+str(self.autoload._config._name())+'&s=run'
            update_text = requests.get(url_)
            _update_text = update_text.json()
            if _update_text['status']:
            	self.mybot.sendMessage(self.message.to, "⏯เปิดใช้งานบอทแล้ว\n พิม HY:STOP เพื่อปิดให้งาน")
            else:
            	self.mybot.sendMessage(self.message.to, "❌มีปัญหา กรุณาติดต่อเจ้าของบอท")
        except Exception as err:
            print('error ',err)
    def _Hoff(self):
        try:
            url_ = str(self.autoload._config._url_api())+'/on_off/status.php?gid='+str(self.message.to)+'&p='+str(self.autoload._config._name())+'&s=stop'
            update_text = requests.get(url_)
            _update_text = update_text.json()
            if _update_text['status']:
            	self.mybot.sendMessage(self.message.to, "⏹หยุดรันผลแล้ว \n พิม HY:START เพื่อเปิดให้งาน")
            else:
            	self.mybot.sendMessage(self.message.to, "❌มีปัญหา กรุณาติดต่อเจ้าของบอท")
        except Exception as err:
            print('error ',err)
    def _Total(self):
        try:
            gid = self.mybot.getGroupIdsJoined()
            members = len(gid)
            self.mybot.sendMessage(self.message.to, 'จำนวนกลุ่ม : '+str(members)+' กลุ่ม' )
        except Exception as err:
            print('error ',err)
    def _updateText(self):
        try:
            alltext = ''
            for i in range(len(self.fixtext)):
            	if i != 0:
            		alltext+= ' '+str(self.fixtext[(i)])
            self.mybot.sendMessage(self.message.to, 'อัพเดท....')
            self.mybot.sendMessage(self.message.to, 'ข้อความของท่าน คือ')
            self.mybot.sendMessage(self.message.to, alltext)
            # Filter
            filter_text = requests.get(str(self.autoload._config._url_api())+'/filter_input/link.php?txt='+str(alltext).strip())
            _filter_text = filter_text.json()
            # update text
            url_ = str(self.autoload._config._url_api())+'/text/update.php?gid='+str(self.message.to)+'&p='+str(self.autoload._config._name())+'&txt='+str(_filter_text['text']).strip()
            update_text = requests.get(url_)
            _update_text = update_text.json()
            if _update_text['status']:
            	self.mybot.sendMessage(self.message.to, "✅ข้อความจะโชว์ในรอบถัดไป ค่ะ")
            else:
            	self.mybot.sendMessage(self.message.to, "❌เกิดข้อผิดพลาด กรุณาติดต่อผู้ให้เช่าบอท")
        except Exception as err:
            print('error ',err)
    def _GID(self):
        try: 
            self.mybot.sendMessage(self.message.to, "รหัสกลุ่มคือ")
            self.mybot.sendMessage(self.message.to, self.message.to)
        except Exception as err:
            print('error ',err)
    def _WALLCOME(self):
        try:
            res = requests.get(str(self.autoload._config._url_api())+"/get_user_filter_multi.php?gid="+str(self.param1)+"&p="+str(self.autoload._config._name()))
            result = res.json()
            if len(result) == 1:
            	if result[0]['groupline_key'] == self.param1:
            		if result[0]['groupline_access'] == 'active':
            			if result[0]['groupline_welcome'] == 'ON':
            				self.mybot.sendMessage(self.param1,"ยินดีต้อนรับสมาชิกใหม่")
            				self.mybot.sendMessage(self.param1, "ชื่อสมาชิก : "+self.mybot.getContact(self.param2).displayName)
            				self.mybot.sendMessage(self.param1, None, contentMetadata={'mid': self.param2}, contentType=13)
            				path = "http://dl.profile.line-cdn.net/"+self.mybot.getContact(self.param2).pictureStatus
            				self.mybot.sendImageWithURL(self.param1,str(path))
        except Exception as err:
            print('error  ',err)
    def _BYE(self):
        try: 
            res = requests.get(str(self.autoload._config._url_api())+"/get_user_filter_multi.php?gid="+str(self.param1)+"&p="+str(self.autoload._config._name()))
            result = res.json()
            if len(result) == 1:
            	if result[0]['groupline_key'] == self.param1:
            		if result[0]['groupline_access'] == 'active':
            			if result[0]['groupline_welcome'] == 'ON':
            				self.mybot.sendMessage(self.param1, "ชื่อสมาชิก : "+self.mybot.getContact(self.param2).displayName)
            				self.mybot.sendMessage(self.param1, None, contentMetadata={'mid': self.param2}, contentType=13)
            				path = "http://dl.profile.line-cdn.net/"+self.mybot.getContact(self.param2).pictureStatus
            				self.mybot.sendImageWithURL(self.param1,str(path))
            				self.mybot.sendMessage(self.param1,"ได้ออกจากกลุ่มไปแล้ว")
        except Exception as err:
            print('error  ',err)
    def _LEAVE(self):
            self.mybot.sendMessage(self.message.to,'😊ขอบคุณที่ใช้บริการ😊')
            leave = self.mybot.leaveGroup(self.message.to)

    # เปิดใช้งาน แค่ รันใหม่ ไม่ให้เปิดค้างไว้
    def _LEAVE_ALL(self):
        print('sleep function')
        # try:
        #     gid = self.mybot.getGroupIdsJoined()
        #     for e in gid:
        #         if e != 'cda0b7ff5b7ac1329f1ad6316ae3afc48' and e != 'cc7a4032f71810699742a58cc3c3bb044' and e != 'ccb13d1004cef4eff0eb7a11a33b8cc55' :
        #             try:
        #                 self.mybot.sendMessage(e,'@mybot รายงานผล ระบบเก่า ขออนุญาต ออกจากกลุ่ม เพื่อนำไปรันผลเว็บ UWIN789 จาก สนใจสามารถติดต่อเช่าผลได้ที่ line://ti/p/~@mybot')
        #                 self.mybot.sendMessage(e,'😊ขอบคุณที่ใช้บริการ😊')
        #                 self.mybot.leaveGroup(e)
        #             except Exception as err:
        #                 print('error ',e)
        # except Exception as err:
        #     print('error ',err)
                        
    def _SetWelcome_ON(self):
        try:
            url_ = str(self.autoload._config._url_api())+'/welcome/welcome.php?gid='+str(self.message.to)+'&p='+str(self.autoload._config._name())+'&mode=ON'
            update_text = requests.get(url_)
            _update_text = update_text.json()
            if _update_text['status']:
            	self.mybot.sendMessage(self.message.to, "⏯เปิดต้อนรับแล้ว\n พิม HYW:OFF เพื่อปิดให้งาน")
            else:
            	self.mybot.sendMessage(self.message.to, "❌มีปัญหา กรุณาติดต่อเจ้าของบอท")
        except Exception as err:
            print('error ',err)
    def _SetWelcome_OFF(self):
        try:
            url_ = str(self.autoload._config._url_api())+'/welcome/welcome.php?gid='+str(self.message.to)+'&p='+str(self.autoload._config._name())+'&mode=OFF'
            update_text = requests.get(url_)
            _update_text = update_text.json()
            if _update_text['status']:
            	self.mybot.sendMessage(self.message.to, "⏹หยุดต้อนรับแล้ว\n พิม HYW:ON เพื่อปิดให้งาน")
            else:
            	self.mybot.sendMessage(self.message.to, "❌มีปัญหา กรุณาติดต่อเจ้าของบอท")
        except Exception as err:
            print('error ',err)
    def TagMember(self):
        self.mybot.sendMessage(self.message.to, "👱‍♂️โหลดสมาชิกทั้งหมด👩‍🦳")
        group = self.mybot.getGroup(self.message.to)
        nama = [contact.mid for contact in group.members]
        k = len(nama)//20
        for a in range(k+1):
            txt = u''
            s=0
            b=[]
            for i in group.members[a*20 : (a+1)*20]:
                b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                s += 7
                txt += u'@Alin \n'

            self.mybot.sendMessage(self.message.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
        self.mybot.sendMessage(self.message.to, "จำนวนทั้งหมด {} คน".format(str(len(nama))))
    def bot_active(self):
        try:
            url_ = str(self.autoload._config._url_api())+'/get_user_filter_multi.php?gid='+str(self.message.to)+'&p='+str(self.autoload._config._name())
            update_text = requests.get(url_)
            _update_text = update_text.json()
            if _update_text[0]['groupline_access'] == 'padding':
            	group = self.mybot.getGroup(self.message.to)
            	t.sleep(0.5)
            	self.mybot.sendMessage(self.message.to,"กรุณาคัดลอกข้อความด้านล่าง\nส่งกลับไปให้ผู้ติดบอท\nเพื่อรันผลครับ\n⬇⬇⬇⬇⬇⬇")
            	t.sleep(0.5)
            	self.mybot.sendMessage(self.message.to,"ชื่อกลุ่ม : "+str(group.name)+"\nบอทรายผล : "+str(self.autoload._config._name())+"\nรหัสกลุ่ม : "+str(_update_text[0]['groupline_id'])+"\n"+str(self.message.to))   
            	t.sleep(0.5)
            	self.mybot.sendMessage(self.message.to,"⬆⬆⬆⬆⬆⬆")
            elif _update_text[0]['groupline_access'] == 'stop':
            	self.mybot.sendMessage(self.message.to,'❌บอทหมดอายุแล้ว\nกรุณาติดต่อ @mybot\nเพิ่มต่ออายุครับ')
            elif _update_text[0]['groupline_access'] == 'active':
            	self.mybot.sendMessage(self.message.to, "เปิดให้งานอยู่แล้ว")
            	_start = datetime.strptime(_update_text[0]['groupline_buy_date'], '%Y-%m-%d')
            	YY = str(int(_start.year)+543)
            	D = str(_start.day)
            	month_name = 'x มกราคม กุมภาพันธ์ มีนาคม เมษายน พฤษภาคม มิถุนายน กรกฎาคม สิงหาคม กันยายน ตุลาคม พฤศจิกายน ธันวาคม'.split()[_start.month]
            	start = D+' '+month_name+' '+YY

            	_end = datetime.strptime(_update_text[0]['groupline_buy_end'], '%Y-%m-%d')
            	YY = str(int(_end.year)+543)
            	D = str(_end.day)
            	month_name = 'x มกราคม กุมภาพันธ์ มีนาคม เมษายน พฤษภาคม มิถุนายน กรกฎาคม สิงหาคม กันยายน ตุลาคม พฤศจิกายน ธันวาคม'.split()[_end.month]
            	end = D+' '+month_name+' '+YY
            	groupline_status = str(_update_text[0]['groupline_status'])
            	groupline_version = str(_update_text[0]['groupline_version'])
            	groupline_theme = str(_update_text[0]['groupline_theme'])
            	groupline_block = str(_update_text[0]['groupline_block'])
            	groupline_over_alert = str(_update_text[0]['groupline_over_alert'])
            	groupline_encode = str(_update_text[0]['groupline_id'])  
            	groupline_welcome = str(_update_text[0]['groupline_welcome'])  
            	# groupline_encode= str(_update_text[0]['groupline_encode'])
            	if groupline_status == 'run':
            		groupline_status = 'เปิดใช้งาน'
            	else: 
            		groupline_status = 'ปิดใช้งาน'            	
            	if groupline_over_alert == 'on':
            		groupline_over_alert = 'เปิด'
            	else: 
            		groupline_over_alert = 'ปิด'
            	if groupline_block == 'ON':
            		groupline_block = 'เปิด'
            	else: 
            		groupline_block = 'ปิด'
            	if groupline_welcome == 'ON':
            		groupline_welcome = 'เปิด'
            	else: 
            		groupline_welcome = 'ปิด'
            	view = "      สถานะบอท\n" + \
            	"🆗 เปิดใช้งานแล้ว 🆗\n" + \
            	"     เปิดใช้งานเมื่อ \n" + \
            	"   "+str(start)+"\n" + \
            	"     หมดอายุวันที่\n" + \
            	"  " +str(end) + "\n" + \
            	"  *******************\n" + \
            	"   บอทเวอร์ชั่น : " + groupline_version + "\n" + \
            	"   สถานะ : " + groupline_status + "\n" + \
            	"  รันผลแบบ : " + groupline_theme + "\n" + \
            	"  ไม้กั้นผล(ซม) : " + groupline_block + "\n" + \
            	" เตือนหมดเวลา : " + groupline_over_alert + "\n" + \
            	" ข้อความต้อนรับ : " + groupline_welcome + "\n" + \
            	"   รหัสกลุ่ม : " + groupline_encode
            	self.mybot.sendMessage(self.message.to, view)
        except Exception as err:
            print('error ',err)
    def bot_alert_on(self):
        try:
            url_ = str(self.autoload._config._url_api())+'/alert/alert.php?p='+str(self.autoload._config._name())+'&mode=on&gid='+str(self.message.to)
            mode = requests.get(url_)
            _mode = mode.json()
            if _mode['status'] == True:
            	self.mybot.sendMessage(self.message.to, "เปิดเตือนหมดเวลาแล้ว✅")
            else:
            	self.mybot.sendMessage(self.message.to, "มีปัญหากรุณาติดต่อ\nแอดมิน")
        except Exception as err:
            print('error ',err)
    def bot_alert_off(self):
        try:
            url_ = str(self.autoload._config._url_api())+'/alert/alert.php?p='+str(self.autoload._config._name())+'&mode=off&gid='+str(self.message.to)
            mode = requests.get(url_)
            _mode = mode.json()
            if _mode['status'] == True:
            	self.mybot.sendMessage(self.message.to, "ปิดเตือนหมดเวลาแล้ว⭕")
            else:
            	self.mybot.sendMessage(self.message.to, "มีปัญหากรุณาติดต่อ\nแอดมิน")
        except Exception as err:
            print('error ',err)
    def bot_block_on(self):
        try:
            url_ = str(self.autoload._config._url_api())+'/block/block.php?p='+str(self.autoload._config._name())+'&mode=ON&gid='+str(self.message.to)
            mode = requests.get(url_)
            _mode = mode.json()
            if _mode['status'] == True:
            	self.mybot.sendMessage(self.message.to, "เปิดไม้กั้นผลแล้ว✅")
            else:
            	self.mybot.sendMessage(self.message.to, "มีปัญหากรุณาติดต่อ\nแอดมิน")
        except Exception as err:
            print('error ',err)
    def bot_block_off(self):
        try:
            url_ = str(self.autoload._config._url_api())+'/block/block.php?p='+str(self.autoload._config._name())+'&mode=OFF&gid='+str(self.message.to)
            mode = requests.get(url_)
            _mode = mode.json()
            if _mode['status'] == True:
            	self.mybot.sendMessage(self.message.to, "ปิดไม้กั้นผลแล้ว⭕")
            else:
            	self.mybot.sendMessage(self.message.to, "มีปัญหากรุณาติดต่อ\nแอดมิน")
        except Exception as err:
            print('error ',err)
    def bot_status(self):
        try:
            url_ = str(self.autoload._config._url_api())+'/get_user_filter.php?gid='+str(self.message.to)+'&p='+str(self.autoload._config._name())
            update_text = requests.get(url_)
            _update_text = update_text.json()
            if _update_text[0]['groupline_access'] == 'active':
            	try:
            		_start = datetime.strptime(_update_text[0]['groupline_buy_date'], '%Y-%m-%d')
            		YY = str(int(_start.year)+543)
            		D = str(_start.day)
            		month_name = 'x มกราคม กุมภาพันธ์ มีนาคม เมษายน พฤษภาคม มิถุนายน กรกฎาคม สิงหาคม กันยายน ตุลาคม พฤศจิกายน ธันวาคม'.split()[_start.month]
            		start = D+' '+month_name+' '+YY

            		_end = datetime.strptime(_update_text[0]['groupline_buy_end'], '%Y-%m-%d')
            		YY = str(int(_end.year)+543)
            		D = str(_end.day)
            		month_name = 'x มกราคม กุมภาพันธ์ มีนาคม เมษายน พฤษภาคม มิถุนายน กรกฎาคม สิงหาคม กันยายน ตุลาคม พฤศจิกายน ธันวาคม'.split()[_end.month]
            		end = D+' '+month_name+' '+YY
            	except Exception as err: 
            		start = "ยังไม่ระบุวันที่เริ่ม"
            		end = "ยังไม่ระบุวันที่หมด"

            	groupline_status = str(_update_text[0]['groupline_status'])
            	groupline_version = str(_update_text[0]['groupline_version'])
            	groupline_theme = str(_update_text[0]['groupline_theme'])
            	groupline_block = str(_update_text[0]['groupline_block'])
            	groupline_over_alert = str(_update_text[0]['groupline_over_alert'])
            	groupline_encode= str(_update_text[0]['groupline_id'])           	
            	# groupline_encode= str(_update_text[0]['groupline_encode'])
            	groupline_welcome= str(_update_text[0]['groupline_welcome'])
            	if groupline_status == 'run':
            		groupline_status = 'เปิดใช้งาน'
            	else: 
            		groupline_status = 'ปิดใช้งาน'            	
            	if groupline_over_alert == 'on':
            		groupline_over_alert = 'เปิด'
            	else: 
            		groupline_over_alert = 'ปิด'
            	if groupline_block == 'ON':
            		groupline_block = 'เปิด'
            	else: 
            		groupline_block = 'ปิด'
            	if groupline_welcome == 'ON':
            		groupline_welcome = 'เปิด'
            	else: 
            		groupline_welcome = 'ปิด'
            	if groupline_theme == 'single':
            		groupline_theme = '1'
            	else: 
            		groupline_theme = groupline_theme.replace("line", "")

            	groupline_products = str(_update_text[0]['groupline_products'])

            	view = "      สถานะบอท\n" + \
            	"🆗 เปิดใช้งานแล้ว 🆗\n" + \
            	"     เปิดใช้งานเมื่อ \n" + \
            	"   "+str(start)+"\n" + \
            	"     หมดอายุวันที่\n" + \
            	"  " +str(end) + "\n" + \
            	"********************\n" + \
                " รันผล :"+groupline_products+"\n"+\
            	"   บอทเวอร์ชั่น : " + groupline_version + "\n" + \
            	"   สถานะ : " + groupline_status + "\n" + \
            	"  รันผลแบบ : " + groupline_theme + " แถว\n" + \
            	"  ไม้กั้นผล(ซม) : " + groupline_block + "\n" + \
            	" เตือนหมดเวลา : " + groupline_over_alert + "\n" + \
            	" ข้อความต้อนรับ : " + groupline_welcome + "\n" + \
            	"   รหัสกลุ่ม : " + groupline_encode+ "\n" + \
            	"➖➖➖➖➖➖➖\n" + \
            	"BOT VERSION "+str(self.autoload._config._building_version())
            	self.mybot.sendMessage(self.message.to, view)
            else:
            	self.mybot.sendMessage(self.message.to, "❌ยังไม่ได้เปิดใช้งาน")
        except Exception as err:
            print('error ',err)
	#MODE 
    def _mode_(self):
        try:
            url_ = str(self.autoload._config._url_api())+'/mode/mode.php?mode='+str(self.loop)+'&p='+str(self.autoload._config._name())+'&gid='+str(self.message.to)
            mode = requests.get(url_)
            _mode = mode.json()
            if _mode['status'] == True:
            	if self.loop == 'single':
            		self.loop = '1'
            	elif self.loop == '5line':
            		self.loop = '5'
            	elif self.loop == '10line':
            		self.loop = '10'
            	elif self.loop == '15line':
            		self.loop = '15'
            	elif self.loop == '20line':
            		self.loop = '20'
            	elif self.loop == '25line':
            		self.loop = '25'
            	elif self.loop == '30line':
            		self.loop = '30'
            	elif self.loop == '40line':
            		self.loop = '40'
            	elif self.loop == '50line':
            		self.loop = '50'
            	self.mybot.sendMessage(self.message.to, "เปลี่ยนโหมด เสร็จแล้ว✅\n➖➖➖➖➖➖➖➖\nใช้โหมดธรรมดา "+str(self.loop)+" แถวแล้ว")
            else:
            	self.mybot.sendMessage(self.message.to, "มีปัญหากรุณาติดต่อ\nแอดมิน")
        except Exception as err:
            print('error ',err)
