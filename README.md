# Universal Product Manager Skill

一个通用产品经理 Skill，用于帮助使用者从模糊需求出发，完成领域理解、需求拆解、产品方案设计、用户增长规划、数据库结构设计、DDD 分析、容器化部署评估、服务器管理方案、产品原型设计、自动化测试方案、项目归档与产品拆解图输出。

本项目适合用于：

- 产品经理工作流辅助
- AI 产品 / SaaS 产品 / 管理系统 / 工具类产品规划
- 创业项目从 0 到 1 设计
- 技术型产品经理方案设计
- 产品方案汇报与项目归档
- 产品拆解图、测试用例、日志模板自动生成

---

## 1. 项目定位

本 Skill 的目标是把一个模糊的产品想法，系统化转化为：

- 可理解的领域分析
- 可执行的需求拆解
- 可落地的产品方案
- 可验证的 MVP 计划
- 可增长的用户增长策略
- 可实现的数据库与技术架构
- 可维护的部署与服务器管理方案
- 可测试的自动化测试方案
- 可归档的项目文档体系
- 可视化的产品拆解图

---

## 2. 文件说明

推荐仓库结构如下：

```text
-skills/
├── README.md
├── UNIVERSAL_PRODUCT_MANAGER_SKILL.md
├── pm_skill_toolkit.py
├── product_brief_template.json
└── LICENSE
```

| 文件 | 作用 | 是否必需 |
|---|---|---|
| `README.md` | 仓库说明、使用顺序、脚本命令说明 | 必需 |
| `UNIVERSAL_PRODUCT_MANAGER_SKILL.md` | 通用产品经理 Skill 主文档，定义完整工作流 | 必需 |
| `pm_skill_toolkit.py` | 自动化辅助脚本，用于初始化项目、生成拆解图、校验文档、追加日志、生成测试用例 | 推荐 |
| `product_brief_template.json` | 产品信息输入模板，供自动化脚本读取 | 推荐 |
| `LICENSE` | 开源许可证，建议使用 MIT License | 推荐 |

---

## 3. 推荐使用顺序

建议按照下面顺序使用：

```text
1. 阅读 README.md，了解仓库用途和文件结构
2. 阅读 UNIVERSAL_PRODUCT_MANAGER_SKILL.md，了解 Skill 的完整工作流
3. 根据具体产品需求，让 Skill 输出完整产品方案
4. 将产品关键信息整理到 product_brief_template.json
5. 使用 pm_skill_toolkit.py 校验 JSON 模板
6. 使用 pm_skill_toolkit.py 生成产品拆解图
7. 使用 pm_skill_toolkit.py 初始化项目文档目录
8. 使用 pm_skill_toolkit.py 生成测试用例模板
9. 在项目推进过程中持续追加决策日志、问题日志和发布日志
10. 根据实际项目进展持续更新产品方案、MVP 范围和复盘文档
```

---

## 4. Skill 主文档

核心 Skill 文档为：

```text
UNIVERSAL_PRODUCT_MANAGER_SKILL.md
```

它覆盖以下完整流程：

1. 需求理解与领域识别
2. 领域知识补充
3. 需求拆解
4. 产品优化方案设计
5. 工作文件整理与日志归档方案
6. 用户增长方案设计
7. 数据库结构设计
8. DDD 领域驱动开发分析
9. 容器化部署方案评估
10. 服务器管理方案
11. 产品原型设计
12. 自动化测试方案
13. 风险分析
14. MVP 版本计划
15. 下一步行动清单
16. 产品拆解图输出

---

## 5. 自动化脚本能力

自动化脚本文件为：

```text
pm_skill_toolkit.py
```

支持以下能力：

| 命令 | 作用 |
|---|---|
| `init` | 初始化产品项目文档目录 |
| `validate-brief` | 校验产品信息 JSON 是否包含必要字段 |
| `breakdown` | 根据 JSON 生成产品拆解图 |
| `validate` | 校验产品方案 Markdown 是否包含关键章节 |
| `log` | 追加项目日志 |
| `testcase` | 根据功能模块生成测试用例模板 |

---

## 6. 使用前准备

本工具使用 Python 编写，不依赖第三方库。

推荐环境：

```text
Python 3.8+
```

查看 Python 版本：

```bash
python --version
```

或：

```bash
python3 --version
```

---

## 7. 快速开始

### 7.1 校验产品信息 JSON

在生成拆解图或测试用例前，建议先校验 JSON：

```bash
python pm_skill_toolkit.py validate-brief --input product_brief_template.json
```

如果字段缺失、字段类型错误或功能优先级不符合要求，脚本会给出错误提示。

---

### 7.2 初始化产品项目目录

```bash
python pm_skill_toolkit.py init --name my-product
```

执行后会生成类似结构：

```text
my-product/
├── README.md
├── 01-requirements/
├── 02-product-design/
├── 03-technical-design/
├── 04-growth/
├── 05-testing/
├── 06-operations/
└── 07-review/
```

---

### 7.3 生成树状产品拆解图

```bash
python pm_skill_toolkit.py breakdown --input product_brief_template.json --output product-breakdown-map.md --type tree
```

---

### 7.4 生成 Markdown 思维导图

```bash
python pm_skill_toolkit.py breakdown --input product_brief_template.json --output product-mindmap.md --type mindmap
```

---

### 7.5 生成 Mermaid 思维导图

```bash
python pm_skill_toolkit.py breakdown --input product_brief_template.json --output product-mermaid.md --type mermaid
```

Mermaid 版本适合复制到支持 Mermaid 的 Markdown 编辑器或文档系统中。

---

### 7.6 校验产品方案完整性

```bash
python pm_skill_toolkit.py validate --file product-solution.md
```

该命令会检查产品方案是否包含关键章节，例如需求理解、领域知识补充、需求拆解、产品定位、功能模块设计、用户增长方案、数据库结构设计、DDD、部署方案、测试方案、MVP 和产品拆解图等。

---

### 7.7 追加项目日志

追加决策日志：

```bash
python pm_skill_toolkit.py log --project my-product --type decision --message "确定 MVP 优先开发核心功能"
```

追加问题日志：

```bash
python pm_skill_toolkit.py log --project my-product --type issue --message "注册流程存在体验问题"
```

追加发布日志：

```bash
python pm_skill_toolkit.py log --project my-product --type release --message "发布 v0.1 MVP 测试版本"
```

---

### 7.8 生成测试用例模板

```bash
python pm_skill_toolkit.py testcase --input product_brief_template.json --output test-cases.md
```

生成内容包括：

- 用例编号
- 功能模块
- 测试场景
- 前置条件
- 操作步骤
- 预期结果
- 优先级

---

## 8. 产品信息 JSON 模板说明

产品信息模板文件为：

```text
product_brief_template.json
```

字段说明：

| 字段 | 类型 | 说明 |
|---|---|---|
| `product_name` | string | 产品名称 |
| `goals` | list[string] | 产品目标 |
| `target_users` | list[string] | 目标用户 |
| `scenarios` | list[string] | 核心使用场景 |
| `pain_points` | list[string] | 用户痛点 |
| `features` | list[object/string] | 功能模块，推荐使用对象形式 |
| `growth` | list[string] | 用户增长策略 |
| `technology` | list[string] | 数据、技术、部署相关内容 |
| `testing` | list[string] | 测试范围或测试场景 |
| `mvp` | list[string] | MVP 范围 |
| `risks` | list[string] | 风险点 |
| `next_steps` | list[string] | 下一步行动 |

推荐功能项格式：

```json
{
  "name": "AI 学习计划生成",
  "description": "根据目标生成阶段性学习计划",
  "priority": "P0"
}
```

其中 `priority` 建议使用：

```text
P0 / P1 / P2 / P3
```

---

## 9. 完整产品方案输出结构

当需要输出完整产品方案时，建议使用以下结构：

```text
产品方案报告
├── 1. 需求理解
├── 2. 领域知识补充
├── 3. 需求拆解
├── 4. 产品定位
├── 5. 功能模块设计
├── 6. 用户流程设计
├── 7. 产品原型设计
├── 8. 用户增长方案
├── 9. 数据库结构设计
├── 10. DDD 领域建模
├── 11. 容器化部署方案
├── 12. 服务器管理方案
├── 13. 自动化测试方案
├── 14. 文件整理与日志归档方案
├── 15. 风险分析
├── 16. MVP 版本计划
├── 17. 下一步行动清单
└── 18. 产品拆解图
```

---

## 10. 产品拆解图要求

完整产品方案最后必须输出产品拆解图。

支持形式：

- 树状图
- Markdown 思维导图
- Mermaid mindmap

产品拆解图应包含：

- 产品名称
- 产品目标
- 目标用户
- 核心场景
- 用户痛点
- 产品价值
- 功能模块
- 用户增长方案
- 数据库结构
- DDD 领域模型
- 部署与服务器管理方案
- 原型设计范围
- 自动化测试方案
- MVP 范围
- 风险分析
- 下一步行动计划

---

## 11. 适用人群

本项目适合：

- 产品经理
- AI 产品经理
- 技术型产品经理
- 创业者
- 独立开发者
- 软件工程学习者
- 项目负责人
- 需要系统化整理产品方案的人

---

## 12. 示例使用场景

```text
我想做一个面向大学生的 AI 学习助手，帮我设计完整产品方案。
```

```text
我想做一个企业内部知识库系统，帮我拆解需求并设计 MVP。
```

```text
我想优化一个在线课程平台，帮我设计产品优化方案和用户增长方案。
```

```text
我想做一个 SaaS 管理后台，帮我设计数据库结构、DDD 模型和部署方案。
```

---

## 13. 许可证

建议使用 MIT License。

---

## 14. 项目目标

本项目希望提供一套通用、结构化、可执行的产品经理工作流，让产品设计不再停留在想法层面，而是进一步进入：

```text
需求理解 → 产品设计 → 技术评估 → 原型设计 → 测试验证 → 上线部署 → 用户增长 → 持续迭代
```

最终形成完整的产品管理闭环。
