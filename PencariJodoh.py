logo = '''
░░░▒█ ▒█▀▀▀█ ▒█▀▀▄ ▒█▀▀▀█ ▒█░▒█ 
░▄░▒█ ▒█░░▒█ ▒█░▒█ ▒█░░▒█ ▒█▀▀█ 
▒█▄▄█ ▒█▄▄▄█ ▒█▄▄▀ ▒█▄▄▄█ ▒█░▒█
author : Sulmad Maulida
github : https://github.com/sulmadmaulida/PencariJodoh

'''
print(logo)
userName = input('nama : ')
userGander = input('cewe/cowo : ')

if userGander == 'cowo':
  print('Hallo ' + userName + ' kita pdkt dulu ya...')
  userPdkt = input('kamu siap pdkt denganku? y/t : ')
  if userPdkt == 'y':
    print('Hallo ' + userName + ' namaku siti')
    userAge = input('umur ' + userName + ' berapa? : ')
    print('wahhhh umurmu ' + userAge + ' tahun yah, jadi makin sayang deh sama kamu🥰🥰🥰')
    nikah = input(userName + ' kamu siap nikah denganku? y/t :')
    if nikah == 'y':
      print('yok kita kepenghulu sekarang')
    else:
      print('ohhhh gitu tidak mau nikah denganku, ok fix kita musuhan sekarang😡')
  else: 
    print('ohhhh gitu tidak mau pdkt denganku, ok fix kita musuhan sekarang😡')
elif userGander == 'cewe':
  print('Hallo ' + userName + ' kita pdkt dulu ya...')
  userPdkt = input('kamu siap pdkt denganku? y/t : ')
  if userPdkt == 'y':
    print('Hallo ' + userName + ' namaku asep')
    userAge = input('umur ' + userName + ' berapa? : ')
    print('wahhhh umurmu ' + userAge + ' tahun yah, jadi makin sayang deh sama kamu🥰🥰🥰')
    nikah = input(userName + ' kamu siap nikah denganku? y/t :')
    if nikah == 'y':
      print('yok kita kepenghulu sekarang')
    else:
      print('ohhhh gitu tidak mau nikah denganku, ok fix kita musuhan sekarang😡')
  else: 
    print('ohhhh gitu tidak mau pdkt denganku, ok fix kita musuhan sekarang😡')
else:
  print('tulislah datamu dengan benar!')