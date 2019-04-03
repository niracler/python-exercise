# python-exercise

> 关于python的面试题及leetcode题目代码实现

## 目录

## Python基础

### 文件操作

1. [写一个返回该文件夹中文件的路径,以及其包含文件夹中文件的路径的函数](interview_question/print_dir.py)

### 模块与包

1. [函数输入为年月日，输出这是该年的第几天](interview_question/get_date.py)

1. [打乱一个排好序的list对象alist？](interview_question/upset_a_list.py)

### 数据类型

1. [现有字典 d= {'a':24,'g':52,'i':12,'k':33}请按value值进行排序?](interview_question/sort_dicts.py)

1. [请反转字符串 "aStr"?](interview_question/reverse_str.py)

1. [将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}](interview_question/to_dicts.py)

1. [请按alist中元素的age由大到小排序](interview_question/sort_list.py)

1. 下面代码的输出结果将是什么？
    ```python
    list1 = ['a','b','c','d','e']
    print(list1[10:])
    ```
    代码将会输出[]， 不会产生IndexError错误， 就像所期望的那样，尝试用超出成员的个数的index来获取某个列表的成员。例如尝试获取list[10]和之后的成员，会导致IndexError。然而， 尝试获取列表的切片，开始的index超过了成员个数不会产生IndexError， 而是仅仅返回一个空列表。这成为特别让人恶心的疑难杂症， 因为运行的时候没有产生错误，导致BUG很难被追踪到。

1. [写一个列表生成式，产生一个公差为11的等差数列](interview_question/gen_list.py)

1. [给定两个列表，怎么找出他们相同的元素和不同的元素？(集合)](interview_question/different_list.py)

1. [请写出一段python代码实现删除list里面的重复元素？](interview_question/dif_sim.py)

### 企业面试题

1. Python新式类与经典类的区别？  
  a. Python里凡是继承了object的类都是新式类  
  b. Python3中只有新式类  
  c. Python2中继承object的类是新式类,没有写父类的是经典类  
  d. 经典类目前在Python中基本没有应用  

2. Python中内置数据结构有几种?  
  int, str, float, complex, long(Python3中没有, 只有无限精度的int)  
  list, tuple, set, dict  

3. Python中如何实现单例模式? 请写出至少两种实现方法  
    第一种方法:[使用装饰器](interview_question/singleton.py)  
    第二种方法:[使用基类new](interview_question/singleton.py), 是真正创建实例对象的方法,所以重写基类的new方法,以此保证创建对象的时候只生成一个实例  
    ~~第三种方法:[元类](interview_question/singleton.py), 元类是用于创建类对象的类,类对象创建实例对象时一定要调用call方法, 因此在调用call时候始终只创建一个实例即可,type是Python的元类~~

4. [反转一个整数，例如-123 --> -321](interview_question/reverse_int.py)

5. [设计实现遍历目录与子目录，抓取.py文件](interview_question/os_test.py)

6. [一行代码实现1-100之和](interview_question/one_line_add.py)

7. [Python-遍历列表时删除元素的正确做法](interview_question/del_list.py)

8. [字符串的操作题目](interview_question/str_operation.py)

9. 可变类型与比可变类型  
  a. 可变类型有list,dict, 不可变类型有tuple, number, string  
  b. 当进行修改操作时,可变类型传递的是内存中的地址,也就是说,直接修改内存中的值,并没有开辟新的内存  
  c. 不可变类型被修改时,并没有改变原来内存地址中的值,而是开辟一块新的内存,将原来地址中的之复制进去,对这块新开辟的内存中的值进行操作

10. is和==有什么区别?  
  is: 比较的是两个对象的id是否相等,也就是比较两对象是否为同一个实例对象.是否指向同一个内存地址  
  ==: 比较两个对象的内容/值是否相等, 默认会调用对象的eq()方法
  
11. [求出列表所有奇数并构造新列表 ](interview_question/odd_number.py)

12. Python中变量的作用域?(变量查找顺序)  
    函数作用域的LEGB顺序  
    a. 什么是LEGB?  
    L: local函数内部作用域   
    E: enclosing 函数内部与内嵌函数之间  
    G: global全局作用域  
    B: build-in 内置作用域  
    python在函数中的查找分为4种, 称之为LEGB,也正是按照这种顺序来查找的  
    
13. [字符串 "123" 转换成 123，不使用内置api，例如 int()](interview_question/atoi.py)

14. [相加值为给定的某个数](interview_question/sum_is_target.py)  
    给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。示例:给定nums = [2,7,11,15],target=9 因为 nums[0]+nums[1] = 2+7 =9,所以返回[0,1]

15. [给列表中的字典排序](interview_question/sort_dicts2.py)  
    假设有如下list对象， ```alist=[{"name":"a","age":20},{"name":"b","age":30},{"name":"c","age":25}]``` ,
    将alist中的元素按照age从大到小排序 ```alist=[{"name":"a","age":20},{"name":"b","age":30},{"name":"c","age":25}]```

16. [python代码实现删除一个list里面的重复元素](interview_question/dist_func.py)

17. [统计一个文本中单词频次最高的10个单词？](interview_question/highest_frequency.py)

1. [请写出一个函数满足以下条件](interview_question/get_even.py)  
    该函数的输入是一个仅包含数字的list,输出一个新的list，其中每一个元素要满足以下条件：  
    1、该元素是偶数  
    2、该元素在原list中是在偶数的位置(index是偶数)  

1. [使用单一的列表生成式来产生一个新的列表](interview_question/gen_list2.py)  
    该列表只包含满足以下条件的值，元素为原始列表中偶数切片

1. [用一行代码生成[1,4,9,16,25,36,49,64,81,100]](interview_question/gen_list3.py)

1. [输入某年某月某日，判断这一天是这一年的第几天？](interview_question/get_data_in_year.py)

1. [两个有序列表，l1,l2，对这两个列表进行合并不可使用extend](interview_question/merge_list.py)

1. [给定一个任意长度数组，实现一个函数](interview_question/up_stream.py)  
    让所有奇数都在偶数前面，而且奇数升序排列，偶数降序排序，如字符串'1982376455',变成'1355798642'

1. [写一个函数找出一个整数数组中，第二大的数](interview_question/get_second_big.py)

1. 阅读一下代码他们的输出结果是什么？

    ```python
    def multi():
        return [lambda x : i*x for i in range(4)]
    print([m(3) for m in multi()])
    ```

1. [统计一段字符串中字符出现的次数](interview_question/count_str.py)


1. super函数的具体用法和场景



## LeetCode热门面试问题

### Array

1. [两个数相加的和等于某个数](leetcode/array/two_sum.py)

1. [将零放到最后](leetcode/array/move_zeros.py)

1. [找单个出现的值](leetcode/array/single_number.py)

1. [list的交集](leetcode/array/intersect.py)

1. [一个存在列表里的数,你将它加1(高精度加法)](leetcode/array/plus_one.py)

1. [不新建一个二维列表旋转图片](leetcode/array/rotate_image.py)

1. [买卖股票的最好时间及最大收益分析](leetcode/array/max_profit.py)

1. [列表中是否有重复的元素？](leetcode/array/contains_duplicate.py)

1. [列表挪位](leetcode/array/rotate_array.py)


### Strings

1. [不用额外的空间翻转字符串](leetcode/strings/reverse_string.py)

1. [翻转数字](leetcode/strings/reverse.py)

1. [自己实现strStr()找子串](leetcode/strings/my_strstr.py)

1. [报数](leetcode/strings/count_and_say.py)

1. [不一样的自己写的atoi()](leetcode/strings/my_atoi.py)

1. [找英文回文](leetcode/strings/valid_palindrome.py)

1. [找字符串中第一个不重复的字母](leetcode/strings/first_uniq_char.py)

1. [判断是不是用同样的字母构成的单词](leetcode/strings/valid_anagram.py)

### Linked List

1. [删除链表中的当前节点的元素](leetcode/linked_list/delete_node.py)

1. [删除链表中倒数第N个节点](leetcode/linked_list/remove_eth_from_end.py)

1. [有序链表合并](leetcode/linked_list/merge_two_lists.py)

1. [链表倒序](leetcode/linked_list/reverse_list.py)

###

## 参考文章

- [关于python的面试题](https://github.com/Niracler/python-interview-question)  
- [python-exercises](https://www.w3resource.com/python-exercises/)
