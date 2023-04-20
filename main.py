from util import str_blocks, get_all_code
from chat import get_result
import os


def get_code_msgs(code_blocks):
    '''生成每个代码块的小结，拼接后输出'''
    # 所有代码块小结
    code_msgs = ''
    for code_block in code_blocks:
        print('正在生成代码块小结...')
        text = '下面是项目的部分代码，请理解这些代码，然后用 200 字概括其使用了哪些编程技术和编程语言、用途是什么\n\n' + code_block
        result = get_result(text)
        code_msgs += result + '\n'
    open('out/代码块小结', 'w', encoding='utf-8').write(code_msgs)
    return code_msgs


def get_main_msg(code_msgs):
    '''生成总结摘要'''
    print('正在生成总结摘要...')
    main_msg = get_result(
        '下面是对同一个项目的不同部分的描述，请综合下面的描述，理解这个项目，然后尽可能详细地描述这个项目，需要包括所用到的技术、编程语言、功能模块、技术特点等\n'
        + code_msgs
    )
    main_msg = main_msg.replace('\n', '')
    open('out/总结摘要', 'w', encoding='utf-8').write(main_msg)
    return main_msg


def get_all_content(main_msg: str):
    all_content = ''
    tasks_str = open('tasks', 'r', encoding='utf-8').read()
    tasks = tasks_str.splitlines()
    i = 1
    for task in tasks:
        print('正在生成正文：' + task)
        cmd = f'''
这是项目的介绍：{main_msg}
这是我要求的大纲：{'、'.join(tasks_str.splitlines())}
我不需要你编写大纲中所有内容，你只需要编写其中的一个模块“{task}”，而且不要超过 500 字。
            '''
        content = get_result(cmd)
        file_path = 'out/' + str(i) + '. ' + task
        i += 1
        open(file_path, 'w', encoding='utf-8').write(content)
        all_content += content + '\n'
    open('out/完整文章', 'w', encoding='utf-8').write(all_content)
    return all_content


if not os.path.exists('out'):
    os.mkdir('out')


if __name__ == '__main__':
    input_code: str = get_all_code('code')
    print('源代码整理完成，共 ' + str(len(input_code.splitlines())) + ' 行')
    code_blocks = str_blocks(input_code)  # 代码块列表
    code_msgs = get_code_msgs(code_blocks)  # 所有代码块小结拼接
    main_msg = get_main_msg(code_msgs)  # 总结摘要
    all_content = get_all_content(main_msg)  # 完整文章内容
    print('完成')
