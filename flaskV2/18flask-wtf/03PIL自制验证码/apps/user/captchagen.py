"""
@File    :captchagen.py
@Editor  : 百年
@Date    :2025/11/10 12:19
"""
from PIL import Image, ImageDraw, ImageFont,ImageFilter
import random
import string


def randcolor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def generate_captcha(length, exclude_similar=True):  # 生成指定长度的验证码

    # 先组好验证码
    base_chars = string.ascii_letters + string.digits
    if exclude_similar:
        similar_chars = {'0', 'O', '1', 'l', 'I', 'o'}
        base_chars = [c for c in base_chars if c not in similar_chars]
    code_parts = [random.choice(base_chars) for _ in range(length)]
    final_code = ''.join(code_parts)
    print(final_code)
    # 组成验证码结束
    width, height = 130, 50
    img = Image.new("RGB", (width, height), randcolor())
    img_draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype('arial.ttf', 20)  # 指定字体像素为20
    except IOError:
        font = ImageFont.load_default()

    # tips:计算每个字符的位置,均匀分布+随机微调
    char_width = width // length  # 每个字符大致占的宽度
    for i, char in enumerate(final_code):
        x = i * char_width + random.randint(-1, 5)
        y = random.randint(5, 15)
        img_draw.text((x, y), char, fill=randcolor(), font=font)
    # img.show()
    # 可选：添加干扰线或点（增强安全性）
    for _ in range(3):
        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 = random.randint(0, width), random.randint(0, height)
        img_draw.line((x1, y1, x2, y2), fill=randcolor(), width=1)

    for _ in range(100):
        x, y = random.randint(0, width), random.randint(0, height)
        img_draw.point((x, y), fill=randcolor())
    img.filter(ImageFilter.BLUR)
    # img.show()
    return final_code,img

# if __name__ == '__main__':
#     generate_captcha(6)
#测试完毕