---
name: cet-fanyi
description: 英语四六级翻译练习技能。通过 `/cet-fanyi` 触发，支持翻译解析、技巧查询和知识归档。
---

# cet-fanyi 技能文档

## Usage

```
/cet-fanyi [command] [query]
```

- `command`：translate / xy-tips / archive / help（省略时默认 translate）
- `query`：命令后的自由文本

完整文档见 `docs/usage.md`。

## Trigger

仅在用户发送 `/cet-fanyi` 开头的消息时触发。不响应自然语言。

## Workflow

### Step 1：解析命令

用户输入 `/cet-fanyi ...` 后，运行解析脚本提取 command 和 query：

```bash
python3 skills/cet-fanyi/scripts/parse.py "<用户输入的完整字符串>"
```

脚本输出 JSON：
```json
{
    "command": "translate|xy-tips|archive|help",
    "query": "附加文本"
}
```

根据解析结果路由到对应的 sub-skill：

```
command
  ├── translate → sub-skills/translate.md
  ├── xy-tips   → sub-skills/xy-tips.md
  ├── archive   → sub-skills/archive.md
  └── help      → 读取并展示 docs/usage.md
```

## Rules

1. 仅在 `/cet-fanyi` 命令时触发，不响应自然语言

## Directory Convention

```
KBase/                          ← 项目根目录下的知识库
├── technique.md                ← 翻译技巧速查（≤10条，≤1000字符）
├── 001/                        ← 归档单元
└── ...

.claude(codex等)/skills/cet-fanyi/
├── SKILL.md                    ← 主 skill 文档（本文件）
├── docs/
│   └── usage.md                ← CLI 使用手册
├── scripts/
│   ├── parse.py                ← CLI 参数解析脚本
│   └── kbase.py                ← KBase technique.md 管理脚本
├── sub-skills/
│   ├── translate.md            ← 翻译解析流程规范
│   ├── xy-tips.md              ← 技巧查询流程规范
│   └── archive.md              ← 知识归档流程规范
└── reference/
    ├── translate.md            ← 翻译解析示例
    └── xy-tips.md              ← 应试技巧示例
```
