# 1. 파일 읽기

# 1.1 파일 전체 읽기
# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())

# 1.2 파일 경로
# 윈도우 \
# 리눅스 /

# 1.3 한 행씩 읽기
# filename = 'pi_digits.txt'

# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

# 1.4 파일에서 행 리스트 만들기
# filename = 'pi_digits.txt'

# with open(filename) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())

# 1.5 파일 콘텐츠 다루기
# filename = 'pi_digits.txt'

# with open(filename) as file_object:
#     lines = file_object.readlines()

# pi_string = ''
# for line in lines:
#     pi_string += line.strip()

# print(pi_string)
# print(len(pi_string))

# 2. 파일에 쓰기
# 2.1 빈 파일에 쓰기
# filename = 'programming.txt'

# with open(filename, 'w') as file_object:
#     file_object.write('I love programming.')

# 3. 예외처리

try: 
    print(5 / 0)
except:
    print('불가능합니다')