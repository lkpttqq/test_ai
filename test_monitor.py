#!/usr/bin/env python3
"""测试资源监控程序"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from monitor import get_cpu_usage, get_memory_usage, get_disk_usage, get_network_usage


def test_cpu():
    cpu = get_cpu_usage()
    assert isinstance(cpu, float), "CPU should return float"
    assert 0 <= cpu <= 100, "CPU percentage should be 0-100"
    print(f"CPU test passed: {cpu}%")


def test_memory():
    mem = get_memory_usage()
    assert isinstance(mem, dict), "Memory should return dict"
    assert 'total' in mem and 'used' in mem and 'percent' in mem
    assert mem['percent'] >= 0 and mem['percent'] <= 100
    print(f"Memory test passed: {mem['percent']}%")


def test_disk():
    disk = get_disk_usage()
    assert isinstance(disk, dict), "Disk should return dict"
    assert 'total' in disk and 'used' in disk and 'percent' in disk
    assert disk['percent'] >= 0 and disk['percent'] <= 100
    print(f"Disk test passed: {disk['percent']}%")


def test_network():
    net = get_network_usage()
    assert isinstance(net, dict), "Network should return dict"
    assert 'bytes_sent' in net and 'bytes_recv' in net
    print(f"Network test passed: sent={net['bytes_sent']}, recv={net['bytes_recv']}")


if __name__ == '__main__':
    test_cpu()
    test_memory()
    test_disk()
    test_network()
    print("\nAll tests passed!")