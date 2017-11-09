#!/usr/bin/env python
# coding: utf-8
import time
import threading
from wxbot import *

class MyWXBot(WXBot):
    reply=True
    def handle_msg_all(self, msg):

        if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:#收到了信息
            print("收到了信息 ")
            self.shifouxuyao=True
            self.weixinid = msg['user']['id']
            self.lastest_receive_time=time.time()
            # print(t.isAlive())
            # print(t.getName())
            #self.send_msg_by_uid(u'正在忙，请稍后联系 （本条为自动回复）', msg['user']['id'])
            # if(msg['msg_type_id']==4):
            #     self.send_msg_by_uid(u'正在忙，请稍后联系 （本条为自动回复）', msg['user']['id'])
        if msg['msg_type_id'] == 1 and msg['content']['type'] == 0:
            print("回复了")
            self.shifouxuyao=False
            # thread = threading.current_thread()
            # print(thread.getName())
            #self.send_msg_by_uid(u'啊？', msg['user']['id'])
            #print msg
            #self.send_img_msg_by_uid("img/1.png", msg['user']['id'])
            #self.send_file_msg_by_uid("img/1.png", msg['user']['id'])
        # if msg['msg_type_id'] == 99:
        #     print("查看了")

# schedule()的功能为收到某人的信息，且三分钟内无回复，则自动回复信息
# 可能不能正常运行的情况：多人不同时间发送信息，单人每隔2分钟发送信息
# 改进方向：1.不用 msg['msg_type_id'] == 1判断是否需要回复，而是用msg unkonw判断
#          2.利用数组或列表等记录多人不同时间发送信息的情况，依次对每个人自动回复

    def schedule(self):
        try:
            if (self.shifouxuyao == True and (time.time()-self.lastest_receive_time)>180):      #有没回的信息，且时间超过30秒，需要自动发送
                self.send_msg_by_uid(u'正在忙，请稍后联系 （本条为自动回复）', self.weixinid)
                self.send_msg_by_uid(u'本功能为本人编写，可能存在漏发，误发，迟发等一系列问题，敬请谅解，有急事可拨打电话18586108602。代码改编自wxBot，源代码已在github上更新。', self.weixinid)
                self.shifouxuyao=False
        except :
            print("出错了")
            #print shifouxuyao,lastest_receive_time
        print("经历了一轮schedule")+str(time.time())
        time.sleep(10)



def main():
    shifouxuyao=False
    weixinid=0
    lastest_receive_time=time.time()
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()


if __name__ == '__main__':
    main()
