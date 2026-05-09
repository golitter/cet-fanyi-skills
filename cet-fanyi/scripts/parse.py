#!/usr/bin/env python3
"""CET-翻译 CLI parser - 解析 /cet-fanyi 命令参数。

用法:
    python parse.py "/cet-fanyi translate 丝绸之路促进了东西方贸易"
    python parse.py "/cet-fanyi xy-tips 经济类翻译技巧"
    python parse.py "/cet-fanyi archive 把词汇存进去"
    python parse.py "/cet-fanyi help"
    python parse.py "/cet-fanyi 丝绸之路促进了东西方贸易"

输出 JSON:
    {"command": "translate|xy-tips|archive|help", "query": "附加文本"}
"""

import json
import sys

PREFIX = "/cet-fanyi"
VALID_COMMANDS = {"translate", "xy-tips", "archive", "help"}


def parse(input_str: str) -> dict:
    text = input_str.strip()

    if not text.startswith(PREFIX):
        return {"error": "不是 /cet-fanyi 命令"}

    text = text[len(PREFIX):].strip()

    if not text:
        return {"command": "translate", "query": ""}

    tokens = text.split(None, 1)
    first = tokens[0]
    rest = tokens[1] if len(tokens) > 1 else ""

    if first in VALID_COMMANDS:
        return {"command": first, "query": rest.strip()}

    return {"command": "translate", "query": text}


def main():
    if len(sys.argv) < 2:
        print("用法: python parse.py '<cet-fanyi 命令字符串>'")
        sys.exit(1)

    result = parse(" ".join(sys.argv[1:]))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
