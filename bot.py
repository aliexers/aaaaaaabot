elif msg.get("text") == "راهنما":
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
									rules = open("helps_arianbot/cc.txt","r",encoding='utf-8').read()
									bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
								else:
									bot.sendMessage(target,f" کاربر  {G_UN} شما متاسفانه عضو کانال ما نیستید برای اجرای این\nدستور ابتدا عضو کانال ما شوید: \n@arian____bot", message_id=msg.get("message_id"))
							except:
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
										rules = open("helps_arianbot/cc.txt","r",encoding='utf-8').read()
										bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
									else:
										bot.sendMessage(target,f" کاربر  {G_UN} شما متاسفانه عضو کانال ما نیستید برای اجرای این\nدستور ابتدا عضو کانال ما شوید: \n@arian____bot", message_id=msg.get("message_id"))
								except:
									print("err rahnama")
