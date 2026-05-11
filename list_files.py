#!/usr/bin/env python3
"""获取当前目录文件列表"""

import os


def list_files(directory='.'):
    """获取目录下的文件列表"""
    files = []
    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)
        if os.path.isfile(full_path):
            files.append({
                'name': item,
                'type': 'file',
                'size': os.path.getsize(full_path)
            })
        else:
            files.append({
                'name': item,
                'type': 'directory',
                'size': 0
            })
    return files


def main():
    print("当前目录文件列表:")
    print("-" * 40)

    files = list_files('.')
    for f in files:
        print(f"{f['name']:<30} {f['type']:<10} {f['size']:>10} bytes")


if __name__ == '__main__':
    main()