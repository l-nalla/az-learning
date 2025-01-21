# for loop is used to iterate over a collection like list, tuple, string, dict

# for (start, end, increment){
# }

sentence = "Hello world"

# for ele in sentence:
#     print(ele)


# l1 = ["abc", 'bvc', 'dfdc', 'dfd'] # first counts the len of iterable obj len(ite obj) 0 -> len-1

# for ele in l1:
#     print(ele, end=",")


nums_1_100 = [i for i in range(1,101)]

# for ele in nums_1_100:
#     if ele % 2 == 0:
#         print(ele)

for ele in range(0,100,2):
    print(ele)