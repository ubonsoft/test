class Theme(object):
	def _block(_b) :
		if _b == 4 or _b == 8 or _b == 12 or _b == 16 or _b == 20 or _b == 24 or _b == 28 or _b == 32 or _b == 36 or _b == 40 or _b == 44 or _b == 48 or _b == 52 or _b == 56 or _b == 60 or _b == 64 or _b == 68 or _b == 72 or _b == 76 or _b == 80 or _b == 84 or _b == 88 or _b == 92 :
			return " \n➖➖➖➖➖➖➖"
		else:
			return ""

	def show_1_loop(result,text_header,show_date,_time,text_msg,_view,_block):
		view = ''
		_unit = ''
		_unit_vip = ''
		_time = ''
		_name = ''
		theme = ""
		theme_vip = ""
		theme_header = "➖➖➖➖➖➖➖\n♉รายงานผล UWIN789♉"
		figloop = 5
		_result_row = len(result)
		if len(result) < 5:
			figloop = _result_row
		_index = _result_row - figloop
		for i in range(_index,_result_row):
			try:
				_unit = str(result[i]['lottery_loop_3unit'])+' - '+str(result[i]['lottery_loop_2unit'])
				_time = str(result[i]['lottery_loop_time'])
				_name = str(result[i]['lottery_loop_name'])
			except Exception as err:
				print('error')
		if _view == 'NORMAL' :
			view = str(theme_header)+"\n"+ \
			"      เวลา " + str(_name) + " น. \n" + \
			"          รอบที่ " + str(_time) + "   \n" + \
			"➖➖➖➖➖➖➖ \n" + \
			"    ♉จับยี่ UWIN♉ \n" + \
			"          " + str(_unit) 
		view =  view+"\n➖➖➖➖➖➖➖\n   "+ show_date +"\n➖➖➖➖➖➖➖\n " +	text_msg
		return view

	def show_5_loop(result,text_header,show_date,_time,text_msg,_view,_block):
		view = ''
		_unit = ''
		_unit_vip = ''
		_time = ''
		_name = ''
		theme = ""
		theme_vip = ""
		theme_header = "➖➖➖➖➖➖➖\n♉รายงานผล UWIN789♉\n➖➖➖➖➖➖➖"
		figloop = 5
		_result_row = len(result)
		if len(result) < 5:
			figloop = _result_row
		_index = _result_row - figloop
		for i in range(_index,_result_row):
			try:
				theme = theme+"\n"+str(result[i]['lottery_loop_time'])+" : "+str(result[i]['lottery_loop_name'])+" ➡️ "+str(result[i]['lottery_loop_3unit'])+" - "+str(result[i]['lottery_loop_2unit'])
			except Exception as err:
				print('error')
		if _view == 'NORMAL' :
			view = text_header+'\n'+str(theme_header)+''+str(theme)
		view =  view+"\n➖➖➖➖➖➖➖\n"+ show_date +"\n➖➖➖➖➖➖➖\n" +	text_msg
		return view

	def show_multi_loop(result,text_header,show_date,_time,text_msg,_view,_block,loop):
		view = ''
		_unit = ''
		_unit_vip = ''
		_time = ''
		_name = ''
		theme = ""
		theme_vip = ""
		theme_header = "➖➖➖➖➖➖➖\n♉รายงานผล UWIN789♉\n➖➖➖➖➖➖➖"
		figloop = loop
		_result_row = len(result)
		if len(result) < loop:
			figloop = _result_row
		_index = _result_row - figloop
		for i in range(_index,_result_row):
			try:
				theme = theme+"\n"+str(result[i]['lottery_loop_time'])+" : "+str(result[i]['lottery_loop_name'])+" ➡️ "+str(result[i]['lottery_loop_3unit'])+" - "+str(result[i]['lottery_loop_2unit'])
				_unit = str(result[i]['lottery_loop_3unit'])+' - '+str(result[i]['lottery_loop_2unit'])
				_time = str(result[i]['lottery_loop_time'])
				_name = str(result[i]['lottery_loop_name'])
				try:
					if _block == 'ON':
						theme = theme+''+str(Theme._block(result[i]['lottery_loop_time']))
				except Exception as err:
					print('error block')
			except Exception as err:
				print('error')
		highlight = "➖➖➖➖➖➖➖ \n" + \
		" จับยี่ UWIN รอบ " + _time + "\n" + \
		"         " + _unit 
		if _view == 'NORMAL' :
			view = text_header+'\n'+str(theme_header)+''+str(theme)+'\n'+highlight
		view =  view+"\n➖➖➖➖➖➖➖\n"+ show_date +"\n➖➖➖➖➖➖➖\n" +	text_msg
		return view