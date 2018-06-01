import re
email = input('请输入邮箱地址:')
result = re.match('.{4,20}@\.163.com$',email)
print(result)
if result !=None:
    print('登陆成功')

else:
    print('登录失败')