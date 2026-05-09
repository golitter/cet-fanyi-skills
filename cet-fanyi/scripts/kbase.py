#!/usr/bin/env python3
"""KBase technique.md 管理脚本。

维护一个最多 10 条、总字符不超过 1000 的技巧列表。

用法:
    python kbase.py list                          # 列出所有技巧
    python kbase.py add "技巧内容"                # 添加一条技巧（超限时报错）
    python kbase.py remove <编号>                 # 按编号删除一条技巧
    python kbase.py check "技巧内容"              # 检查是否可以添加（不实际写入）

输出 JSON。
"""

import json
import os
import sys

MAX_COUNT = 10
MAX_CHARS = 1000

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# KBase 在项目根目录，与 .claude/ 平级
# scripts/ → cet-fanyi/ → skills/ → .claude/ → 项目根
KBASE_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "..", "..", "..", "KBase"))
TECHNIQUE_FILE = os.path.join(KBASE_DIR, "technique.md")


def _ensure_file():
    os.makedirs(KBASE_DIR, exist_ok=True)
    if not os.path.exists(TECHNIQUE_FILE):
        with open(TECHNIQUE_FILE, "w", encoding="utf-8") as f:
            f.write("# 翻译技巧速查\n\n")


def _read_techniques():
    _ensure_file()
    with open(TECHNIQUE_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    techniques = []
    for line in lines:
        line = line.strip()
        if line and line[0].isdigit() and ". " in line:
            techniques.append(line.split(". ", 1)[1])
    return techniques


def _write_techniques(techniques):
    _ensure_file()
    with open(TECHNIQUE_FILE, "w", encoding="utf-8") as f:
        f.write("# 翻译技巧速查\n\n")
        for i, t in enumerate(techniques, 1):
            f.write(f"{i}. {t}\n")


def _total_chars(techniques):
    return sum(len(t) for t in techniques)


def list_techniques():
    techniques = _read_techniques()
    total = _total_chars(techniques)
    return {
        "count": len(techniques),
        "max_count": MAX_COUNT,
        "total_chars": total,
        "max_chars": MAX_CHARS,
        "techniques": techniques,
    }


def add_technique(text):
    techniques = _read_techniques()
    text = text.strip()
    if not text:
        return {"error": "技巧内容不能为空"}
    if len(techniques) >= MAX_COUNT:
        return {"error": f"已达上限 {MAX_COUNT} 条，请先删除旧技巧"}
    new_total = _total_chars(techniques) + len(text)
    if new_total > MAX_CHARS:
        remaining = MAX_CHARS - _total_chars(techniques)
        return {"error": f"字符超限：剩余 {remaining} 字符，当前内容 {len(text)} 字符"}
    techniques.append(text)
    _write_techniques(techniques)
    return {
        "ok": True,
        "index": len(techniques),
        "total_chars": _total_chars(techniques),
        "remaining_slots": MAX_COUNT - len(techniques),
        "remaining_chars": MAX_CHARS - _total_chars(techniques),
    }


def remove_technique(index_str):
    techniques = _read_techniques()
    try:
        index = int(index_str)
    except ValueError:
        return {"error": f"无效编号：{index_str}"}
    if index < 1 or index > len(techniques):
        return {"error": f"编号超出范围：1-{len(techniques)}"}
    removed = techniques.pop(index - 1)
    _write_techniques(techniques)
    return {
        "ok": True,
        "removed": removed,
        "count": len(techniques),
        "total_chars": _total_chars(techniques),
    }


def check_technique(text):
    techniques = _read_techniques()
    text = text.strip()
    new_total = _total_chars(techniques) + len(text)
    can_add = len(techniques) < MAX_COUNT and new_total <= MAX_CHARS
    return {
        "can_add": can_add,
        "text_chars": len(text),
        "current_count": len(techniques),
        "current_total_chars": _total_chars(techniques),
        "remaining_slots": max(0, MAX_COUNT - len(techniques)),
        "remaining_chars": max(0, MAX_CHARS - _total_chars(techniques)),
    }


def main():
    if len(sys.argv) < 2:
        print("用法: python kbase.py <list|add|remove|check> [args...]")
        sys.exit(1)

    action = sys.argv[1]

    if action == "list":
        result = list_techniques()
    elif action == "add":
        if len(sys.argv) < 3:
            result = {"error": "请提供技巧内容"}
        else:
            result = add_technique(" ".join(sys.argv[2:]))
    elif action == "remove":
        if len(sys.argv) < 3:
            result = {"error": "请提供要删除的编号"}
        else:
            result = remove_technique(sys.argv[2])
    elif action == "check":
        if len(sys.argv) < 3:
            result = {"error": "请提供要检查的内容"}
        else:
            result = check_technique(" ".join(sys.argv[2:]))
    else:
        result = {"error": f"未知操作：{action}"}

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
