print("⚠️کاربران گرامی شما حق ویرایش یا ادیت سورس پایتون آرین بات را ندارید درصورت مشاهده آپدیت های سورس بنده دراختیار شما قرار نمی گیرد⚠️")



from requests import get
from re import findall
import os
import glob
from rubika.client import Bot
from rubika.tools import Tools
from rubika.encryption import encryption
import io






#شناسه اکانت
bot = Bot(" ")
#......
#شناسه کانال
channell = " "



answered, retries = [], {}


while 1:
	try:
		pass


		while 1:
			try:
				messages = bot.getChatsUpdate()
				break
			except:
				continue

		for CHAT in messages:
			try:
				if CHAT["abs_object"]["type"]== "User" and not CHAT['last_message']['message_id'] in answered:
					msg = CHAT["last_message"]
					print("PV:" +" "+"[" + msg.get("author_object_guid") +"]" + ">>>" + " " + "(" + msg.get("text")+ ")"  + "\n")
					print(".....")
					if msg.get("text").startswith("جوین گپ"):
						try:
							G_U = msg.get("author_object_guid")
							ID_karbar = bot.getUserInfo(G_U)["data"]["user"]["username"]
							NAME_karbar = bot.getUserInfo(G_U)["data"]["user"]["first_name"]
							if ID_karbar != None:
								ozv_ajbar = [i["member_guid"] for i in bot.getChannelMembers(channell,ID_karbar)["data"]["in_chat_members"]]
							else:
								if NAME_karbar != None:
									ozv_ajbar = [i["member_guid"] for i in bot.getChannelMembers(channell,NAME_karbar)["data"]["in_chat_members"]]
								else:pass
							G_UN = bot.getUserInfo(G_U)["data"]["user"]["first_name"]
							if msg.get("author_object_guid") in ozv_ajbar:
								joingroup = msg.get("text").strip("جوین گپ")
								bot.joinGroup(joingroup)
								bot.sendMessage(msg.get("author_object_guid"),f"کاربر {G_UN} اکانت هوشمند با موفقیت عضو گروه شما شد ✅", message_id=msg.get("message_id"))
							else:
								bot.sendMessage(msg.get("author_object_guid"),f" کاربر  {G_UN} شما متاسفانه عضو کانال ما نیستید برای اجرای این\nدستور ابتدا عضو کانال ما شوید: \n@arian____bot", message_id=msg.get("message_id"))
						except:pass

					elif msg.get("text").startswith("جوین چنل"):
						try:
							G_U = msg.get("author_object_guid")
							ID_karbar = bot.getUserInfo(G_U)["data"]["user"]["username"]
							NAME_karbar = bot.getUserInfo(G_U)["data"]["user"]["first_name"]
							if ID_karbar != None:
								ozv_ajbar = [i["member_guid"] for i in bot.getChannelMembers(channell,ID_karbar)["data"]["in_chat_members"]]
							else:
								if NAME_karbar != None:
									ozv_ajbar = [i["member_guid"] for i in bot.getChannelMembers(channell,NAME_karbar)["data"]["in_chat_members"]]
								else:pass
							G_UN = bot.getUserInfo(G_U)["data"]["user"]["first_name"]
							if msg.get("author_object_guid") in ozv_ajbar:
								joinchannell = msg.get("text").strip("جوین چنل")
								print(joinchannell)
								bot.joinChannel(joinchannell)
								bot.sendMessage(msg.get("author_object_guid"),f"کاربر {G_UN} اکانت هوشمند با موفقیت عضو کانال شما شد ✅", message_id=msg.get("message_id"))
							else:
								bot.sendMessage(msg.get("author_object_guid"),f" کاربر  {G_UN} شما متاسفانه عضو کانال ما نیستید برای اجرای این\nدستور ابتدا عضو کانال ما شوید: \n@arian____bot", message_id=msg.get("message_id"))
						except:pass
				else:pass
			except:
				continue

			answered.append(CHAT['last_message']['message_id'])



	except KeyboardInterrupt:
		exit()

	except Exception as e:
		if type(e) in list(retries.keys()):
			if retries[type(e)] < 3:
				retries[type(e)] += 1
				continue
			else:
				retries.pop(type(e))
		else:
			retries[type(e)] = 1
			continue