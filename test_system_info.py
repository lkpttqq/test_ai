#!/usr/bin/env python3
"""测试系统信息获取程序"""

import subprocess
import sys


def test_system_info_module():
    from system_info import get_os_info, get_cpu_info, get_memory_info, get_disk_info

    os_info = get_os_info()
    assert 'system' in os_info
    assert os_info['system'] == 'Linux'

    cpu_info = get_cpu_info()
    assert 'model' in cpu_info
    assert len(cpu_info['model']) > 0

    mem_info = get_memory_info()
    assert 'total' in mem_info
    assert mem_info['total'] > 0

    disk_info = get_disk_info()
    assert isinstance(disk_info, list)

    return True


def test_main():
    result = subprocess.run([sys.executable, 'system_info.py'], capture_output=True, text=True)
    assert result.returncode == 0
    assert '系统硬件信息' in result.stdout
    assert 'CPU' in result.stdout
    assert '内存' in result.stdout
    return True


if __name__ == '__main__':
    test_system_info_module()
    test_main()
    print("所有测试通过!")
