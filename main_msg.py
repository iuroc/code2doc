from main import get_all_code, str_blocks, get_code_msgs, get_main_msg

if __name__ == '__main__':
    input_code: str = get_all_code('code')
    code_blocks = str_blocks(input_code)  # 代码块列表
    code_msgs = get_code_msgs(code_blocks)  # 所有代码块小结拼接
    main_msg = get_main_msg(code_msgs)  # 总结摘要
    print(main_msg)
