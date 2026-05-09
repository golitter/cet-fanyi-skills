<div align="center">

# 四六级翻译练习.SKILL

> *「先保证意思对、语法对、写得完，再追求词更准、句更漂亮。」*

<br>

CET 四六级翻译练习技能，通过 `/cet-fanyi` 命令触发。<br>
提供段落翻译逐句解析、应试技巧查询和知识归档，<br>
内置"提取主干 → 翻译主干 → 补充修饰 → 通读润色"四步翻译法，<br>
以及提炼自刘晓燕老师课堂的三条救命策略——上位词替代、释义描述、跳过小词，不会的词也能拿分。

[使用方法](#使用方法) · [安装](#安装) · [参考](#参考)

</div>

---

## 使用方法

在Claude Code等aicoding工具中输入：
```bash
/cet-fanyi [command] [query]
```

| 命令 | 说明 | 示例 |
|---|---|---|
| `translate` | 翻译段落，输出译文及逐句讲解（**默认命令**） | `/cet-fanyi 丝绸之路促进了东西方贸易` |
| `xy-tips` | 标注难点词，给出上位词替换和释义方案 | `/cet-fanyi xy-tips 剪纸是传统民间艺术` |
| `archive` | 将会话中的词汇、句型、技巧归档到知识库 | `/cet-fanyi archive 保存本次的高频词汇` |
| `help` | 查看使用帮助 | `/cet-fanyi help` |

使用`/cet-fanyi help` 或者 查看`/skills/cet-fanyi/docs/usage.md`文档。

---

## 安装

将 `cet-fanyi` 目录放到 Claude Code 等 aicoding 的 skills 目录下：

```bash
~/.claude(xxx)/skills/cet-fanyi
```

在对话中输入 `/cet-fanyi help` 即可开始使用。

---

## 参考
1. https://www.bilibili.com/video/BV1Gw4m1X7db/
2. https://www.zhihu.com/question/280581372/answer/2521870747
