s='cap dOcker'

s.capitalize() #'字符串第一位大写，若不为字母则忽略,其余小写'  'Qweq方-asa asdasd'
s.title() #单词第一个字母大写 单词以任意非字母分割 其余小写 'Qweq方-Asa Asdasd'
'CaT'.casefold() #忽略大小写 效果同lower  'cat'
s.upper() #所有字母大写 'CAP DOCKER'
s.lower() # 所有字母小写 'cap docker'
s.swapcase() #大写变小写，小写变大写 'CAP DoCKER': str = 'kittle'

'a{a}{b}'.format_map({"a":1,'b':3}) #按字典格式化   'a13'
'11{}'.format(22)  #格式化  '22'

'思芹 '.encode(encoding='utf-8') #字符串编码 b'\xe6\x80\x9d\xe8\x8a\xb9 '
b'\xe6\x80\x9d\xe8\x8a\xb9 '.decode(encoding='utf-8') #解码 '思芹 '

'dasda'.count('as',1,3) #字符串指定位置匹配子串数量

s.zfill(12) #以在字符串左侧加0的方式，使字符串达到指定长度 '00cap dOcker'
str.maketrans({'a':'',' ':'0'}) #生成翻译对照表，可以说是批量ord
s.translate({ord('a'):'',ord(' '):'0'}) #按照字典键值替换字符 'cp0dOcker'
'cap,application'.replace('ap','---',2) # 字符串替换，替换次数默认为无数  'c---,---plication'


s.startswith('ap',1,3) #判断字符串是否以指定字符开始，可以自定义字符串开始和结束位置         True
s.endswith('ck',1,-2) #判断字符串是否以指定字符结束，可以自定义字符串开始和结束位置         True
'app.py'.removesuffix('.py') #删除匹配的后缀字符串否则返回原字符串    'app'
'app.py'.removeprefix('app')#删除匹配的前缀字符串否则返回原字符串    '.py'

' asdasdalasdass'.strip(' asd') #删除首尾所有属于传入参数的字母，默认参数空格 'l'
' asdasdalasdass'.rstrip(' asd') #删除尾所有属于传入参数的字母，默认参数空格 ' asdasdal'
' asdasdalasdass'.lstrip(' asd') #删除首所有属于传入参数的字母，默认参数空格 'lasdass'

'cat\ndog s'.splitlines() #将字符串按换行符分行 ['cat', 'dog s']

"cat-dogs-find-had".split('-',2) #将字符串按指定符号分割指定次数，默认是空格，无数次 ['cat', 'dogs', 'find-had']
"cat-dogs-find-had".rsplit('-',2) #从尾部开始 将字符串按指定符号分割指定次数，默认是空格，无数次 ['cat', 'dogs', 'find-had']

'sapsaps'.rpartition('ap') #将字符串按指定字符串最后匹配位置分割   ('saps', 'ap', 's')
'sapsaps'.partition('ap') #将字符串按指定字符串分割 ('s', 'ap', 'saps')

'-.-'.join(['cat', 'dog',' sad'])#将字符串加入到另一个由字符串可迭代对象中间  'cat-.-dog-.- sad'

s.rjust(12,'-') #将字符串以指定长宽右对齐，以指定符号填充，默认空格  '--cap dOcker'
s.ljust(12,'-') #将字符串以指定长宽左对齐，以指定符号填充，默认空格  'cap dOcker--'
s.center(12,'-') #将字符串以指定长宽中间对齐，以指定符号填充，默认空格  '-cap dOcker-'

s.index('c',0,9) #在字符串指定区域匹配指定字符串的最小索引,失败则valueerror            0
s.rindex('ck',0,9) # 在字符串指定区域匹配指定字符串的最大索引,失败则valueerror            6
s.find('c',0,9) # 在字符串指定区域匹配指定字符串的最小索引 ，失败返回-1             0
s.rfind('ck',0,9) # 在字符串指定区域匹配指定字符串的最大索引 ，失败返回-1             6

's\ts'.expandtabs(3) #把tab字符用指定数量-1的空格代替，默认为8.  参数2=1都是1个空格

s.isuper() #是否全大写
s.islower() #是否全小写
s.istitle() #是否每词开头大写
str.isspace()   #是否空白字符 \n \t \r 空格 'Ture'
str.isprintable() #是否可打印 \n \t \r 'False'
'1④四壹'.isnumeric() #Unicode数字，全角数字（双字节），罗马数字，汉字数字   |   b'2'单字节error
'1④四壹'.isdigit()#是否Unicode数字，byte数字（单字节），全角数字（双字节）
'11'.isdecimal()#Unicode数字，，全角数字（双字节） |   b'2'单字节error
'a1;'.isascii()#是否ascii 字符，英文标点，数字，字母大小写
'王a'.isalpha() #是否是字符
'a'.isalnum() #是否
'-is'.isidentifier() #是否合法的python变量






