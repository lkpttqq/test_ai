#!/usr/bin/env python3
"""艺术字符Log生成工具 - 支持颜色输出"""

import sys
import pyfiglet
from colorama import init, Fore, Style

init(autoreset=True)

# ANSI颜色码
COLORS = {
    'red': Fore.RED,
    'green': Fore.GREEN,
    'yellow': Fore.YELLOW,
    'blue': Fore.BLUE,
    'magenta': Fore.MAGENTA,
    'cyan': Fore.CYAN,
    'white': Fore.WHITE,
    'reset': Fore.RESET,
}

# 渐变色组合 (参考fastfetch风格)
GRADIENT_COLORS = [
    Fore.RED,
    Fore.YELLOW,
    Fore.GREEN,
    Fore.CYAN,
    Fore.BLUE,
    Fore.MAGENTA,
]


def rainbow_text(text):
    """生成彩虹色渐变文字"""
    result = []
    for i, char in enumerate(text):
        color = GRADIENT_COLORS[i % len(GRADIENT_COLORS)]
        result.append(f"{color}{char}{Fore.RESET}")
    return ''.join(result)


def apply_color(text, color_name='white'):
    """应用单一颜色"""
    color = COLORS.get(color_name.lower(), Fore.WHITE)
    return f"{color}{text}{Fore.RESET}"


def gradient_print(text, font='banner'):
    """生成渐变色艺术字"""
    ascii_art = pyfiglet.figlet_format(text, font=font)
    lines = ascii_art.split('\n')
    colored_lines = []

    for line in lines:
        colored_line = []
        for i, char in enumerate(line):
            if char.strip():
                color = GRADIENT_COLORS[i % len(GRADIENT_COLORS)]
                colored_line.append(f"{color}{char}{Fore.RESET}")
            else:
                colored_line.append(char)
        colored_lines.append(''.join(colored_line))

    return '\n'.join(colored_lines)


def generate_art_logo(text, font='banner', color_mode='gradient'):
    """生成艺术字符Logo

    Args:
        text: 要生成的标题（支持中英文）
        font: 字体样式，默认为banner
        color_mode: 颜色模式 - gradient(渐变), rainbow, 或颜色名如red/green/blue等
    """
    try:
        ascii_art = pyfiglet.figlet_format(text, font=font)
        lines = ascii_art.split('\n')

        if color_mode == 'gradient':
            colored_lines = []
            for line in lines:
                colored_line = []
                for i, char in enumerate(line):
                    if char.strip():
                        color = GRADIENT_COLORS[i % len(GRADIENT_COLORS)]
                        colored_line.append(f"{color}{char}{Fore.RESET}")
                    else:
                        colored_line.append(char)
                colored_lines.append(''.join(colored_line))
            return '\n'.join(colored_lines)
        elif color_mode == 'rainbow':
            return rainbow_text(ascii_art)
        else:
            color = COLORS.get(color_mode, Fore.WHITE)
            return f"{color}{ascii_art}{Fore.RESET}"
    except Exception as e:
        return f"生成失败: {e}"


def main():
    if len(sys.argv) > 1:
        text = sys.argv[1]
    else:
        text = "KST"

    font = sys.argv[2] if len(sys.argv) > 2 else 'banner'
    color_mode = sys.argv[3] if len(sys.argv) > 3 else 'gradient'

    print("=" * 60)
    print("艺术字符Log生成工具")
    print("=" * 60)
    print(f"标题: {text}")
    print(f"颜色模式: {color_mode}")
    print("-" * 60)
    print(generate_art_logo(text, font, color_mode))
    print("=" * 60)


if __name__ == '__main__':
    main()