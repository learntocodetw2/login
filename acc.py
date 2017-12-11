acc = {
	'allen1225': 'qwe123456',
	'a0919123123': 'mayday123',
	'jolin1124': '8315566'
}
# 讓使用者可以重複輸入帳號，
# 如果帳號存在，就讓他輸入密碼，然後檢查密碼對不對
# (密碼對 就印出 登入成功! 不對就說不對..)
# 如果帳號不存在，就印出 找不到帳號
while True:
	username = input('請輸入帳號: ')
	if username in acc:
		print('有這個帳號!')
		password = input('請輸入密碼: ')
		if password == acc[username]:
			print('登入成功!')
			break
		else:
			print('密碼錯誤!')
	else:
		print('找不到這個帳號!')