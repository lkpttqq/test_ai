#!/usr/bin/env python3
"""测试文件列表功能"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from list_files import list_files


def test_list_files():
    files = list_files('.')
    assert isinstance(files, list), "Should return a list"
    assert len(files) > 0, "Should have at least some files"
    for f in files:
        assert 'name' in f, "Each item should have 'name'"
        assert 'type' in f, "Each item should have 'type'"
        assert f['type'] in ('file', 'directory'), "Type should be file or directory"
    print(f"Test passed! Found {len(files)} items")
    for f in files[:5]:
        print(f"  {f['name']} ({f['type']})")


if __name__ == '__main__':
    test_list_files()