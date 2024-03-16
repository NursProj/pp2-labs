import re
strings = input()
#1
# def pattern_1(strs):
#     pattern = 'ab*'
#     return re.fullmatch(pattern, strs)
# print(pattern_1(strings))

#2
# def pattern_2(strs):
#     pattern = 'ab{2,3}'
#     return re.fullmatch(pattern, strs)
# print(pattern_2(strings))

#3
# def sequence_3(strs):
#     pattern = '[a-z]+_[a-z]+'
#     return re.fullmatch(pattern, strs)
# print(sequence_3(strings))
    
#4
# def sequence_4(strs):
#     pattern = '[A-Z][a-z]+'
#     return re.fullmatch(pattern, strs)
# print(sequence_4(strings))
    
#5
# def pattern_5(strs):
#     pattern = '^a.*b$'
#     return re.match(pattern, strs)
# print(pattern_5(strings))

#6
# def replace_6(strs):
#     pattern = r'[ ,.]'
#     return re.sub(pattern, ':', strs)
# print(replace_6(strings))

#7
# def snake_to_camel(strs):
#     components = strs.split('_')
#     return components[0] + ''.join(x.title() for x in components[1:])
# print(snake_to_camel(strings))

#8
# def split_at_uppercase(strs):
#     return re.findall('[A-Z][a-z]*', strs)
# print(split_at_uppercase(strings))

#9
# def insert_space(strs):
#     return re.sub(r'(?<=[a-z])([A-Z])', r' \1', strs)
# print(insert_space(strings))

#10 
def camel_to_snake(strs):
    snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', strs)
    return snake_case.lower()
print(camel_to_snake(strings))
