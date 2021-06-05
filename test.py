# print('Hello world')

# print('Hello world')

# print('Hello world')


# #演算
# print(1+1)
# print(1-1)
# print(2*2)
# print(10/2)
# print(5%3)

# 変数
# comment = 'l_size'
# comment_length = 5
# comment_times = 5.5
# print(comment)

# 条件分岐と関係演算子
# if else elif
# ==, !=, <, >, >=, <=

# if comment_length < 3:
#   print('dekai!')
# else:
#   print('sukunai')

関数


def unko_funbaru(arg):
    unko_status = arg

    if unko_status < 10:
        return "mada daijobu"
    else:
        return "yabai"


print(unko_funbaru(5))

lists
unko_list = ["unko_small", "unko_medium", "unko_large"]
print(unko_list[1])


a = [["sato", "tanaka"], ["yamada", "jirou"]]
print(a[0][0])
print(a[0][1])
print(a[1][0])
print(a[1][1])


a= [1, 2, 3, 4]


# forF
# for index in range(12):
#     print(unko_funbaru(index))

# for item in unko_list:
#     print(item)

# with
# open()
# with open('./text.txt', 'r') as file:
#     print(file.read())

# class
# class Card:
#     def __init__(self, date, user_name):
#         self.date = date
#         self.user_name = user_name
#     def message(self):
#         return 'この投稿は' + self.user_name + 'さんが' + self.date + 'に投稿しました'

# date_a = '2020-01-01'
# user_name_a = 'Taro'

# date_b = '2020-09-21'
# user_name_b = 'Kayoko'
# card_b = Card(date_b, user_name_b)

# card_a = Card(date_a, user_name_a)

# print(card_b.message())

# import
# import math
# print(math.pi)


# Pythonのライブラリpypiで検索
# NumPy
# Pandas
# Flask
# Django


print("new")
