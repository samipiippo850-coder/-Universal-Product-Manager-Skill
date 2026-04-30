# Universal Product Manager Skill

版本：v2.1 Beginner + SOP Governance Edition  
中文名：通用产品经理新手与大厂交付 SOP Governance Skill

本 Skill 同时支持**新手模式**与 **SOP 模式**。新手默认使用标准版，先学习产品主线；当需要团队协作、项目落地或大厂流程时，再启用完整 SOP 模式。

这是一个面向**没有当过产品经理的人**的产品工作流 Skill。它既能帮助新手从模糊想法开始设计产品，也能进一步补齐互联网团队常用的 SOP 能力，包括标准化流程、组织协作、评审机制、指标口径、质量门禁、上线审批、合规风险和 RACI 责任矩阵。

---

## 1. 项目定位

本项目不是单纯的 PRD 模板，而是一套：

```text
产品经理新手学习框架
+ 通用产品方案生成流程
+ 技术型产品交付辅助
+ 大厂产品 SOP 治理模板
+ 自动化文档生成脚本
```

它适合：

- 没有产品经理经验，但想系统学习产品工作流的人
- 想把一个想法整理成产品方案的人
- 想做 AI 产品、SaaS 产品、工具类产品、管理后台或数据平台的人
- 想学习互联网团队如何做需求评审、上线审批、质量门禁和复盘的人
- 独立开发者、创业者、学生、技术转产品的人

---

## 2. 核心能力

```text
Universal Product Manager Skill
├── 新手引导
├── 产品经理术语解释
├── 需求理解
├── 领域知识补充
├── 用户研究
├── 竞品分析
├── 需求拆解
├── 产品定位
├── 功能模块设计
├── MVP 版本计划
├── 用户流程与原型设计
├── 用户增长方案
├── 指标体系
├── 实验设计
├── 数据库结构设计
├── DDD 领域建模
├── 容器化部署与服务器管理
├── 测试与验收
├── 发布检查清单
├── 标准化流程
├── 组织协作
├── 评审机制
├── RACI 责任矩阵
├── 指标口径与埋点规范
├── 质量门禁
├── 阶段准入 / 准出标准
├── 上线审批
├── 合规风险检查
├── 工作文件整理与日志归档
└── 产品拆解图输出
```

---

## 3. 默认输出规则

默认输出**标准版**，避免新手一开始被过重内容淹没。

只有当使用者明确要求以下内容时，才输出完整版或 SOP 增强版：

- 完整方案
- 落地方案
- 技术方案
- 项目交付方案
- 大厂 SOP
- 上线审批
- 评审流程
- 质量门禁
- RACI 责任矩阵

### 3.1 双模式说明

本 Skill 同时支持**新手模式**与 **SOP 模式**。

| 模式 | 适用对象 | 默认输出 | 适合场景 |
|---|---|---|---|
| 新手模式 | 没有产品经理经验的人 | 标准版 | 学习产品主线、完成产品方案初稿 |
| SOP 模式 | 团队协作或项目落地场景 | 完整 SOP 增强版 | 需求评审、质量门禁、上线审批、指标口径和 RACI 协作 |

新手默认使用标准版，先学习产品主线；当需要团队协作、项目落地或大厂流程时，再启用完整 SOP 模式。

---

## 4. 推荐仓库结构

```text
-skills/
├── README.md
├── UNIVERSAL_PRODUCT_MANAGER_SKILL.md
├── pm_skill_toolkit.py
├── product_brief_template.json
└── LICENSE
```

---

## 5. 文件说明

| 文件 | 说明 |
|---|---|
| `README.md` | 项目说明文档 |
| `UNIVERSAL_PRODUCT_MANAGER_SKILL.md` | Skill 主文档 |
| `pm_skill_toolkit.py` | 自动化辅助脚本 |
| `product_brief_template.json` | 产品信息输入模板 |
| `LICENSE` | 开源许可证 |

---

## 6. 自动化脚本

脚本名称：

```text
pm_skill_toolkit.py
```

推荐环境：

```text
Python 3.8+
```

该脚本不依赖第三方库。

### 6.1 初始化产品项目目录

```bash
python pm_skill_toolkit.py init --name my-product
```

### 6.2 校验产品信息模板

```bash
python pm_skill_toolkit.py validate-brief --input product_brief_template.json
```

### 6.3 生成产品拆解图

```bash
python pm_skill_toolkit.py breakdown --input product_brief_template.json --output product-breakdown-map.md --type tree
```

可选类型：

```text
tree
mindmap
mermaid
```

### 6.4 生成测试用例

```bash
python pm_skill_toolkit.py testcase --input product_brief_template.json --output test-cases.md
```

### 6.5 生成发布检查清单

```bash
python pm_skill_toolkit.py release-checklist --input product_brief_template.json --output release-checklist.md
```

### 6.6 生成新手引导文档

```bash
python pm_skill_toolkit.py beginner-guide --output beginner-guide.md
```

### 6.7 生成产品经理术语表

```bash
python pm_skill_toolkit.py glossary --output pm-glossary.md
```

### 6.8 生成 RACI 责任矩阵

```bash
python pm_skill_toolkit.py raci --input product_brief_template.json --output raci-matrix.md
```

### 6.9 生成大厂 SOP 检查清单

```bash
python pm_skill_toolkit.py sop-checklist --input product_brief_template.json --output sop-checklist.md
```

### 6.10 生成指标口径表

指标口径表包含：指标名称、业务定义、计算公式、数据来源、更新频率、负责人、适用范围、异常处理和看板位置。

```bash
python pm_skill_toolkit.py metric-dictionary --input product_brief_template.json --output metric-dictionary.md
```


### 6.11 生成阶段准入 / 准出标准表

```bash
python pm_skill_toolkit.py phase-gates --input product_brief_template.json --output phase-gates.md
```

### 6.12 追加项目日志

```bash
python pm_skill_toolkit.py log --project my-product --type decision --message "确认 MVP 范围"
```

支持日志类型：

```text
decision
issue
release
learning
```

---

## 7. 产品信息模板

模板文件：

```text
product_brief_template.json
```

v2.0 主要字段：

| 字段 | 说明 |
|---|---|
| `product_name` | 产品名称 |
| `experience_level` | 使用者经验水平 |
| `preferred_output_depth` | 期望输出深度 |
| `learning_goals` | 学习目标 |
| `goals` | 产品目标 |
| `target_users` | 目标用户 |
| `scenarios` | 使用场景 |
| `pain_points` | 用户痛点 |
| `features` | 功能模块 |
| `competitors` | 竞品分析 |
| `user_research` | 用户研究计划 |
| `growth` | 用户增长方案 |
| `metrics` | 指标体系 |
| `experiments` | 实验设计 |
| `technology` | 技术与数据设计 |
| `testing` | 测试方案 |
| `mvp` | MVP 范围 |
| `risks` | 风险分析 |
| `release_checklist` | 发布检查清单 |
| `standardized_process` | 标准化流程 |
| `collaboration` | 组织协作 |
| `reviews` | 评审机制 |
| `metric_definitions` | 指标口径，包含业务定义、公式、来源、频率、负责人、适用范围、异常处理和看板位置 |
| `quality_gates` | 质量门禁 |
| `phase_gate_standards` | 阶段准入 / 准出标准，包含输入物、输出物、负责人、评审人、准入条件、准出条件和归档位置 |
| `launch_approval` | 上线审批 |
| `compliance_risks` | 合规风险 |
| `raci` | RACI 责任矩阵 |
| `next_steps` | 下一步行动 |

---

## 8. 推荐使用流程

```text
1. 用自然语言描述产品想法
2. 使用 Skill 输出标准版产品方案
3. 根据方案补充 product_brief_template.json
4. 使用脚本生成产品拆解图
5. 使用脚本生成测试用例和发布检查清单
6. 如果要模拟大厂 SOP，生成 RACI、SOP 检查清单、阶段准入 / 准出标准和指标口径表
7. 进入评审、开发、测试、上线和复盘
```

---

## 9. 示例需求

```text
我想做一个面向大学生的 AI 学习助手，帮我设计产品方案。
```

默认输出标准版。

```text
我想做一个面向大学生的 AI 学习助手，帮我设计完整落地方案，包括数据库、部署、测试、上线审批和大厂 SOP。
```

输出完整版 / SOP 增强版。

---

## 10. 项目目标

本项目希望帮助没有产品经理经验的人，从 0 开始掌握：

```text
需求理解 → 用户研究 → 竞品分析 → 需求拆解 → 产品设计 → MVP 验证
→ 指标体系 → 技术沟通 → 测试验收 → 上线审批 → SOP 治理 → 复盘迭代
```

最终使用户不仅能写出产品方案，还能理解一个产品如何在真实团队中被评审、开发、测试、上线和复盘。
