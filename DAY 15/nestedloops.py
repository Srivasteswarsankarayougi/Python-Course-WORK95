# for row in range(3):
#     for col in range(5):
#         print(col,end = ' ')
#     print()


# for row in range(5):
#     for col in range(5):
#         print('#',end = ' ')
#     print()

# '''
# output
# # # # # # 
# # # # # # 
# # # # # # 
# # # # # # 
# # # # # # 
# '''


# #question 3
# '''
# output:

#    0 1 2 3 4
# 0  1 0 1 0 1 
# 1  0 1 0 1 0 
# 2  1 0 1 0 1 
# 3  0 1 0 1 0 
# 4  1 0 1 0 1 

# 1 = 00 02 04 = 0 2 4 = even no
# 0 = 01 03 = 1 3 = odd no
# logic if int = even print 1


# '''

# for row in range(5):
#     for col in range(5):
#         print( int((col+row) % 2 == 0),end=' ')
#     print()



# #question 4
# '''
#    0 1 2 3 4
# 0  0 1 0 1 0 
# 1  0 1 0 1 0 
# 2  0 1 0 1 0 
# 3  0 1 0 1 0 
# 4  0 1 0 1 0 

# 1 - 00 01 02 03 04 = 
# '''

# for row in range(5):
#     for col in range(5):
#         print( col%2,end=' ')
#     print()


# count = 2

# for row in range(5):
#     for col in range(5):
        
#         print(count,end = ' ')
#         count += 2

#     print()




# count = 1

# for row in range(5):
#     for col in range(5):
        
#         print(count,end = ' ')
#         count += 1

#     print()


# #    0 1 2 3 4
# # 0  0 0 0 0 0 
# # 1  0 1 2 3 4 
# # 2  0 2 4 6 8 
# # 3  0 3 6 9 12
# # 4  0 4 8 12 16


# for row in range(5):
#     for col in range(5):
#         print(row*col , end = ' ')
#     print()



#star pattern
# n  = int(input("enter the num:"))
# for row in range(n):
#     for col in range(row+1):
        
         
#          print( '*', end = ' ')

#     print()




n = int(input("enter the num:"))

for row in range(n):
    for col in range(n-row):
        print('*', end=' ')
    print()