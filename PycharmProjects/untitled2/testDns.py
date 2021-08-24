import dns.resolver

domain = input('Please input an domain: ')  #输入域名地址
A = dns.resolver.query(domain, 'A')  #查询记录为A记录
#print(A.response.answer)
for i in A.response.answer:
	for j in i.items:
		if j.rdtype == 1: #加判断，不然会出现AttributeError: 'CNAME' object has no attribute 'address'

			print(j.address)