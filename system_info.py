#!/usr/bin/env python3
"""系统信息获取程序 - 获取操作系统、CPU、内存、硬盘等硬件信息"""

import platform
import subprocess
import re


def get_os_info():
    return {
        'system': platform.system(),
        'release': platform.release(),
        'version': platform.version(),
        'machine': platform.machine(),
        'processor': platform.processor(),
    }


def get_cpu_info():
    cpu_info = {}

    try:
        with open('/proc/cpuinfo', 'r') as f:
            for line in f:
                if line.startswith('model name'):
                    cpu_info['model'] = line.split(':')[1].strip()
                    break
    except:
        pass

    if not cpu_info.get('model'):
        cpu_info['model'] = platform.processor() or 'Unknown'

    try:
        result = subprocess.run(['lscpu'], capture_output=True, text=True)
        for line in result.stdout.split('\n'):
            if 'Architecture' in line:
                cpu_info['architecture'] = line.split(':')[1].strip()
            elif 'CPU(s)' in line and 'Thread' not in line:
                cpu_info['cores'] = line.split(':')[1].strip()
    except:
        pass

    return cpu_info


def get_memory_info():
    mem_info = {}

    try:
        with open('/proc/meminfo', 'r') as f:
            for line in f:
                if line.startswith('MemTotal'):
                    total_kb = int(re.search(r'\d+', line).group())
                    mem_info['total'] = total_kb * 1024
                elif line.startswith('MemAvailable'):
                    avail_kb = int(re.search(r'\d+', line).group())
                    mem_info['available'] = avail_kb * 1024
                elif line.startswith('MemFree'):
                    free_kb = int(re.search(r'\d+', line).group())
                    mem_info['free'] = free_kb * 1024
    except:
        pass

    try:
        result = subprocess.run(['dmidecode', '-t', '17'], capture_output=True, text=True)
        for line in result.stdout.split('\n'):
            if 'DDR' in line:
                mem_info['type'] = line.strip()
                break
    except:
        mem_info['type'] = 'Unknown'

    return mem_info


def get_disk_info():
    disk_info = []

    try:
        result = subprocess.run(['lsblk', '-d', '-o', 'NAME,MODEL,SIZE,TYPE'], capture_output=True, text=True)
        lines = result.stdout.split('\n')[1:]
        for line in lines:
            if line.strip():
                parts = line.split()
                if len(parts) >= 3:
                    disk_info.append({
                        'name': parts[0],
                        'model': ' '.join(parts[1:-1]),
                        'size': parts[-1] if parts[-1] not in ['NAME', 'MODEL', 'SIZE', 'TYPE'] else 'Unknown'
                    })
    except:
        pass

    if not disk_info:
        try:
            with open('/proc/ide/hda/model', 'r') as f:
                disk_info.append({'model': f.read().strip(), 'size': 'Unknown'})
        except:
            pass

    return disk_info


def main():
    print("=" * 60)
    print("系统硬件信息")
    print("=" * 60)

    os_info = get_os_info()
    print("\n【操作系统信息】")
    print("  系统: {}".format(os_info['system']))
    print("  版本: {}".format(os_info['release']))
    print("  详细版本: {}".format(os_info['version']))
    print("  架构: {}".format(os_info['machine']))

    cpu_info = get_cpu_info()
    print("\n【CPU 信息】")
    print("  型号: {}".format(cpu_info.get('model', 'Unknown')))
    if 'architecture' in cpu_info:
        print("  架构: {}".format(cpu_info['architecture']))
    if 'cores' in cpu_info:
        print("  核心数: {}".format(cpu_info['cores']))

    mem_info = get_memory_info()
    print("\n【内存信息】")
    if 'total' in mem_info:
        print("  总计: {:.2f} GB".format(mem_info['total'] / (1024**3)))
    if 'available' in mem_info:
        print("  可用: {:.2f} GB".format(mem_info['available'] / (1024**3)))
    if 'free' in mem_info:
        print("  空闲: {:.2f} GB".format(mem_info['free'] / (1024**3)))
    if 'type' in mem_info:
        print("  类型: {}".format(mem_info['type']))

    disk_info = get_disk_info()
    print("\n【硬盘信息】")
    if disk_info:
        for i, disk in enumerate(disk_info, 1):
            print("  硬盘{}: {}".format(i, disk.get('model', 'Unknown')))
            if 'size' in disk and disk['size'] != 'Unknown':
                print("    大小: {}".format(disk['size']))
    else:
        print("  未检测到硬盘信息")

    print("\n" + "=" * 60)


if __name__ == '__main__':
    main()
