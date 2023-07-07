# -*- coding: utf-8 -*-
#!/usr/bin/python
#Google Indexing Api
# Coded Shin_Code
#My Friendo : JametKNTLS -  h0d3_g4n - Moslem And All Coders
# Blog : https://www.blog-gan.org          
#Buy coffee :
	# BTC = 31mtLHqhaXXyCMnT2EU73U8fwYwigiEEU1
	# PERFECT MONEY  = U22270614
	# SAWERIA : https://saweria.co/Shin403
	# TRAKTEER : https://trakteer.id/shin403
#CONTACT ME :(
       # ICQ : https://icq.im/Shin403
       # Telegram : https://t.me/Shin_code
       # Youtube : Smile Of Beauty 
# Apakah kamu hanya bisa melakukan recode dengan mengganti nama author?
# Can you only recode by changing the author name?
############# [ Module ] #############
import urllib2
from xml.dom import minidom
import google.auth
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from google.oauth2 import service_account
import json
import subprocess
import time
import os

IJO = '\033[92m'
KUNING = '\033[93m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
BIRU = '\033[36m'
ABANG = '\033[91m'
RESET = '\033[0m'



def Single_Post():
	file_path = raw_input("\nMasukkan path file JSON \033[36m(contoh: blog.json) ~#$ \033[0m")
	url_kamu = raw_input("\nMasukkan Url \033[36m(contoh: https://www.blog-gan.org/2023/07/cara-menggunakan-google-indexing-api.html) ~#$ \033[0m")
	credentials = None
	with open(file_path) as f:
		credentials = json.load(f)
		credentials = service_account.Credentials.from_service_account_info(credentials)
		scoped_credentials = credentials.with_scopes(['https://www.googleapis.com/auth/indexing'])
		indexing_service = build('indexing', 'v3', credentials=scoped_credentials)
		url_notification = {
		'url': url_kamu,
		'type': 'URL_UPDATED'
		}
		try:
			request = indexing_service.urlNotifications().publish(body=url_notification)
			response = request.execute()
			metadata = response['urlNotificationMetadata']
			latest_update = metadata['latestUpdate']
			url = metadata['url']
			url2 = latest_update['url']
			notify_time = latest_update['notifyTime']
			type_shin = latest_update['type']
			print('\n[-] url : ' + KUNING + url + RESET)
			print('[?] Update Url :  ' + CYAN + url2 + RESET)
			print('[+] Waktu Update : ' + MAGENTA + notify_time + RESET)
			print('[*] Success Submit Google Indexing : ' + IJO + type_shin + RESET)
		except Exception as e:
			print(ABANG + 'Terjadi kesalahan:\n' + RESET, str(e))


def mass_post():
	try:
		file_path = raw_input("\nMasukkan path file JSON \033[36m(contoh: blog.json) ~#$ \033[0m")
		sitemap_url = raw_input("\nMasukkan Url \033[36m(contoh: https://www.blog-gan.org/sitemap.xml ~#$ \033[0m")
		response = urllib2.urlopen(sitemap_url)
		xml_content = response.read()
		xml_doc = minidom.parseString(xml_content)
		loc_elements = xml_doc.getElementsByTagName('loc')
		urls = [element.firstChild.nodeValue for element in loc_elements]
		count = len(urls)
		print('[?] URLs extracted :  ' + BIRU + str(count) + RESET)
		credentials = None
		with open(file_path) as f:
			credentials = json.load(f)
			credentials = service_account.Credentials.from_service_account_info(credentials)
			scoped_credentials = credentials.with_scopes(['https://www.googleapis.com/auth/indexing'])
			indexing_service = build('indexing', 'v3', credentials=scoped_credentials)
			for url in urls:
				url_notification = {
				'url': url,
				'type': 'URL_UPDATED'
				}
				try:
					request = indexing_service.urlNotifications().publish(body=url_notification)
					response = request.execute()
					metadata = response['urlNotificationMetadata']
					latest_update = metadata['latestUpdate']
					url = metadata['url']
					url2 = latest_update['url']
					notify_time = latest_update['notifyTime']
					type_shin = latest_update['type']
					print('\n[-] url : ' + KUNING + url + RESET)
					print('[?] Update Url :  ' + CYAN + url2 + RESET)
					print('[+] Waktu Update : ' + MAGENTA + notify_time + RESET)
					print('[*] Success Submit Google Indexing : ' + IJO + type_shin + RESET)
					time.sleep(2)
				except Exception as e:
					print(ABANG + 'Terjadi kesalahan:\n' + RESET, str(e))
	except Exception as e:
		print('Error:', str(e))


def Main():
	try:
		if choose =='1':
			print "{}Single Indexing{}".format(ABANG,RESET)
			Single_Post()
		elif choose =='2':
			print "{}Mass Indexing{}".format(IJO,RESET)
			mass_post()
	except:
		pass

if __name__ == '__main__':
	os.system('cls' if os.name == 'nt' else 'clear')
	def create_banner(*texts):
		borders = '-' * max(len(text) for text in texts)
		banner = '{}\n{}\n{}'.format(borders, '\n'.join(texts), borders)
		return banner
	banner_text0 = "{} Google Indexing Api  | {}Shin Code\n{}".format(KUNING,CYAN,RESET)
	banner_text1 = "{} 1. Single Indexing{}".format(ABANG,RESET)
	banner_text2 = "{} 2. Mass Indexing{}".format(IJO,RESET)
	banner = create_banner(banner_text0, banner_text1, banner_text2)
	print(banner)
	choose = raw_input("\nPilih Ex # 1 : ")
	Main()
			
