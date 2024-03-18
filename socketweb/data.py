def read_after_specific_char_in_line(file_path, specific_char):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if specific_char in line:
                # 找到指定字符，返回该行指定字符之后的部分
                return line[line.find(specific_char) + len(specific_char):]
                # 如果文件结束仍未找到指定字符，返回空字符串
        return ""

    # 使用函数


file_path = 'data.txt'
specific_char = 'name:'
content_after_char = read_after_specific_char_in_line(file_path, specific_char)
print(content_after_char)