# """
# 题目：题目三. 在对域名进行分析中，常常会碰到“主域归属”问题。首先，我们有一个主域列表，如下所示：
# *.sports.sina.com.cn
# *.sina.com.cn
# *.baidu.com
# *.tencent.com
# *.com
# *.cn
# 等等，这个列表可能会包含百万级别的配置。
# 在有这个配置的前提下，给定一个域名，比如roll.sports.sina.com.cn，希望能够找到它所匹配的最长的“主域”，比如，对于上面这个域名，
# 应该匹配到*.sports.sina.com.cn这个主域。
#
# 请实现一个程序，从配置文件domain.txt读取主域列表，每行一个；
# 从标准输入读取需要匹配的域名，每行一个；向标准输出打印：需要匹配的域名\t它匹配到的最长主域。
# 注意，请尽可能高效，使用正则匹配会非常慢。
#
# url:
# """


class Solution:
    def que1(self, a):
        f = open('domain.txt', 'r')
        for i in f.readlines():
            print(i)
        return ""

#             int[] arr = new int[1000];
#
#             HashSet<String> hashSet = new HashSet<>();
#             String line = null;
#             while((line = bufferedReader.readLine()) != null){
#                 line.trim();
#                 int index = line.indexOf(".");
#                 if(index>=0) hashSet.add(line.substring(index+1));
#             }
#             Scanner scanner = new Scanner(System.in);
#             while(scanner.hasNext()){
#                 String domain = scanner.nextLine();
#                 String sub = domain;
#                 int pos = -1;
#                 do{
#                     sub = sub.substring(pos+1);
#                     if(hashSet.contains(sub)){
#                         System.out.println(domain + "\t" + "*."+sub);
#                         break;
#                     }
#                     pos = sub.indexOf(".");
#                 }while (pos >= 0);
#             }
#
#         } catch (FileNotFoundException e) {
#             e.printStackTrace();
#         }catch (IOException ioe){
#             ioe.printStackTrace();
#         }


if __name__ == '__main__':
    a = ""

    solution = Solution()
    result = solution.que1(a)
    print(result)

# """
# 分析:
#
# """
