#!/usr/bin/env python3
import requests, json, time, re, os

# Warna
KUNING = ('\x1b[1;93m')
MERAH = ('\x1b[1;91m')
HIJAU = ('\x1b[1;92m')
PUTIH = ('\x1b[1;97m')
U = ('\x1b[1;95m')
O = ('\x1b[1;96m')
N = ('\x1b[0m')
J = ('\033[38;2;255;127;0;1m')
# Banner
banner = (f"""     {MERAH}({PUTIH}-Rudal-XD-{MERAH}){PUTIH}
{MERAH}╔═╗┌─┐┌┐┌┬  ┬┌─┐┬─┐┌┬┐
{MERAH}║  │ ││││└┐┌┘├┤ ├┬┘ │
{PUTIH}╚═╝└─┘┘└┘ └┘ └─┘┴└─ ┴
""")
# Convert Cookie Ke Token
class convert:

  def __init__(self):
    os.system('clear')
    print(f"""{banner}
{HIJAU}1.{O} Mendapatkan token EAAI
{HIJAU}2.{PUTIH} Dapatkan token EAAB
{HIJAU}3.{PUTIH} Cara menggunakan
{HIJAU}4.{PUTIH} Keluar {HIJAU}({MERAH}exit{HIJAU}){MERAH}
   """)
    masuk = input(f"{KUNING}?.{PUTIH} Choose :{HIJAU} ")
    if masuk == '1' or masuk == '01':
      cookie = input(f"\n{HIJAU}?.{PUTIH} Cookie :{KUNING} ")
      if 'c_user=' in str(cookie):
        self.__satu__(cookie)
      else:
        masuk = input(f"{MERAH}!.{MERAH} Periksa cookienya")
        sleep(1)
        os.system('git pull');convert()
    elif masuk == '2' or masuk == '02':
      cookie = input(f"\n{HIJAU}?.{PUTIH} Cookie :{KUNING} ")
      if 'c_user=' in str(cookie):
        self.__dua__(cookie)
      else:
        exit(f"{MERAH}!.{MERAH} Periksa cookienya")
    elif masuk == '3' or masuk == '03':
      print(f"{KUNING}?.{PUTIH} Anda akan diarahkan ke youtube...");time.sleep(3);os.system('xdg-open https://youtu.be/Xv0plMtS4Cw');exit()
    elif masuk == '4' or masuk == '04':
      exit()
    else:
      os.system('git pull');convert()
  def __satu__(self,cookie):
    try:
      with requests.Session() as r:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Cookie': cookie
        }
        response = r.get('https://web.facebook.com/ads/manager/account_settings/account_billing/?_rdc=1&_rdr', headers = headers)
        find = re.findall('(EAAI\w+)', response.text)
        if len(find) == 0:
          exit(f"{MERAH}!.{MERAH} Token tidak ditemukan")
        else:
          for token in find:
            print(f"\n{KUNING}?.{PUTIH} Your token :{HIJAU} {token}")
    except Exception as e:
      exit(f"{MERAH}!.{MERAH} {e}")
  def __dua__(self,cookie):
    try:
      with requests.Session() as r:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Cookie': cookie
        }
        respon = r.get('https://web.facebook.com/adsmanager?_rdc=1&_rdr', headers = headers)
        find = re.findall('act=(.*?)&nav_source', respon.text)
        if len(find) == 0:
          exit(f"{MERAH}!.{MERAH} Token tidak ditemukan")
        else:
          for y in find:
            response = r.get(f'https://web.facebook.com/adsmanager/manage/campaigns?act={y}&nav_source=no_referrer', headers = headers)
            token = re.search('(EAAB\w+)', response.text).group(1)
            print(f"\n{KUNING}?.{PUTIH} Your token :{HIJAU} {token}")
    except Exception as e:
      exit(f"{MERAH}!.{MERAH} {e}")

if __name__=='__main__':
  os.system('git pull');convert()
