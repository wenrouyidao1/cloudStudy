
# 验证码生成器
import random

def getCode(n):
    if n <= 0:
        return 'please input right number！！！'

    def warpper(n):
        code = ''
        for i in range(n):
            result = [str(random.randint(0, 9)), chr(random.randint(65, 90)), chr(random.randint(97, 122))]
            code += random.choice(result)
        return code
    return warpper(n)

codes = getCode(4)
print('验证码为：{}'.format(codes))

userInput = input('请输入上方验证码：')
if userInput.lower() == codes.lower():
    print('login successfully')
else:
    print('faild！！！')