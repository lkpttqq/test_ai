#!/usr/bin/env python3
"""资源监控程序 - 获取本机 CPU、内存、磁盘、网络使用信息"""

import psutil
import time


def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    mem = psutil.virtual_memory()
    return {
        'total': mem.total,
        'available': mem.available,
        'percent': mem.percent,
        'used': mem.used
    }

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return {
        'total': disk.total,
        'used': disk.used,
        'free': disk.free,
        'percent': disk.percent
    }

def get_network_usage():
    net = psutil.net_io_counters()
    return {
        'bytes_sent': net.bytes_sent,
        'bytes_recv': net.bytes_recv,
        'packets_sent': net.packets_sent,
        'packets_recv': net.packets_recv
    }

def main():
    print("=" * 50)
    print("系统资源监控信息")
    print("=" * 50)

    print("\nCPU 使用率: {}%".format(get_cpu_usage()))

    mem = get_memory_usage()
    print("\n内存使用情况:")
    print("  总计: {:.2f} GB".format(mem['total'] / (1024**3)))
    print("  已使用: {:.2f} GB".format(mem['used'] / (1024**3)))
    print("  可用: {:.2f} GB".format(mem['available'] / (1024**3)))
    print("  使用率: {}%".format(mem['percent']))

    disk = get_disk_usage()
    print("\n磁盘使用情况:")
    print("  总计: {:.2f} GB".format(disk['total'] / (1024**3)))
    print("  已使用: {:.2f} GB".format(disk['used'] / (1024**3)))
    print("  可用: {:.2f} GB".format(disk['free'] / (1024**3)))
    print("  使用率: {}%".format(disk['percent']))

    net = get_network_usage()
    print("\n网络使用情况:")
    print("  发送字节: {}".format(net['bytes_sent']))
    print("  接收字节: {}".format(net['bytes_recv']))
    print("  发送数据包: {}".format(net['packets_sent']))
    print("  接收数据包: {}".format(net['packets_recv']))

    print("\n" + "=" * 50)

if __name__ == '__main__':
    main()