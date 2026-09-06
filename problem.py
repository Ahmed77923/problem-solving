 

 #=+==========================================================================+=
 #=+==========================================================================+=
 #=+==========================================================================+=
 #=+==========================================================================+=
 #=+==========================================================================+=
#1 https://www.codewars.com/kata/554b4ac871d6813a03000035
#2 https://www.codewars.com/kata/563cf89eb4747c5fb100001b
#3 https://www.codewars.com/kata/55908aad6620c066bc00002a
#4 https://www.codewars.com/kata/546e2562b03326a88e000020
#5 https://www.codewars.com/kata/56606694ec01347ce800001b
#6 https://www.codewars.com/kata/57eaec5608fed543d6000021
#7 https://www.codewars.com/kata/558fc85d8fd1938afb000014
#8 https://www.codewars.com/kata/5656b6906de340bd1b0000ac
#9 https://www.codewars.com/kata/55f2b110f61eb01779000053
#10 https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
#11 https://www.codewars.com/kata/559590633066759614000063
#12 
#13 
#14 https://www.codewars.com/kata/5467e4d82edf8bbf40000155
#15 https://www.codewars.com/kata/54ff3102c1bad923760001f3
#16 https://www.codewars.com/kata/566fc12495810954b1000030
#17 https://www.codewars.com/kata/57f609022f4d534f05000024
#18 https://www.codewars.com/kata/554e4a2f232cdd87d9000038
#19 https://www.codewars.com/kata/5679aa472b8f57fb8c000047
#20 https://www.codewars.com/kata/53dbd5315a3c69eed20002dd

# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064
#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# def row_sum_odd_numbers(n):
#     #your code here
#     return n ** 3
# https://www.codewars.com/kata/5590961e6620c0825000008f

# https://www.codewars.com/kata/55d24f55d7dd296eb9000030

# https://www.codewars.com/kata/56a1c63f3bc6827e13000006

# https://www.codewars.com/kata/5583090cbe83f4fd8c000051

# https://www.codewars.com/kata/5592e3bd57b64d00f3000047

# https://www.codewars.com/kata/56b1f01c247c01db92000076

# https://www.codewars.com/kata/56541980fa08ab47a0000040

# https://www.codewars.com/kata/54ba84be607a92aa900000f1

# https://www.codewars.com/kata/559f860f8c0d6c7784000119

# https://www.codewars.com/kata/566a65d6d8ebfcac5e000075

# https://www.codewars.com/kata/55c45be3b2079eccff00010f

# https://www.codewars.com/kata/57f8ff867a28db569e000c4a

# https://www.codewars.com/kata/55f8a9c06c018a0d6e000132

# https://www.codewars.com/kata/56f3f6a82010832b02000f38

# https://www.codewars.com/kata/54da539698b8a2ad76000228

# https://www.codewars.com/kata/567501aec64b81e252000003

# https://www.codewars.com/kata/55ccdf1512938ce3ac000056

# https://www.codewars.com/kata/566dc566f6ea9a14b500007b

# https://www.codewars.com/kata/563e320cee5dddcf77000158
#=+==========================================================================+=
#=+==========================================================================+=
#=+==========================================================================+=
# Importing pandas and matplotlib
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# # Read in the Netflix CSV as a DataFrame
# netflix_df = pd.read_csv("netflix_data.csv")

# # Filter the data for movies released in the 1990s

# # Filter 1990s short movies and count
# moviesIn1990s = netflix_df[
#     (netflix_df['release_year'] >=1990) &
#     (netflix_df['release_year']<= 1999)
# ]
# short_movie_count = (moviesIn1990s["duration"] < 90).sum()

# duration = short_movie_count
#=+==========================================================================+=
# Importing pandas and matplotlib
#
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# # Read in the Netflix CSV as a DataFrame
# netflix_df = pd.read_csv("netflix_data.csv")

# # Filter the data for movies released in the 1990s

# # Filter 1990s short movies and count
# moviesIn1990s = netflix_df[
#     (netflix_df['release_year'] >=1990) &
#     (netflix_df['release_year']<= 1999)
# ]
# short_movie_count = (action_movies_1990s["duration"] < 90).sum()

# duration = short_movie_count



#=+==========================================================================+=
#=+==========================================================================+=
#=+==========================================================================+=
#=+==========================================================================+=
#=+==========================================================================+=
#=+==========================================================================+=
#=+==========================================================================+=
#=+==========================================================================+=
#==================================  1 =========================================+=
# def nb_dig(n, d):
#     result = 0
#     newlist = []
#     for i in range(n+1):
#         newlist.append(str(i**2))
#     for j in newlist:
#         result += j.count(str(d))
#     return result
# nb_dig(5750, 0)#, 4700)
# nb_dig(11011, 2)#, 9481)
# nb_dig(12224, 8)#, 7733)
# nb_dig(11549, 1)#, 11905)
# nb_dig(14550, 7)#, 8014)
# nb_dig(8304, 7)#, 3927)
# nb_dig(10576, 9)#, 7860)
 #======================================  2 =====================================+=
# def DNA_strand(dna):
#     result  =''
#     for i in dna:
#         if i == 'T':
#             result += 'A'
#         elif i == 'A':
#             result  += 'T'
#         elif i == 'C':
#             result += 'G'
#         elif i == 'G':
#             result  += 'C'
#         else:
#             result += i
#     return result
#  #=======================================  3 ====================================+=
# def div_con(x):
#     result = 0
#     for i in x:
#         if type(i) == int:
#             result += i
#         else:
#             result -= int(i)
#     return result 
# n =[1,3,2,121]
# print(n.index(121))
 #============================================  4 ===============================+=
# def digitize(n):
#     return [ int(i) for i in str(n)]
# digitize(123)#, [1,2,3])
# digitize(1), [1])
# digitize(0), [0])
# digitize(1230), [1,2,3, 0])
# digitize(8675309), [8,6,7,5,3,0,9])
 #====================================  5 =======================================+=
# def xo(s):
#     result1=0
#     result2=0
#     for i in s:
#         if i.lower() == 'o':
#             result1 +=1
#         if i.lower() == 'x':
#             result2 += 1
#     if result1 == result2:
#         return True
#     else:
#         return False
# anther solving for this problem 
#     s = s.lower()
    # return s.count('x') == s.count('o')
# xo("ooxx")#,    True),
# xo("xooxx")#,   False),
# xo("ooxXm")#,   True), # Comparison is case-insensitive
# xo("zpzpzpp")#, True), # when no 'x' and 'o' is present should return true
# xo("zzoo")#,    False),
# xo("oxOx")#,    True),
# xo("")#,        True),
 #===================================  6 ========================================+=
# def vaporcode(s):
#     result = ''
#     for i in s:
#         if i != " " :
#             result +=i.upper() + '  '
#     return  result[:-2]
# vaporcode("Lets go to the movies")#,"L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S")
# vaporcode("Why isn't my code working?")#,"W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?")
 #======================================  7 =====================================+=
# def divisors(n):
#     result = 1
#     for i in range(1,n):
#         if n % i == 0:
#             result += 1
#     return result
# divisors(1), 1 
# divisors(4), 3
# divisors(5), 2
# divisors(12), 6
# divisors(30), 8
# divisors(4096), 13
 #=====================================  8 ======================================+=
# def sum_nested(lst):
#     total = 0
#     for item in lst:
#         if isinstance(item, list):
#             total += sum_nested(item)
#         else:
#             total += item
#     return total
#=========================================  9 ==================================+=
# def scramble(strng, array):
#     result = ''
#     listt=[]
#     for i,j in zip(strng,array):
#         listt.append([i,j])
#         sorted_list = sorted( listt, key=lambda x: x[1])
#     for t,k in sorted_list:
#        result += t
#     # print(listt)
#     print(result)
# scramble('abcd', [0,3,1,2])#, 'acdb', "Should return acdb")
# scramble('sc301s', [4,0,3,1,5,2])#, "c0s3s1", "Should return c0s3s1")
# scramble('bskl5', [2,1,4,3,0])#, "5sblk", "Should return 5sblk")
#  #======================================  10 =====================================+=
# def remove_vowels(strng):
#     char = ['a','i','e','o','u']
#     result =''
#     for i in strng:
#         if i in char:
#             pass
#         else:
#             result += i
#     return result
# remove_vowels("drake")#, "drk")
# remove_vowels("aeiou")#, "")
# #=======================================  11 ====================================+=
# def capitalize(s):
#     result = []
#     item = ''
#     for i,j in enumerate(s):
#         if i % 2 ==0:
#             item +=j.upper()
#         else:
#             item += j 
#     result.append(item)
#     for i,j in enumerate(s):
#         if i % 2 ==1:
#             item +=j.upper()
#         else:
#             item += j 
#     result.append(item)
#     print(result)
# capitalize("abcdef")#,['AbCdEf', 'aBcDeF'])
# capitalize("codewars")#,['CoDeWaRs', 'cOdEwArS'])
# capitalize("abracadabra")#,['AbRaCaDaBrA', 'aBrAcAdAbRa'])
# capitalize("codewarriors")#,['CoDeWaRrIoRs', 'cOdEwArRiOrS'])
# capitalize("indexinglessons")#,['InDeXiNgLeSsOnS', 'iNdExInGlEsSoNs'])
# capitalize("codingisafunactivity")#,['CoDiNgIsAfUnAcTiViTy', 'cOdInGiSaFuNaCtIvItY'])
#====================================  12 =======================================+=
# def find_screen_height(width, ratio): 
#     w, h = map(int, ratio.split(':'))
#     height = width * h // w
#     print(f'{width}x{int(height)}')
# find_screen_height(1024, "4:3")#, "1024x768")
# find_screen_height(1280, "16:9")#, "1280x720")
# find_screen_height(3840, "32:9")#, "3840x1080")
# find_screen_height(1600, "4:3")# "1600x1200")
# find_screen_height(1280, "5:4")# "1280x1024")
# find_screen_height(2160, "3:2")# "2160x1440")
# find_screen_height(1920, "16:9")#, "1920x1080")
# find_screen_height(5120, "32:9")#, "5120x1440")
# #===================================  13 ========================================+=
# def decode(message):
#     message = message.lower()
#     result = ''
#     for i in message:
#         m = ord(i)-97
#         result +=  chr(122 - m)
        
#     print(result)
# decode('abcd')#zyxw
# decode("svool")#,"hello")
# decode("r slkv mlylwb wvxlwvh gsrh nvhhztv")#,"i hope nobody decodes this message")
# decode("qzezxirkg rh z srts ovevo wbmznrx fmgbkvw zmw rmgvikivgvw kiltiznnrmt ozmtfztv rg szh yvvm hgzmwziwravw rm gsv vxnzxirkg ozmtfztv hkvxrurxzgrlm zolmthrwv sgno zmw xhh rg rh lmv lu gsv gsivv vhhvmgrzo gvxsmloltrvh lu dliow drwv dvy xlmgvmg kilwfxgrlm gsv nzqlirgb lu dvyhrgvh vnkolb rg zmw rg rh hfkkligvw yb zoo nlwvim dvy yildhvih drgslfg koftrmh")#, "javacript is a high level dynamic untyped and interpreted programming language it has been standardized in the ecmacript language specification alongside html and css it is one of the three essential technologies of world wide web content production the majority of websites employ it and it is supported by all modern web browsers without plugins") 
# decode("gsv vrtsgs hbnkslmb dzh qvzm hryvorfh urmzo nzqli xlnklhrgrlmzo kilqvxg lxxfkbrmt srn rmgvinrggvmgob")#, "the eighth symphony was jean sibelius final major compositional project occupying him intermittently")
# decode("husbands ask repeated resolved but laughter debating")#, "sfhyzmwh zhp ivkvzgvw ivhloevw yfg ozftsgvi wvyzgrmt")
# decode("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")#, "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
# decode(" ")#," ")
# decode("")#,"")
# decode("thelastrandomsentence")#, "gsvozhgizmwlnhvmgvmxv")
#====================================  14 =======================================+=
# def save(sizes, hd):
#     result = 0 # 1 + 1 + 1
#     hard = 0
#     if sizes == [] or sizes[0]>hd :
#         print(0) 
#     for i in sizes:
#         if hard + i > hd: break
#         else: hard += i
#         result += 1
#     print( result) 
# save([4,4,4,3,3], 12)#, 3)
# save([4,4,4,3,3], 11)#, 2)
# save([4,8,15,16,23,42], 108)#, 6)
# save([13], 13)#, 1)
# save([1,2,3,4], 250)#, 4)
# save([100], 500)#, 1)
# save([11,13,15,17,19], 8)#, 0)
# save([45], 12)#, 0)
# save([12, 0, 0, 1], 12)#, 3)
#=====================================  15 ======================================+=
# def get_middle(s):
#     if len(s)%2==1:
#         return s[int(len(s)/2)]
#     else:
#         return s[int(len(s)/2)-1]+ s[int(len(s)/2)]
# get_middle("test")#,"es")
# get_middle("testing")#,"t")
# get_middle("middle")#,"dd")
# get_middle("A")#,"A")
# get_middle("of")#,"of")
# #====================================  16 =======================================+=
# def sort_by_binary_ones (numList):
#   newlist = []
#   num = (bin(numList[0]).count('1'))
#   for i in numList:
#     if  num < (bin(i).count('1')):
#       newlist.append(i)
#   newlist.append(num)
#   print(newlist)
# sort_by_binary_ones([1, 5,3])#, [3, 1]
# sort_by_binary_ones([1, 2, 3, 4])#, [3, 1, 2, 4])        
# sort_by_binary_ones([1, 2, 3, 4])#, [3, 1, 2, 4])
# sort_by_binary_ones([1, 3])#, [3, 1])
# sort_by_binary_ones([1, 15, 7, 3, 5])#, [15, 7, 3, 5, 1])
# sort_by_binary_ones([80, 21])#, [21, 80])
# sort_by_binary_ones([0, 1024, 33])#, [33, 1024, 0])
# sort_by_binary_ones([2, 2048, 3])#, [3, 2, 2048])
# sort_by_binary_ones([5, 2049, 3])#, [3, 5, 2049])
# sort_by_binary_ones([1,5,21,7,44,99,50,51,49,80,33,25])#, [ 51, 99, 7, 21, 25, 44, 49, 50, 5, 33, 80, 1 ])
#=====================================  17 ======================================+=
# def sum_of_integers_in_string(s):
#     result= 0
#     num = 0
#     for i in s:
#         if i.isdigit():
#             num = num * 10 +(ord(i) - ord('0')) 
#         else:
#           result += num
#           num =0
#     result+= num
#     print( result)
  
# sum_of_integers_in_string("12.4" )#16
# sum_of_integers_in_string("h3ll0w0rld", 3),
# sum_of_integers_in_string("2 + 3 = ", 5),
# sum_of_integers_in_string("Our company made approximately 1 million in gross revenue last quarter.", 1),
# sum_of_integers_in_string("The Great Depression lasted from 1929 to 1939.", 3868),
# sum_of_integers_in_string("Dogs are our best friends.", 0),
# sum_of_integers_in_string("C4t5 are 4m4z1ng.", 18),
# sum_of_integers_in_string("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog", 3635)
        
#=====================================  18 ======================================+=
# def doubles(s):
#     result = []
#     for i in s:
#         if result == [] or i != result[-1]:
#             result.append(i)
#         else:
#             result.pop()
#     return ''.join(result)
# ('abbcccdddda')#'aca'
# ('vvvvvoiiiiin')#,'voin')
# ('rrrmooomqqqqj')#,'rmomj')
# ('xxbnnnnnyaaaaam')#,'bnyam')
# ('qqqqqqnpppgooooonpppppqmmmmmc')#,'npgonpqmc')
# ('qqqqqwwwx')#,'qwx')
# ('jjjfzzzzzzsddgrrrrru')#,'jfsgru')
# ('jjjjjfuuuutgggggqppdaaas')#,'jftgqdas')
# ('iiiiibllllllyqqqqqbiiiiiituuf')#,'ibyqbtf')
# ('mmmmmmuzzqllllmqqqp')#,'uqmqp')
#====================================  19 =======================================+=
# def solve(st,a,b):
#     result = ''
#     now = ''
    
#     for i in range(len(st)):
#       if i < a :
#         result += st[i] 
#       elif i >= a and i <= b:
#         now += st[i]
#     result += now[::-1]
#     for i in range(b + 1, len(st)):
#         result += st[i]
#     print(result) 

# solve("codewars",1,5)#,"cawedors")
# solve("codingIsFun",2,100)#,"conuFsIgnid")
# solve("FunctionalProgramming", 2,15)#,"FuargorPlanoitcnmming")
# solve("abcefghijklmnopqrstuvwxyz",0,20)#,"vutsrqponmlkjihgfecbawxyz")
# solve("abcefghijklmnopqrstuvwxyz",5,20)#,"abcefvutsrqponmlkjihgwxyz")
#====================================  20 =======================================+=
# def solve(s):
#     letters = [c for c in s if c != " "]
#     letters.reverse()

#     result = ""
#     idx = 0
#     for c in s:
#         if c == " ":
#             result += " "
#         else:
#             result += letters[idx]
#             idx += 1
#     print( result)

# solve("ahmed als")
# solve("codewars")#,"srawedoc"
# solve("your code")#"edoc ruoy"
# solve("your code rocks") #,"skco redo cruoy"
# solve("i love codewars") #,"s rawe docevoli"
#===================================  21 ========================================+=
# def to24hourtime(hour, minute, period):
#     reaslt = ''
#     if period == 'am' and hour == 12:
#         hour = 0
#     elif period == 'pm' and hour < 12:
#         hour += 12
#     if hour < 10 :
#         reaslt += '0'
#     reaslt+=str(hour)
#     if minute < 10 :
#         reaslt += '0' 
#     reaslt += str(minute)
#     print(reaslt)
# to24hourtime( 1,  0, 'am') # '0100'
# to24hourtime( 1,  0, 'pm') # '1300'
# to24hourtime(12,  0, 'am') # '0000'
# to24hourtime(12,  0, 'pm') # '1200'
# to24hourtime( 6, 30, 'am') # '0630'
# to24hourtime( 9, 45, 'pm') # '2145'
#====================================  22 =======================================+=
# def digits(num):
#     s = str(num)
#     arry = []
#     for i in range(len(s)):
#         for j in range(i+1, len(s)):
#             x = int(s[j])+int(s[i])
#             arry.append(x)
#     print( arry)

# digits(123245)
#======================================  23 =====================================+=
#  solving 1
# def find_deleted_number(arr, mixed_arr):
#     mixed = sorted(mixed_arr)
#     print(mixed)
#     for i in arr:
#       if i not in  mixed:
#         print(i)

#  solving 2

# def find_deleted_number(arr, mixed_arr):
#     mixed = sorted(mixed_arr)
#     if len(arr) == len(mixed):
#         return 0
#     for i,k in zip(arr , mixed):
#         if i  !=  k:
#             return(i)
#     return arr[-1]

# find_deleted_number([1,2,3,4,5], [3,4,1,5])
#=====================================  24 ======================================+=
# def elements_sum(arr):
#     reazelt =0
#     length = len(arr)
#     for i in range(length):
#       indexcount = (length - 1) - i
#       if len(arr[i]) > indexcount:
#         reazelt += arr[i][indexcount]
#     print(reazelt)
# elements_sum([[3, 2, 1, 0], [4, 6, 5, 3, 2], [9, 8, 7, 4]])  #16
# elements_sum([[3], [4, 6, 5, 3, 2], [9, 8, 7, 4]])  #15
# elements_sum([[3, 2, 1, 0], [4, 6, 5, 3, 2], []])# 7
# elements_sum([[3, 2, 1, 0], [4, 6, 5, 3, 2], []], 5)  #12
# elements_sum([[3, 2], [4], []]), 0
#=====================================  25 ======================================+=




# def most_frequent_item_count(collection):
#     reazelt = 0
#     for i in collection:
#         count =0
#         for j in collection:
#             if i == j:
#                 count += 1
#         if count > reazelt :
#             reazelt = count
#     print(reazelt)
# most_frequent_item_count([1,1,2,3,4,5,3,21,1,1])
# most_frequent_item_count([1,1,2,3,4,1,1,1,1,1,1,5,3,21,1,1])
#=====================================  26 ======================================+=
# def explode(arr):
#     if isinstance(arr[0], int) and isinstance(arr[1], int):
#         num = arr[0] + arr[1]
        
#     elif isinstance(arr[0], int):
#         num = arr[0]
#     else:
#         num = arr[1]
#     array = []
#     for i in range(num):
#         array.append(arr)
#     print(array) 
# explode([9,3])
# explode([9,'s'])
# explode(['l',2])
    # Do your magic. :)
   
#====================================  27 =======================================
# def elevator_distance(array):
#     rezelt = 0
#     for i in range(len(array)-1):
#       rezelt += abs(array[i]-array[i+1]) 
#     return(rezelt)
#     # your code here
# elevator_distance([7,1,7,1])
#====================================  28 =======================================
# def solve(strings : list[str]) -> list[int]:
#     num =0
#     lists=[]
#     for word in strings:
#       for index,char in enumerate(word):
#         print(ord(char))
#         if ord(char) ==index+ 97 or ord(char) == index + 65 :
#           num += 1
#       lists.append(num)
#       num = 0
#     print(lists)
# solve(["abode","ABc","xyzD"] ) #[4,3,1]

#====================================  29 =======================================
# def string_to_array(s):
#     nou =[]
#     a=''
#     for i in s:
#         if i != ' ':
#             a+=i
#         else: 
#             nou.append(a)
#             a = ''
#         if a:
#           nou.append(a)
#     return nou
#string_to_array('ahmrf alsafi')
#====================================  30 =======================================
# def sum_array(arr):
#     if arr is None or len(arr)==0:
#          return None
#     else:
#         num = arr[0]
#         num2 =arr[0]
#         for i in arr:
#             if i > num:
#                 num = i
#         for i in arr:
#             if i < num2:
#                 num2 = i
#         print(num - num2)
# sum_array([1,2,3,2,5,5])
# sum_array([])
#====================================  31 =======================================
# def reverse_seq(n):
    # now =[]
    # for i in range(1,n+1 ):
        
    #     now.insert(n, i)
    # now.reverse()
#     print(now)
# reverse_seq(5)
#=====================================  32 ======================================
# def opposite(n):
#     if n > 0:
#         return n * -1
#     print( float((n * n)/2))
# opposite(-2.864255672)
  # your solution here
#=======================================  33 ====================================
# def multi_table(n):
#     print('\n'.join(f'{i} * {n} = {i*n}' for i in range(1, 11)))
# multi_table(50)
#=======================================  34 ====================================
# def sum_of_differences(arr):
#     num = sorted(arr, reverse=True)
#     n = 0
#     for i in range(len(arr)-1):
#         n +=( num[i]-num[i + 1] )
# sum_of_differences([1,2,10])
#=========================================   35  ==================================
# def correct(s):
#     now = ''
#     for i in s:
#         if i == '5':
#             i = 'S'
#         elif i == '0':
#             i = 'O'
#         elif i == '1':
#             i = 'I'
#         now +=i
#     print (now)
# correct('ahme501')
#=========================  36 ============================
# def hero(bullets, dragons):
#     print( bullets >= dragons)
# hero(10,110)
#==========================  37 ===========================
# def odd_count(n):
#     num = 0
#     for i in range(int(n/2)):
#         m = int(i - 2)
#         num += 1
#     print (num)
# odd_count(1219570765)
#========================  38 =============================
# def to_alternating_case(string):
#     now =''
#     for i in string :
#         if i.isupper() :
#             now += i.lower()
#         elif i.islower() :
#             now += i.upper()
#         else :
#             now += i
#     print(now)
#to_alternating_case("strAng")
#=======================  39 ============================
# def str_count(strng, letter):
#     num =0
#     for i in strng:
#         if i == letter:
#             num =num+ 1
#     # Your code here ;)
#     print(num)
# str_count("stttrng", 't')
# ====================  40 =========================
# def no_space(x):
#     return x.replace(' ','')
#     #your code here   
# no_space('8 j 8   mBliB8g  imjB8B8  jl  B')
#====================  41 ========================
# def remove_char(s):
#     x = len(s)
#     print(x)
#     for i in s:
#         if i == 0:
#             s.remove(i)
#         elif i == (1 - x):
#             s.remove(i)
#     print(s)
# remove_char("ahmed")
#========================  42 ===========================+
# def grow(arr):
#     x = 1
#     for i in arr:
#         x = x * i 
#     print( x)
#     pass
# grow([1, 2, 3])
#++++++++++++++++++++  43  +++++++++++++++++++++++
# def grow(arr):
#     for i in arr:
#         x =  i * (i)
#         print(x)
#     pass
# grow([1, 2, 3])
# ====================  44 ========================
# def minimum(arr):
#     print(max(arr))
#     #your code here...
# def maximum(arr):
#     print(arr.max())
#     #...and here
# minimum([-52, 56, 30, 29, -54, 0, -110])
#=========================  45 =====================================
# def remove_exclamation_marks(s):
#     now =''
#     for i in s:
#         if i != '!':
#             now +=''.join(i) 
#     print(now)
#     #your code here
# remove_exclamation_marks('oiuyt!')
#======================  46 ======================================
# def quarter_of(n):
#     print( (n + 2) // 3)
# quarter_of(3)
#=======================  47 =====================================
# def solution(j):
#     print("".join(reversed(j)))      
# solution('stsring')
#=======================  48 =====================================
# def is_divisible(n,x,y):
#     if n / x == y:
#         return True
#     else:
#         return False
#     #your code here
# is_divisible(12,3,4)
#=======================  49 =====================================
# def century(year):
#     if year  % 100 == 0:
#         print( year / 100)
#     else:
#         a= int(year / 100 + 1)
#         print(a)
# century(1709)
# century(1999)
# century(1999)
#=======================  50 =====================================
# 
# def generate_shape(n):
#     return '\n'.join("+" * n for _ in range(n))
# generate_shape(3)
# generate_shape(8)
#========================  51 ====================================
# def generate_shape(n):
#     row = "+" * n
#     for i in range(n):
#         print(f'{row} \n')
# generate_shape(5)
#==========================  52 ==================================
# def high_and_low(numbers):
#     # ...
#     x  = max(numbers)
#     d = min(numbers)
#     print(x,d)
#     return  x,d
# high_and_low('1 2 3 4 5') # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
#==========================  53 ==================================
# def filter_list(l):
#     newList = []
#     list2 = []
#     for i in l :
#         if (isinstance(i, int)):
#             newList.append(i)
#         elif (isinstance(i, str)):
#             list2.append(i)
#     last = (newList,list2)
#     print(last)
#     return last
# filter_list([1, 2, "a", "b"])
# filter_list([1, 'a', 'b', 0, 15])
# filter_list([1, 2, 'aasf', '1', '123', 123])
# filter_list([1, 2, 'aasf', '1', '123', 123])
#===========================  54 =================================
# def count_bits(n):
#     print( bin(n).count("1"))
# count_bits(190)
#=+=================================  53  =========================================+=
# def get_sum(a,b):
#     su = 0
#     if a<b:
#         for i in range(a,b+1):
#             print(i)
#             su  += i
#     else:
#         for i in range(b,a+1):
#             print(i)
#             su  += i
#     return su
#=+=================================  54  =========================================+=
# def comp(array1, array2):
#     if array1 is None or array2 is None:
#         return False
#     if len(array1) != len(array2):
#         return False
#     for i ,j in zip(sorted(array1), sorted(array2)):
#         if i * i != j:
#             return False
        
#     return True

# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
# comp(a1, a2)#, True
# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
# comp(a1, a2)#, False)
# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
# comp(a1, a2)#, False)
#=+=================================  55  =========================================+=
# def solution(s):
#     return ''.join(i if not i.isupper() else ' ' + i for i in s)
# solution("camelCasing")#,"camel Casing")
# solution("camelCasingTest")#,"camel Casing Test")

#=+=================================  56  =========================================+=
# def series_sum(n):
#     return ''.join(f"{sum(1/(1+3*i) for i in range(n)):.2f}")
# print(series_sum(1))#,"1.00")
# print(series_sum(2))#,"1.25")
#=+=================================  57  =========================================+=
# def solution(nums):
#     return [] if nums is  None else sorted(nums)
# print(solution(None))# , [])
# print(solution([1, 2, 3, 10, 5]))# , [1, 2, 3, 5, 10])  
# print(solution([5, 4, 3, 2, 1]))# , [1, 2, 3, 4, 5])
#=+=================================  58  =========================================+=

# def interlockable(a, b): 
#     print (True if  (str(bin(a)[2:]).find('0') >=1) and (str(bin(b)[2:]).find('0')>=1) else False)
        
# interlockable( 9, 4)#,  True )
# interlockable( 3, 6)#, False )
# interlockable( 2, 5)#,  True )                            
# interlockable( 7, 1)#, False )
# interlockable( 0, 8)#,  True ) 
#=+=================================  59  =========================================+=

# def duplicate_count(text):
#     text = text.lower()
#     count= 0
#     li=[]
#     for i in set(text):
#         if text.count(i)>1:
#             count+=1
#             li.append(i)
#     print(li,count)
# duplicate_count('Indentationfrro')#5
# duplicate_count("abcde")#,   0, 'duplicate_count("abcde")'  )
# duplicate_count("abcdeaa")#, 1, 'duplicate_count("abcdeaa")')
# duplicate_count("abcdeaB")#, 2, 'duplicate_count("abcdeaB")')
# duplicate_count("Indivisibilities")#, 2, 'duplicate_count("Indivisibilities")')


#=+=================================  60  =========================================+=
# # def find_it(seq):
# #     num= 0
# #     lists= list(set(seq))
# #     print(lists)
# #     for i in lists:
# #         if seq.count(i)%2==1:
# #             print(i)
# #             num = i
# #     print (num)
    
# # find_it([20,20,1,1,2,2,2])


#=+=================================  61  =========================================+=
# def bool_to_word(boolean):
#     return 'Yes' if  boolean else 'No'
# print(bool_to_word(True))#,'Yes')
# print(bool_to_word(False))#,'No')
#=+=================================  62  =========================================+=
# def unique_in_order(sequence):
#     result = []
#     for item in sequence:
#         if not result or item != result[-1]:
#             result.append(item)
#     return result

# print(unique_in_order('AAAABBBCCDAABBB'))#['A', 'B', 'C', 'D', 'A', 'B'])
#=+=================================  63  =========================================+=
# def longest(a1, a2):
#     return ''.join((set(a1+a2))) 
# longest("aretheyhere", "yestheyarehere")#,"aehrsty")
# print(longest("loopingisfunbutdangerous", "lessdangerousthancoding"))#,"abcdefghilnoprstu")
#=+=================================  64  =========================================+=
# def swap(s):
# # return s.swapcase() # this the same solution but i want to do it by myself
#     result = ''
#     for i in s:
#         if i in "ABCDEFGHIJKLMNOPQURSTVWXYZ":
#             result += i.lower()
#         elif i in 'abcdefghijklmnopqurstvwxyz':
#             result += i.upper()
#         else:
#             result += i
#     return result
# swap("Hello World")#,"hELLO wORLD")
# swap("vR0.sfKErA62 b,F5Yce_.MwQ,Q 2 HLmQ2 97")
#=+=================================  65  =========================================+=
# kata level 6
# def create_phone_number(n):
#     # return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
#     return f"({str(n[0])+str(n[1])+str(n[2])}) {str(n[3])+str(n[4])+str(n[5])}-{str(n[6])+str(n[7])+str(n[8])+str(n[9])}"
# print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))#,"(123) 456-7890")

#=+=================================  66  =========================================+=
# Kata level 6
# def two_sum(nums, t):
#     for i, x in enumerate(nums):
#         for j, y in enumerate(nums):
#             if i != j and x + y == t:
#                 return [i, j]

# print(two_sum([1, 2, 3, 5], 6))#,[0, 3])
#    #   numbers       target   valid results
    
# print(two_sum([1 ,2, 3],            4))#,[0, 2])
# print(two_sum([1234,5678,9012], 14690))#,[1, 2])
# print(two_sum([2, 2, 3],            4))#,[0, 1])
# #=+=================================  67  =========================================+=
# def sumdigits(number):
#     return sum(int(i) for i in str(number) if i.isdigit())
# print(sumdigits(10))#1
# print(sumdigits(99))#18
#=+=================================  68  =========================================+=

# def factorial(m):
#     n = 1
#     if m < 0:
#         print("error")
#     for i in range(1,m+1):
#         n *= i
#     print(n)
# factorial(0) #1
# factorial(-1) #1
# factorial(24) #2
#=+=================================  69  =========================================+=\
# def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
#     n = []
#     for i in range(a,b): # 135
#         total = 0
#         for j,k in enumerate(str(i)): # "1"
#             total += int(k)**(j+1) # 1**1
#             if total == i:
#                 n.append(i)
#     return n
# print(sum_dig_pow(1, 10))#,[1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(sum_dig_pow(1, 100))#,[1, 2, 3, 4, 5, 6, 7, 8, 9, 89])

# #=+=================================  70  =========================================+=
# def reverse(st):
#     return  "".join(i+' ' for i in reversed(st.split(" ")))[:-1]
# print(reverse('Hello World'))#,'World Hello')

# #=+=================================  71  =========================================+=
# def capitals(word):
#     return [ j for j,i in enumerate(word) if i.isupper()]    
# print(capitals('CodEWaRs'))#[0, 3, 4, 6])   

#=+=================================  72  =========================================+=

# def is_pangram(st):
#     alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"    
#     s = "".join(dict.fromkeys(st))
#     for i in s:
#         if i.upper() in alpha:
#             alpha = alpha.replace(i.upper(), '')
#     return alpha == ''
# print(is_pangram("ABCDEFGHIJKLMNOPQRSTUVWXYz"))#True
# print(is_pangram("This is not a pangram."))#False
#=+=================================  73  =========================================+=
# def expanded_form(num):
#     # "70304"  5   4
#     # 7 + '0' * 4
#     # 0    0 * 3
#     #  3 + 0 * 2
#     # 0 +  0 * 1
#     # 4 +  0 * 0
#     s = str(num)
#     result = ''
#     for j,i in enumerate(s):
#         if int(i) != 0 :
#             l = i + ('0'*(len(s)- 1 - j ))
#             result += l + " + "
#     return result[:-3]
# print(expanded_form(70309874))#,"70000 + 300 + 4")

# #=+=================================  74  =========================================+=
# def duplicate_encode(word):
#     word = word.lower()
    
#     result = ''
    
#     for i in word:
#         if word.count(i) == 1:
#             result += '('
#         else:
#             result += ')'
    
#     return result
# print(duplicate_encode("din"))#,"((("
# print(duplicate_encode("recede"))#,"()()()"
# print(duplicate_encode("Success"))#,")())())"
# print(duplicate_encode("(( @"))#,"))(("
#=+=================================  75  =========================================+=
# def binary_array_to_number(arr):
#     s = ''.join(str(i) for i in arr)
#     return int(s,2)
# print(binary_array_to_number([0,0,0,1]))#1
# print(binary_array_to_number([0,0,1,0]))#2


# def binary_array_to_number(arr):
#     s = 0 # 1 + 3 + 7 + 15
#     for digit in arr: # 1 1 !
#         s = s * 2 + digit # 1

#     return s
# print(binary_array_to_number([1,1,1,1]))#1

#=+=================================  76  =========================================+=
# def likes(names):
#     if names ==  []:
#         return 'no one likes this'
#     elif len(names) == 1:
#         return f'{names[0]} likes this'
#     elif len(names) == 2:
#         return f'{names[0]} and {names[1]} like this'
#     elif len(names) == 3:
#         return f"{names[0]}, {names[1]} and {names[2]} like this"
#     else:
#         return f'{names[0]}, {names[1]} and {len(names)-2} others like this'
        
        

# print(likes([]))#,'no one likes this')
# print(likes(['Peter']))#,'Peter likes this')
# print(likes(['Peter', 'John']))#,'Peter and John like this')
# print(likes(['Peter', 'John', 'Mark']))#,'Peter, John and Mark like this')
# print(likes(['Alex', 'Jacob', 'Mark', 'Max']))#,'Alex, Jacob and 2 others like this')   
#=+=================================  77  =========================================+=
# def sort_array(ar):
#     evens = sorted(x for x in ar if x % 2 == 1)
#     result = []
#     j = 0
#     for x in ar:
#         if x % 2 == 1:
#             result.append(evens[j])
#             j += 1
#         else:
#             result.append(x)
#     return(result)
# print(sort_array([5, 3, 2, 8, 1, 4]))#[1, 3, 2, 8, 5, 4])

#=+=================================  78  =========================================+=
# def distinct(seq):
#     return list(dict.fromkeys(seq))
# print(distinct([1, 2, 1, 4, 1, 3]))#[1, 2, 4, 3])
# for i in enumerate
#=+=================================  79  =========================================+=
# # NORTH ↔ SOUTH
# # EAST  ↔ WEST
# def dir_reduc(arr):
#     result  = []
#     for j ,i in enumerate(arr):
#         if result == []:
#             result.append(i)
#         elif( result[-1] == 'NORTH' and i  == 'SOUTH'):
#             result.pop()
#         elif result[-1] == 'WEST' and i == 'EAST':
#             result.pop()
#         elif( i == 'NORTH' and result[-1]  == 'SOUTH'):
#             result.pop()
#         elif i == 'WEST' and result[-1] == 'EAST':
#             result.pop()
#         else:
#             result.append(i)
#     return(result)
# print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))#["WEST"])
# print(dir_reduc(["NORTH", "WEST", "SOUTH", "EAST"]))#["NORTH", "WEST", "SOUTH", "EAST"])
#=+=================================  80  =========================================+=
# def sum_of_minimums(n):
#     return sum(min(n[i]) for i in range(len(n)))
# print(sum_of_minimums([[7, 9, 8, 6, 2], [6, 3, 5, 4, 3], [5, 8, 7, 4, 5], [4, 8, 9, 9, 1], [6, 7, 8, 5, 4]]))#14
#=+=================================  81  =========================================+=
# def min_value(digits):
#     sor = sorted(set(digits))
#     return int(''.join(str(i) for i in sor))
# # #print(min_value([1, 3, 1, 5, 0]))#1035
# #=+=================================  82  =========================================+=
# def domain_name(url):
#     url = url.replace("http://", "")
#     url = url.replace("https://", "")
#     url = url.replace("www.", "")
    
#     return url.split(".")[0]

# #print(domain_name("http://github.com/carbonfive/raygun"))#,"github")

# #=+=================================  83  =========================================+=
# def find_multiples(integer, limit):
#     arr = []
#     i = 1
#     while i * integer <= limit:
#         arr.append(i * integer)
#         i += 1
#     return arr
# print(find_multiples(5, 25))#[5, 10, 15, 20, 25])
# =+=================================  84  =========================================+=
# def find_uniq(arr):
#     n = 0
#     for i in set(arr):
#         if arr.count(i) == 1:
#             n += i
#     return n
# print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))#2
# print(find_uniq([ 0, 0, 0.55, 0, 0 ]))#0.55
#=+=================================  85  =========================================+=
# def remove_url_anchor(url):
#   return url.split('#')[0]
# print(remove_url_anchor('codewars.com#about'))#,'www.codewars.com')

#=+=================================  86  =========================================+=
# def descending_order(num):
#     return int(''.join(sorted(str(num), reverse = True)))
# print(descending_order(0))#0
# print(descending_order(1))#1
# print(descending_order(123456789))#987654321
#=+=================================  87  =========================================+=
# def split_str(st):
#     result = []
#     for i in st.split(' '): # " Ahmed alsafi"
#         result.append(list(i))
#     return result
    # return [list(i) for i in st.split(' ')]
            
# print(sep_str("Ahmed alsafi"))#[['A','h','m','e','d'], ['a','l','s','a','f','i']]
#=+=================================  88  =========================================+=
# def sep_str(st):
#     words = st.split()
#     max_len = max((len(word) for word in words), default=0) # 5
#     result = []
#     for i in range(max_len):
#         row = []
#         for word in words:
#             if i < len(word):
#                 row.append(word[i])
#             else:
#                 row.append('')
#         result.append(row)
#     return result
# print(sep_str("Ahmed alsafi"))#
#[['A','a'],
# ['h','l'], 
# ['m','s'], 
# ['e','a'], 
# ['d','f'], 
# ['' ,'i']] 

# the same solution but with list comprehension
# from itertools import zip_longest
# def sep_str(st):
#     return [[*cs] for cs in zip_longest(*st.split(), fillvalue='')]
# print(sep_str("Ahmed alsafi"))#
# #[['A','a'],
#=+=================================  89  =========================================+=
# def add_length(str_):
#     return ["{} {}".format(i, len(i)) for i in str_.split(' ')]
# def add_length(str_):
#     result = []
#     s = ''
#     for i in str_:
#         s+=i
#         if i == ' ':
#             result.append((s + str(len(s)-1) ))
#             s = ''
#     result.append((s +" "+ str(len(s))))
#     return result        
# print(add_length('ahmed alsafi'))#['ahmed 5', 'alsafi 6']
#=+=================================  90  =========================================+=
# def to_jaden_case(string):
#     return ''.join(i[0].upper()+i[1:].lower()+' ' for i in string.split(" "))[:-1]


# print(to_jaden_case("How can mirrors be real if our eyes aren't real"))#,"How Can Mirrors Be Real If Our Eyes Aren't Real")
# print(to_jaden_case("hello world't"))#,"Hello World't")
#=+=================================  91  =========================================+=
# def bouncing_ball(h, bounce, window):
#     count = 1 
#     if h <= 0  or  bounce <= 0 or bounce >= 1 or window >= h:
#         return -1
#     count = 1
#     h *= bounce
#     while h > window:
#         count += 2
#         h *= bounce 
#     return count 

#=+=================================  92  =========================================+=
# def calculator(x,y,op):
#     if not isinstance(x, int) or not isinstance(y, int):
#         return 'unknown value'
    
#     if op == '+':
#         return x + y
        
#     if op == '-':
#         return x - y
        
#     if op == '*':
#         return x * y
        
#     if op == '/':
#         return x / y
        
#     return 'unknown value'

#=+=================================  93  =========================================+=
#=+=================================  94  =========================================+=
#=+=================================  95  =========================================+=
#=+=================================  96  =========================================+=
#=+=================================  97  =========================================+=
#=+=================================  98  =========================================+=
#=+=================================  99  =========================================+=
#=+=================================  100 =========================================+=
#=+=================================  101 =========================================+=
#=+=================================  102 =========================================+=
#=+=================================  103 =========================================+=
#=+=================================  104 =========================================+=
#=+=================================  105 =========================================+=
#=+=================================  106 =========================================+=
#=+=================================  107 =========================================+=
#=+=================================  108 =========================================+=
#=+=================================  109 =========================================+=
#=+=================================  111 =========================================+=
#=+=================================  112 =========================================+=
#=+=================================  113 =========================================+=
#=+=================================  114 =========================================+=
#=+=================================  115 =========================================+=
#=+=================================  116 =========================================+=
#=+=================================  117 =========================================+=
#=+=================================  118 =========================================+=
#=+=================================  119 =========================================+=
#=+=================================  120 =========================================+=
#=+=================================  121 =========================================+=
#=+=================================  122 =========================================+=
#=+=================================  123 =========================================+=
#=+=================================  124 =========================================+=
#=+=================================  125 =========================================+=
#=+=================================  126 =========================================+=
#=+=================================  127 =========================================+=
#=+=================================  128 =========================================+=
#=+=================================  129 =========================================+=
#=+=================================  130 =========================================+=

# s = "hello World 123"

# print(s.swapcase())   
# print(s.title())      
# print(s.islower())    
# print(s.isdigit())   
# print(s.isalpha())
# print(s.isalnum())
# print(s.split())
#  set -> to give a unique value
# print(s.replace(" ", "_"))
# for i in enumerate(s):