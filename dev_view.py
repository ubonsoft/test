import json
import time as t
from datetime import datetime
import pytz
import requests
import application.View.Theme as Theme
Theme = Theme.Theme
# import application.View.Menu as Menu
# Menu = Menu.Menu

# print(Menu.ShowCommand())

try: 
	tz_NY = pytz.timezone('Asia/Bangkok') 
	# show footer time
	now1 = datetime.now(tz_NY)
	month_name = 'x มกราคม กุมภาพันธ์ มีนาคม เมษายน พฤษภาคม มิถุนายน กรกฎาคม สิงหาคม กันยายน ตุลาคม พฤศจิกายน ธันวาคม'.split()[now1.month]
	thai_year = now1.year + 543
	time_str = now1.strftime('%H:%M:%S')
	show_date = "%d %s %d"%(now1.day, month_name, thai_year) # 30 ตุลาคม 2560 # disabled -> 20:45:30

	datetime_NY = datetime.now(tz_NY)
	HM = datetime_NY.strftime("%H:%M")
	time = requests.get('http://at-mybot.me/api/py/forbot/huay/time.json')
	_time = time.json()
	result = ''
	maxloop = 1
	while True :
		print('loop')
		t.sleep(1)
		res = requests.get('http://api5.at-mybot.me/api/huay30line.php?loop='+_time[HM])
		result = res.json()
		fix = ''
		for x in result:
			fix = str(x['lottery_loop_3unit'])
		if fix != 'xxx' and int(res.status_code) == 200:
			break
		if maxloop == 50:
			break
		maxloop += 1

	users = requests.get('http://at-mybot.me/api/py/forbot/get_users.php?v=V1&p=HUAYNORMALVIP')
	_users = users.json()
	index = 0
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
			if index == 0:
				index = 1
				if _u['groupline_theme'] == 'single':
					resp = Theme.show_1_loop(result,str(text_header),show_date,_time,text_msg,str(text_view),_block)
				elif _u['groupline_theme'] == '5line':
					resp = Theme.show_5_loop(result,str(text_header),show_date,_time,text_msg,str(text_view),_block)
				elif _u['groupline_theme'] == '10line':
					resp = Theme.show_10_loop(result,str(text_header),show_date,_time,text_msg,str(text_view),_block)
				elif _u['groupline_theme'] == '15line':
					resp = Theme.show_15_loop(result,str(text_header),show_date,_time,text_msg,str(text_view),_block)
				elif _u['groupline_theme'] == '20line':
					resp = Theme.show_20_loop(result,str(text_header),show_date,_time,text_msg,str(text_view),_block)
				elif _u['groupline_theme'] == '25line':
					resp = Theme.show_25_loop(result,str(text_header),show_date,_time,text_msg,str(text_view),_block)
				elif _u['groupline_theme'] == '30line':
					resp = Theme.show_30_loop(result,str(text_header),show_date,_time,text_msg,str(text_view),_block)
				print(resp)
		except Exception as err:
			print('error ',err)
except Exception as err:
	print('error ',err)



