def str_blocks(text: str, block_len: int = 300, step_len: int = 300) -> list:
    '''字符串跳跃分块

    从多行字符串中，每次取 block_len 行，然后跳过 step_len 行，循环如此

    参数列表
    ----------
    text : str
        被提取的多行字符串
    block_len : int, 可选
        每次取的行数, 默认值 300
    step_len : int, 可选
        每次跳过的行数, 默认值 300

    返回值
    -------
    list
        提取到的块列表，每个块中是 block_len 行字符串
    '''
    lines = text.splitlines()
    i = 0
    blocks = []
    while True:
        item: str = lines[i : i + block_len]
        i += block_len + step_len
        if not item:
            break
        blocks.append('\n'.join(item))
    return blocks


if __name__ == '__main__':
    code: str = open('3000_line', 'r', encoding='utf-8').read()
    blocks = str_blocks(code)
    for i in blocks:
        print(i.splitlines()[0])
