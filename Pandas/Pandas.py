import pandas as pd


#显示所有列
#显示所有行
#设置value的显示长度为100，默认为50
# print(pd.get_option('display.max_colwidth'))
# pd.set_option("max_colwidth", 1)
# print(pd.get_option('display.max_colwidth'))
# df = pd.DataFrame(
#     {'Name': ['12222222222', '2', '3'],
#      'Age': [10, 11, 12],
#      'Sex': ['male', 'male', 'female']
#      }
# )
df = pd.DataFrame({'text': ['foo foo foo foo foo foo foo foo', 'bar bar bar bar'],
                   'number': [1, 2]})

# print(df['Age'])

# hello = pd.Series(data=[4, 5, 6], name='hello')
# print(hello)
#
# print(df['Age'].max())
# print(df.describe())
# print(df)
# df.to_excel('1.xlsx', index=False)  # 保存csv文件
df.style.set_properties(subset=['text'], **{'width': '1000px'})

print(df)
df.to_excel('1.xlsx', index=False)


# b = pd.read_csv('1.csv')
# # print(b)
# # print(b.head(2))  # 看的是行
# # print(b.tail(2))  # 后2行
# # print(b['Age'].shape)
# # print(b['Age'].isin([10]))
# c = b[b['Age'].isin([10])]
# # print(c.head())
# df['Age'] = (1 / 2)  # 会遍历每一个值进行运算，牛啊
# print(df)
# # 添加列的方法 -1
# df.insert(df.shape[1], 'hello', [11, 12, 13])
# print(df.shape)  # 返回的是行列
# # 添加列的方法 -2
# df['he'] = ['wa', 'wa', 'wa']
# print(df)
# # 添加行的方法 -3 需要重新复制
# df2 = pd.DataFrame({'Name': ['1', '2', '3'],
#                     'Age': [10, 11, 12],
#                     'Sex': ['male', 'male', 'female']
#                     })
# df3 = df.append(df2, ignore_index=True)
# print(df3)
# # 添加行的方法 -2
# df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
# df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
# df3 = df.append(df2, ignore_index=True)
# print(df3)
# # 添加行的方法 -3
# df.loc[df.shape[0]] = [1, 2]
# print(df)
