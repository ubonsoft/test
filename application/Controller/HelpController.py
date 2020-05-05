import application.Config.config as _config
Conf = _config.config
import application.View.Menu as Menu
Menu = Menu.Menu

class HelpController(object):
    def __init__(self,msg):
        # _group = msg.message.to
        txt = msg.message.text.lower()
        _txt = txt.strip()
        if _txt == '@mybot' or _txt == '@uwin' or _txt == 'uwin':
            HelpController.HelpGroup(msg)
            
    def HelpGroup(self):
        try:
            self.mybot.sendMessage(self.message.to, Menu.ShowCommand())
        except Exception as err:
            print('error ',err)
        
