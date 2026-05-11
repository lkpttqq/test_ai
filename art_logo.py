#!/usr/bin/env python3
"""艺术字符Log生成工具"""

import sys
import pyfiglet


def generate_art_logo(text, font='banner'):
    """生成艺术字符Logo

    Args:
        text: 要生成的标题（支持中英文）
        font: 字体样式，默认为banner
    """
    try:
        ascii_art = pyfiglet.figlet_format(text, font=font)
        return ascii_art
    except Exception as e:
        return f"生成失败: {e}"


def main():
    if len(sys.argv) > 1:
        text = sys.argv[1]
    else:
        text = "KST"

    font = sys.argv[2] if len(sys.argv) > 2 else 'banner'

    print("=" * 60)
    print("艺术字符Log生成工具")
    print("=" * 60)
    print(f"标题: {text}")
    print("-" * 60)
    print(generate_art_logo(text, font))
    print("=" * 60)


if __name__ == '__main__':
    main()