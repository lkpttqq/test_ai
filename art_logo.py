#!/usr/bin/env python3
"""艺术字符Log生成工具"""

def generate_art_logo(text):
    """生成艺术字符Logo"""
    chars = {
        '思': [
            "  ██████  ",
            " ██    ██ ",
            "  ██████  ",
            " ██    ██ ",
            "  ██████  "
        ],
        '逸': [
            " ████████ ",
            "██░░░░░░██",
            "  ██████  ",
            " ██    ██ ",
            " ████████ "
        ],
        '科': [
            " ████████ ",
            "██░░░░░░██",
            "  ██████  ",
            "  ██  ██  ",
            "  ██████  "
        ],
        '技': [
            "████████  ",
            "██      ██",
            " ████████ ",
            "██      ██",
            "████████  "
        ]
    }

    lines = ["", "", "", "", ""]
    for char in text:
        char_art = chars.get(char, [f"  {char}  "] * 5)
        for i in range(5):
            lines[i] += char_art[i] + "  "

    return "\n".join(lines)


def main():
    logo = generate_art_logo("思逸科技")
    print("=" * 60)
    print("艺术字符Log生成工具")
    print("=" * 60)
    print(logo)
    print("=" * 60)


if __name__ == '__main__':
    main()