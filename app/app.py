from collections import defaultdict
from typing import List

def dedupe_header(columns: List[str]) -> List[str]:
    """
    处理重复的表头名称，为重复的表头添加数字后缀
    例如: ['id', 'id', 'id'] → ['id', 'id.1', 'id.2']
    """
    seen_counts = defaultdict(int)
    result: List[str] = []

    for col in columns:
        count = seen_counts[col]
        if count == 0:
            result.append(col)
        else:
            result.append(f"{col}.{count}")
        seen_counts[col] += 1

    return result

def add_numbers(a, b):
    """
    新增功能：两个数字相加
    """
    return a + b

if __name__ == "__main__":
    # 测试表头去重功能
    sample_headers = ["id", "name", "id", "name", "name"]
    print(f"原始表头: {sample_headers}")
    print(f"去重后表头: {dedupe_header(sample_headers)}")
    
    # 测试加法功能
    print(f"2 + 3 = {add_numbers(2, 3)}")