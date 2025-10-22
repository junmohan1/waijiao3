import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.app import dedupe_header, add_numbers

def test_dedupe_header():
    """测试表头去重功能"""
    # 测试唯一列名
    assert dedupe_header(["id", "name", "age"]) == ["id", "name", "age"]
    
    # 测试重复列名
    assert dedupe_header(["id", "id", "id"]) == ["id", "id.1", "id.2"]
    
    # 测试混合列名
    cols = ["id", "name", "id", "name", "name"]
    expected = ["id", "name", "id.1", "name.1", "name.2"]
    assert dedupe_header(cols) == expected
    
    # 测试空列表
    assert dedupe_header([]) == []
    
    # 测试单列
    assert dedupe_header(["id"]) == ["id"]
    
    # 测试复杂重复
    cols = ["a", "b", "a", "c", "b", "a", "d"]
    expected = ["a", "b", "a.1", "c", "b.1", "a.2", "d"]
    assert dedupe_header(cols) == expected
    
    # 测试特殊字符
    assert dedupe_header(["col-1", "col-1", "col_2"]) == ["col-1", "col-1.1", "col_2"]

def test_add_numbers():
    """测试加法功能"""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(10, -5) == 5