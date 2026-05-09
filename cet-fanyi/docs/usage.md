# `/cet-fanyi` CLI 使用文档
CET四六级翻译辅助命令行工具，支持翻译解析、技巧查询和知识归档。
## 语法
```bash
/cet-fanyi [command] [query]
```
- 若省略 `command`，默认执行 `translate` 命令。
- `query` 为紧跟命令后的附加文本。
## 命令列表
| 命令 | 说明 | 示例 |
|---|---|---|
| `translate` | 翻译四六级段落，输出译文及逐句讲解（**默认命令**） | `/cet-fanyi 丝绸之路促进了东西方贸易` |
| `xy-tips` | 提供上位词、高级词汇替换及翻译技巧；若省略 `query`，则使用上下文中最近一次翻译的原文 | `/cet-fanyi xy-tips 经济类翻译技巧` |
| `archive` | 将当前会话上下文及文档归档至本地知识库（KBase），默认目录为根目录下 `/KBase` | `/cet-fanyi archive 把词汇存进去` |
| `help` | 查看使用帮助 | `/cet-fanyi help` |
## 使用示例
**1. 翻译（默认）**
直接输入需要翻译的内容，无需指定命令：
```bash
/cet-fanyi 丝绸之路促进了东西方贸易
# 等同于 /cet-fanyi translate 丝绸之路促进了东西方贸易
```
**2. 查询翻译技巧**
```bash
/cet-fanyi xy-tips 经济类常用上位词
```
**3. 归档知识**
```bash
/cet-fanyi archive 保存本次会话的高频词汇
```
**4. 查看帮助**
```bash
/cet-fanyi help
```
## 输出格式
命令解析后统一输出 JSON：
```json
{
  "command": "translate | xy-tips | archive | help",
  "query": "附加文本"
}
```
**异常处理**：若输入非 `/cet-fanyi` 前缀，则返回：
```json
{
  "error": "不是 /cet-fanyi 命令"
}
```
