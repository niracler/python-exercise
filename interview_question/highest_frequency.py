# """
# 题目：统计一个文本中单词频次最高的10个单词？
#
# """
import re


class Solution:
    def get_highest_frequency(self, article):
        """
        失败
        :param article:
        :return:
        """
        words = article.replace('\n', ' ')
        words = words.replace('(', ' ')
        words = words.replace(')', ' ')
        words = words.replace('[', ' ')
        words = words.replace(']', ' ')
        words = words.split()
        print(words)

        dicts = {}
        dicts = dicts.fromkeys(words)
        word_list = dicts.keys()
        for word in word_list:
            dicts[word] = words.count(word)

        # 使用lambda匿名函数用value排序,返回列表[('the', 45), ('function', 38)...这种形式]
        dicts = sorted(dicts.items(), key=lambda x: x[1], reverse=True)
        dicts = dict(dicts[:10])

        return dicts


if __name__ == '__main__':
    article = """
        David Beazley's talk at US PyCon 2018, about parser generators, reminded me I should write a bit about its history. Here'.s a brief brain dump (maybe I'll expand later)
        
        There are actually two pgens. The original, in C, and a rewrite in Python, under lib2to3/pgen2.
        
        I wrote both. The original was actually the first code I wrote for Python. Although technically I had to write the lexer first (pgen and Python share their lexer, pgen just doesn't have any uses for most tokens). 
        
        The reason for writing my own parser generator was that at the time the landscape of parser generators (that I was familiar with) was pretty sparse -- basically there was Yacc (the GNU rewrite named Bison existed, but I don't know if I knew); or you could write a parser by hand (which is what most people did). I had used Yacc in college and was familiar with how it worked from the Dragon book, but for some reason I didn't like it much; IIRC I found it hard to reason about what the limitations on an LALR(1) grammar would be. I was also familiar with LL(1) parsers and had written some serious recursive-descent LL(1) parsers by hand -- I liked that fine but I was also familiar (again from the Dragon book) with LL(1) parser generation techniques, and I had one improvement over that that I wanted to try out: using regular expressions (sort of) instead of the standard BNF format. The Dragon book had also taught me how to turn regular expressions into DFAs, so I combined all that and pgen was born. [Update: see below for a slightly different version for the reason.]
        
        I was not familiar with more advanced techniques, or I deemed them too inefficient. (I think most people working in parsers did, at the time.) 
        
        For the lexer I decided I would not use a generator -- I had a much lower opinion of Lex than of Yacc, since the version of Lex that I was familiar with would just segfault when trying to scan a token longer than 255 bytes (really!). Also I figured that indentation would be hard to teach to a lexer generator. 
        
        The story of pgen2 is quite different: I was employed by a startup in San Mateo (Elemental Security, it died in 2007, after I had left and joined Google) where I was given the task to design a custom language (for security assertions about system configuration), and was given pretty much free reign. I decided to design something vaguely like Python, implemented in Python, and decided that I wanted to reuse pgen, but with a backend in Python, using tokenize.py as the lexer. So I just rewrote the exact algorithm from pgen in Python and then moved on to build the rest of that language. Open-sourcing the tooling made sense to management so they quickly approved that, and some time later (I had probably moved on to Google by then?) it made sense to use those tools for 2to3. (It was easy to generate a Python parser with it because the input format was identical to the original pgen -- I just had to feed the Grammar file into the tool. :-)
        """

    solution = Solution()
    result = solution.get_highest_frequency(article)
    print(result)

# """
# 分析:
#
# """
