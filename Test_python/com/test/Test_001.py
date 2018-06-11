#coding=utf-8

print "hahah哈哈哈"


#python 最具特色的就是用缩进来写模块。
if True:
    print "True"
else:
    print "False"
  
'''
在 Python 的代码块中必须使用相同数目的行首缩进空格数。 否则运行就会报错。
  if True:
      print "Answer"
      print "True"
  else:
      print "Answer"
      # 没有严格缩进，在执行时会报错
    print "False"
'''


total = 'item_one' + \
        "item_two" + \
        'item_three'
print (total);

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday'];
print (days);

word = 'word'
sentence = "这是一个" \
          + "句子。"
paragraph = """这是一个段落。
包含了多个语句"""
print (sentence);
print (paragraph);