#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Universal Product Manager Skill Toolkit v2.1

用途：
1. 初始化产品项目文档目录
2. 生成产品方案基础模板
3. 生成产品拆解图
4. 校验产品报告完整性
5. 校验产品信息 JSON 模板
6. 追加项目日志
7. 根据功能模块生成测试用例模板
8. 生成发布检查清单
9. 生成新手引导文档
10. 生成产品经理术语表
11. 生成 RACI 责任矩阵
12. 生成大厂 SOP 检查清单
13. 生成指标口径表
14. 生成阶段准入 / 准出标准表

本脚本不依赖第三方库，Python 3.8+ 可直接运行。
"""

import argparse
import json
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, List


REQUIRED_SECTIONS = [
    "需求理解",
    "领域知识补充",
    "用户研究",
    "竞品分析",
    "需求拆解",
    "产品定位",
    "功能模块设计",
    "MVP",
    "用户增长方案",
    "指标体系",
    "测试",
    "风险分析",
    "下一步行动",
    "产品拆解图",
]

COMPLETE_SECTIONS = REQUIRED_SECTIONS + [
    "实验设计",
    "数据库结构设计",
    "DDD",
    "容器化部署方案",
    "服务器管理方案",
    "自动化测试方案",
    "文件整理",
    "发布检查清单",
    "标准化流程",
    "组织协作",
    "RACI",
    "指标口径",
    "质量门禁",
    "上线审批",
    "合规风险",
]

REQUIRED_BRIEF_KEYS = [
    "product_name",
    "experience_level",
    "preferred_output_depth",
    "learning_goals",
    "goals",
    "target_users",
    "scenarios",
    "pain_points",
    "features",
    "competitors",
    "user_research",
    "growth",
    "metrics",
    "experiments",
    "technology",
    "testing",
    "mvp",
    "risks",
    "release_checklist",
    "standardized_process",
    "collaboration",
    "reviews",
    "metric_definitions",
    "quality_gates",
    "phase_gate_standards",
    "launch_approval",
    "compliance_risks",
    "raci",
    "next_steps",
]

LIST_KEYS = [
    "learning_goals",
    "goals",
    "target_users",
    "scenarios",
    "pain_points",
    "features",
    "competitors",
    "user_research",
    "growth",
    "metrics",
    "experiments",
    "technology",
    "testing",
    "mvp",
    "risks",
    "release_checklist",
    "standardized_process",
    "collaboration",
    "reviews",
    "metric_definitions",
    "quality_gates",
    "phase_gate_standards",
    "launch_approval",
    "compliance_risks",
    "raci",
    "next_steps",
]

DEFAULT_PROJECT_DIRS = [
    "01-requirements",
    "02-product-design",
    "03-user-research",
    "04-competitive-analysis",
    "05-growth-and-metrics",
    "06-technical-design",
    "07-testing",
    "08-operations",
    "09-review",
    "10-learning-notes",
    "11-sop-governance",
]

DEFAULT_FILES = {
    "01-requirements/user-requirements.md": "# 用户需求文档\n\n## 目标用户\n\n## 用户痛点\n\n## 用户场景\n\n## 用户需求列表\n",
    "01-requirements/business-requirements.md": "# 业务需求文档\n\n## 业务目标\n\n## 核心指标\n\n## 商业模式\n\n## 业务约束\n",
    "01-requirements/product-requirements.md": "# 产品需求文档 PRD\n\n## 产品背景\n\n## 产品目标\n\n## 功能需求\n\n## 非功能需求\n\n## 验收标准\n",
    "02-product-design/product-solution.md": "# 产品方案报告\n\n## 1. 需求理解\n\n## 2. 领域知识补充\n\n## 3. 用户研究\n\n## 4. 竞品分析\n\n## 5. 需求拆解\n\n## 6. 产品定位\n\n## 7. 功能模块设计\n\n## 8. MVP 版本计划\n\n## 9. 用户流程与原型设计\n\n## 10. 用户增长方案\n\n## 11. 指标体系\n\n## 12. 测试与验收方案\n\n## 13. 风险分析\n\n## 14. 下一步行动清单\n\n## 15. 产品拆解图\n",
    "02-product-design/user-flow.md": "# 用户流程设计\n\n## 核心用户流程\n\n## 异常流程\n\n## 权限差异\n",
    "02-product-design/information-architecture.md": "# 信息架构\n\n## 页面结构\n\n## 导航结构\n\n## 数据结构关系\n",
    "02-product-design/product-breakdown-map.md": "# 产品拆解图\n\n",
    "03-user-research/user-interview.md": "# 用户访谈\n\n## 访谈目标\n\n## 访谈对象\n\n## 访谈问题\n\n## 结论\n",
    "03-user-research/user-persona.md": "# 用户画像\n\n## 用户类型\n\n## 目标\n\n## 痛点\n\n## 使用场景\n",
    "04-competitive-analysis/competitor-analysis.md": "# 竞品分析\n\n## 竞品列表\n\n## 功能对比\n\n## 差异化机会\n",
    "05-growth-and-metrics/growth-strategy.md": "# 用户增长方案\n\n## 获客\n\n## 激活\n\n## 留存\n\n## 转化\n",
    "05-growth-and-metrics/metrics-dashboard.md": "# 指标体系\n\n## 北极星指标\n\n## 输入指标\n\n## 过程指标\n\n## 结果指标\n",
    "05-growth-and-metrics/experiment-plan.md": "# 实验设计\n\n## 实验假设\n\n## 对照组\n\n## 实验组\n\n## 成功标准\n",
    "06-technical-design/database-design.md": "# 数据库结构设计\n\n## 核心实体\n\n## 数据表设计\n\n## 索引设计\n\n## 数据安全\n",
    "06-technical-design/domain-model.md": "# DDD 领域模型\n\n## 核心领域\n\n## 子领域\n\n## 限界上下文\n\n## 聚合根\n\n## 领域事件\n",
    "06-technical-design/deployment-plan.md": "# 部署方案\n\n## 本地开发\n\n## 测试环境\n\n## 生产环境\n\n## 回滚方案\n",
    "07-testing/test-plan.md": "# 测试计划\n\n## 测试目标\n\n## 测试范围\n\n## 测试类型\n\n## 验收标准\n",
    "07-testing/test-cases.md": "# 测试用例\n\n",
    "07-testing/bug-log.md": "# Bug 记录\n\n| 日期 | 问题 | 影响范围 | 优先级 | 状态 |\n|---|---|---|---|---|\n",
    "08-operations/server-management.md": "# 服务器管理方案\n\n## 服务器配置\n\n## 安全配置\n\n## 监控方案\n\n## 备份方案\n",
    "08-operations/release-checklist.md": "# 发布检查清单\n\n",
    "08-operations/release-log.md": "# 发布日志\n\n| 版本 | 日期 | 内容 | 风险 | 状态 |\n|---|---|---|---|---|\n",
    "08-operations/incident-log.md": "# 故障记录\n\n| 时间 | 故障 | 影响 | 原因 | 处理方案 | 状态 |\n|---|---|---|---|---|---|\n",
    "09-review/weekly-review.md": "# 周复盘\n\n## 本周完成\n\n## 遇到问题\n\n## 下周计划\n",
    "09-review/project-retrospective.md": "# 项目复盘\n\n## 项目目标\n\n## 实际结果\n\n## 经验总结\n\n## 后续优化\n",
    "10-learning-notes/beginner-guide.md": "# 产品经理新手引导\n\n## 先理解问题\n\n## 再拆解需求\n\n## 再设计 MVP\n\n## 最后验证和迭代\n",
    "11-sop-governance/standardized-process.md": "# 标准化流程\n\n## 需求准入\n\n## 评审流程\n\n## 开发测试\n\n## 上线复盘\n",
    "11-sop-governance/raci-matrix.md": "# RACI 责任矩阵\n\n| 事项 | R 负责执行 | A 最终负责 | C 协作咨询 | I 知会 |\n|---|---|---|---|---|\n",
    "11-sop-governance/review-process.md": "# 评审机制\n\n## 需求评审\n\n## 产品评审\n\n## 技术评审\n\n## 上线评审\n",
    "11-sop-governance/metric-dictionary.md": "# 指标口径表\n\n| 指标名称 | 业务定义 | 计算公式 | 数据来源 | 更新频率 | 负责人 | 适用范围 | 异常处理 | 看板位置 |\n|---|---|---|---|---|---|---|---|---|\n",
    "11-sop-governance/quality-gates.md": "# 质量门禁与阶段准入 / 准出标准\n\n| 阶段 | 输入物 | 输出物 | 负责人 | 评审人 | 准入条件 | 准出条件 | 归档位置 |\n|---|---|---|---|---|---|---|---|\n",
    "11-sop-governance/launch-approval.md": "# 上线审批\n\n| 审批项 | 检查内容 | 负责人 | 状态 |\n|---|---|---|---|\n",
    "11-sop-governance/compliance-risks.md": "# 合规风险检查\n\n| 风险类型 | 检查问题 | 应对方式 | 负责人 |\n|---|---|---|---|\n",
}

GLOSSARY = [
    ("PRD", "产品需求文档，用来说明要做什么、为什么做、怎么验收"),
    ("MVP", "最小可用版本，用最少功能验证用户是否真的需要"),
    ("用户画像", "对典型用户的简化描述，包括身份、目标、痛点和行为"),
    ("用户旅程", "用户从产生需求到完成目标的全过程"),
    ("需求拆解", "把模糊想法拆成可执行的用户、业务、功能和技术需求"),
    ("信息架构", "页面、内容、功能之间如何组织"),
    ("北极星指标", "最能代表产品是否成功的核心指标"),
    ("A/B 测试", "同时测试两个方案，看哪个效果更好"),
    ("留存", "用户使用后是否还会回来"),
    ("转化", "用户完成注册、付费、提交等目标行为"),
    ("DDD", "把复杂业务按领域拆清楚，方便产品和开发沟通"),
    ("RACI", "说明谁负责执行、谁最终拍板、谁协作咨询、谁需要知会"),
    ("质量门禁", "每个阶段进入下一阶段前必须满足的质量条件"),
    ("指标口径", "明确一个指标的定义、计算方式、数据来源和负责人"),
    ("上线审批", "上线前由相关角色确认质量、风险、发布和回滚方案"),
    ("合规风险", "产品可能涉及隐私、数据安全、内容、支付、AI、监管等风险"),
    ("容器化", "用 Docker 等方式让系统更容易部署和迁移"),
    ("灰度发布", "先让少量用户使用新版本，确认稳定后再全面发布"),
    ("回滚", "新版本出问题时退回旧版本"),
]


def load_json(file_path: str) -> Dict[str, Any]:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"找不到文件：{file_path}")
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def validate_brief(data: Dict[str, Any]) -> None:
    missing = [key for key in REQUIRED_BRIEF_KEYS if key not in data]
    if missing:
        raise ValueError(f"产品信息 JSON 缺少字段：{', '.join(missing)}")

    for key in LIST_KEYS:
        if not isinstance(data[key], list):
            raise TypeError(f"字段 {key} 应该是 list 类型")

    for item in data.get("features", []):
        if not isinstance(item, dict):
            raise TypeError("features 中的每一项建议使用对象格式，包含 name、description、priority")
        for field in ["name", "description", "priority"]:
            if field not in item:
                raise ValueError(f"features 中的功能项缺少字段：{field}")

    for item in data.get("competitors", []):
        if not isinstance(item, dict):
            raise TypeError("competitors 中的每一项建议使用对象格式")
        for field in ["name", "positioning", "strength", "weakness"]:
            if field not in item:
                raise ValueError(f"competitors 中的竞品项缺少字段：{field}")
    for item in data.get("metric_definitions", []):
        if not isinstance(item, dict):
            raise TypeError("metric_definitions 中的每一项建议使用对象格式")
        for field in ["name", "definition", "formula", "source", "frequency", "owner", "scope", "exception_handling", "dashboard_location"]:
            if field not in item:
                raise ValueError(f"metric_definitions 中的指标项缺少字段：{field}")

    for item in data.get("phase_gate_standards", []):
        if not isinstance(item, dict):
            raise TypeError("phase_gate_standards 中的每一项建议使用对象格式")
        for field in ["stage", "input", "output", "responsible", "reviewer", "entry_criteria", "exit_criteria", "archive_location"]:
            if field not in item:
                raise ValueError(f"phase_gate_standards 中的阶段项缺少字段：{field}")

    for item in data.get("raci", []):
        if not isinstance(item, dict):
            raise TypeError("raci 中的每一项建议使用对象格式")
        for field in ["task", "responsible", "accountable", "consulted", "informed"]:
            if field not in item:
                raise ValueError(f"raci 中的责任项缺少字段：{field}")



def normalize_list(items: List[Any], default: str = "待补充") -> List[str]:
    if not items:
        return [default]
    result = []
    for item in items:
        if isinstance(item, dict):
            if "name" in item and "description" in item:
                result.append(f"{item.get('priority', '')} {item['name']}：{item['description']}".strip())
            elif "name" in item:
                result.append(str(item["name"]))
            else:
                result.append("；".join(f"{k}：{v}" for k, v in item.items()))
        else:
            result.append(str(item))
    return result


def init_project(args):
    root = Path(args.name)
    root.mkdir(exist_ok=True)

    for directory in DEFAULT_PROJECT_DIRS:
        (root / directory).mkdir(parents=True, exist_ok=True)

    for file_path, content in DEFAULT_FILES.items():
        full_path = root / file_path
        if not full_path.exists() or args.force:
            write_text(full_path, content)

    readme = f"""# {args.name}

这是由 Universal Product Manager Skill Toolkit v2.1 初始化的产品项目工作目录。

## 推荐工作流程

1. 先写用户和场景
2. 再做用户研究与竞品分析
3. 拆解需求并设计 MVP
4. 输出产品方案和产品拆解图
5. 设计指标、实验、测试和发布检查清单
6. 补充评审机制、RACI、质量门禁、上线审批和合规风险
7. 持续记录日志并复盘

## 新手提醒

不要一开始就追求完整系统，先用 MVP 验证核心问题是否真实存在。
"""
    write_text(root / "README.md", readme)
    print(f"项目已初始化：{root.resolve()}")


def generate_tree(data: Dict[str, Any]) -> str:
    product_name = data.get("product_name", "产品项目")
    lines = ["# 产品拆解图（树状图）", "", "```text", product_name]

    def add_section(title: str, items: List[Any], branch="├──"):
        lines.append(f"{branch} {title}")
        normalized = normalize_list(items)
        for idx, item in enumerate(normalized):
            sub = "│   └──" if idx == len(normalized) - 1 else "│   ├──"
            lines.append(f"{sub} {item}")

    add_section("1. 产品目标", data.get("goals", []))
    add_section("2. 目标用户", data.get("target_users", []))
    add_section("3. 核心场景", data.get("scenarios", []))
    add_section("4. 用户痛点", data.get("pain_points", []))
    add_section("5. 用户研究", data.get("user_research", []))

    competitor_items = []
    for comp in data.get("competitors", []):
        competitor_items.append(
            f"{comp.get('name', '未命名竞品')}：{comp.get('positioning', '定位待补充')}；优势：{comp.get('strength', '待补充')}；不足：{comp.get('weakness', '待补充')}"
        )
    add_section("6. 竞品分析", competitor_items or ["待补充"])
    add_section("7. 功能模块", data.get("features", []))
    add_section("8. 用户增长", data.get("growth", []))
    add_section("9. 指标体系", data.get("metrics", []))
    add_section("10. 实验设计", data.get("experiments", []))
    add_section("11. 数据与技术", data.get("technology", []))
    add_section("12. 测试与验收", data.get("testing", []))
    add_section("13. 标准化流程", data.get("standardized_process", []))
    add_section("14. 组织协作", data.get("collaboration", []))
    add_section("15. 评审机制", data.get("reviews", []))
    add_section("16. 指标口径", data.get("metric_definitions", []))
    add_section("17. 质量门禁", data.get("quality_gates", []))
    add_section("18. 阶段准入 / 准出标准", data.get("phase_gate_standards", []))
    add_section("18. 上线审批", data.get("launch_approval", []))
    add_section("19. 合规风险", data.get("compliance_risks", []))
    add_section("20. MVP 范围", data.get("mvp", []))
    add_section("21. 风险分析", data.get("risks", []))

    lines.append("└── 22. 下一步行动")
    steps = normalize_list(data.get("next_steps", []))
    for idx, step in enumerate(steps):
        sub = "    └──" if idx == len(steps) - 1 else "    ├──"
        lines.append(f"{sub} {step}")

    lines.append("```")
    return "\n".join(lines)


def generate_mindmap(data: Dict[str, Any]) -> str:
    product_name = data.get("product_name", "产品项目")
    sections = {
        "产品目标": data.get("goals", []),
        "目标用户": data.get("target_users", []),
        "核心场景": data.get("scenarios", []),
        "用户痛点": data.get("pain_points", []),
        "用户研究": data.get("user_research", []),
        "竞品分析": [c.get("name", "未命名竞品") for c in data.get("competitors", [])],
        "功能模块": data.get("features", []),
        "用户增长": data.get("growth", []),
        "指标体系": data.get("metrics", []),
        "实验设计": data.get("experiments", []),
        "数据与技术": data.get("technology", []),
        "测试与验收": data.get("testing", []),
        "标准化流程": data.get("standardized_process", []),
        "组织协作": data.get("collaboration", []),
        "评审机制": data.get("reviews", []),
        "指标口径": data.get("metric_definitions", []),
        "质量门禁": data.get("quality_gates", []),
        "阶段准入 / 准出标准": data.get("phase_gate_standards", []),
        "上线审批": data.get("launch_approval", []),
        "合规风险": data.get("compliance_risks", []),
        "MVP 范围": data.get("mvp", []),
        "风险分析": data.get("risks", []),
        "下一步行动": data.get("next_steps", []),
    }
    lines = ["# 产品拆解图（思维导图）", "", f"- {product_name}"]
    for section, items in sections.items():
        lines.append(f"  - {section}")
        for item in normalize_list(items):
            lines.append(f"    - {item}")
    return "\n".join(lines)


def generate_mermaid(data: Dict[str, Any]) -> str:
    product_name = str(data.get("product_name", "产品项目")).replace("(", "（").replace(")", "）")
    sections = {
        "产品目标": data.get("goals", []),
        "目标用户": data.get("target_users", []),
        "核心场景": data.get("scenarios", []),
        "用户痛点": data.get("pain_points", []),
        "用户研究": data.get("user_research", []),
        "竞品分析": [c.get("name", "未命名竞品") for c in data.get("competitors", [])],
        "功能模块": data.get("features", []),
        "增长指标实验": data.get("growth", []) + data.get("metrics", []) + data.get("experiments", []),
        "技术测试发布": data.get("technology", []) + data.get("testing", []) + data.get("release_checklist", []),
        "SOP治理": data.get("standardized_process", []) + data.get("reviews", []) + data.get("quality_gates", []) + data.get("phase_gate_standards", []) + data.get("launch_approval", []) + data.get("compliance_risks", []),
        "MVP风险行动": data.get("mvp", []) + data.get("risks", []) + data.get("next_steps", []),
    }
    lines = ["# 产品拆解图（Mermaid Mindmap）", "", "```mermaid", "mindmap", f"  root(({product_name}))"]
    for section, items in sections.items():
        lines.append(f"    {section}")
        for item in normalize_list(items):
            safe = str(item).replace(":", "：").replace("(", "（").replace(")", "）")
            lines.append(f"      {safe}")
    lines.append("```")
    return "\n".join(lines)


def generate_breakdown(args):
    data = load_json(args.input)
    validate_brief(data)
    if args.type == "tree":
        content = generate_tree(data)
    elif args.type == "mindmap":
        content = generate_mindmap(data)
    elif args.type == "mermaid":
        content = generate_mermaid(data)
    else:
        raise ValueError("type 只能是 tree、mindmap 或 mermaid")
    write_text(Path(args.output), content)
    print(f"产品拆解图已生成：{Path(args.output).resolve()}")


def validate_report(args):
    path = Path(args.file)
    if not path.exists():
        raise FileNotFoundError(f"找不到文件：{args.file}")
    content = path.read_text(encoding="utf-8")
    sections = COMPLETE_SECTIONS if args.complete else REQUIRED_SECTIONS
    existing = [section for section in sections if section in content]
    missing = [section for section in sections if section not in content]
    print("产品方案完整性检查结果")
    print("-" * 40)
    print("\n已包含章节：")
    for item in existing:
        print(f"  ✅ {item}")
    print("\n缺失章节：")
    if missing:
        for item in missing:
            print(f"  ❌ {item}")
    else:
        print("  无缺失，文档结构完整。")
    score = int(len(existing) / len(sections) * 100)
    print(f"\n完整度评分：{score}%")


def validate_brief_command(args):
    data = load_json(args.input)
    validate_brief(data)
    print("产品信息 JSON 校验通过。")


def add_log(args):
    project = Path(args.project)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mapping = {
        "decision": ("08-operations/decision-log.md", "# 决策日志\n\n| 时间 | 决策内容 |\n|---|---|\n", f"| {now} | {args.message} |\n"),
        "issue": ("08-operations/incident-log.md", "# 问题 / 故障日志\n\n| 时间 | 问题内容 | 状态 |\n|---|---|---|\n", f"| {now} | {args.message} | 待处理 |\n"),
        "release": ("08-operations/release-log.md", "# 发布日志\n\n| 时间 | 发布内容 |\n|---|---|\n", f"| {now} | {args.message} |\n"),
        "learning": ("10-learning-notes/learning-log.md", "# 学习日志\n\n| 时间 | 学习内容 |\n|---|---|\n", f"| {now} | {args.message} |\n"),
    }
    rel_path, title, row = mapping[args.type]
    log_file = project / rel_path
    log_file.parent.mkdir(parents=True, exist_ok=True)
    if not log_file.exists():
        log_file.write_text(title, encoding="utf-8")
    with log_file.open("a", encoding="utf-8") as f:
        f.write(row)
    print(f"日志已追加：{log_file.resolve()}")


def generate_test_cases(args):
    data = load_json(args.input)
    validate_brief(data)
    lines = [
        "# 自动化测试用例模板",
        "",
        "| 用例编号 | 功能模块 | 测试场景 | 前置条件 | 操作步骤 | 预期结果 | 优先级 |",
        "|---|---|---|---|---|---|---|",
    ]
    for idx, feature in enumerate(data.get("features", []), start=1):
        name = feature.get("name", "未命名功能")
        priority = feature.get("priority", "P0")
        case_id = f"TC{idx:03d}"
        lines.append(f"| {case_id} | {name} | 正常使用流程 | 用户已登录 | 进入功能页面并完成核心操作 | 操作成功，数据正确保存 | {priority} |")
        lines.append(f"| {case_id}-E | {name} | 异常状态处理 | 用户已登录 | 输入异常数据或中断流程 | 系统给出清晰提示且不产生错误数据 | {priority} |")
    write_text(Path(args.output), "\n".join(lines))
    print(f"测试用例已生成：{Path(args.output).resolve()}")


def generate_release_checklist(args):
    data = load_json(args.input)
    validate_brief(data)
    items = normalize_list(data.get("release_checklist", []) + data.get("quality_gates", []) + data.get("launch_approval", []) + data.get("compliance_risks", []))
    lines = [
        "# 发布检查清单",
        "",
        "| 检查项 | 检查说明 | 是否通过 | 负责人 | 备注 |",
        "|---|---|---|---|---|",
    ]
    for item in items:
        lines.append(f"| {item} | 上线前确认该项已完成 | 是 / 否 |  |  |")
    write_text(Path(args.output), "\n".join(lines))
    print(f"发布检查清单已生成：{Path(args.output).resolve()}")


def generate_beginner_guide(args):
    content = """# 产品经理新手引导

## 1. 你现在不是先写功能，而是先理解问题

产品经理的第一步不是画页面，也不是列功能，而是弄清楚：谁在什么场景下遇到了什么问题。

## 2. 新手推荐工作顺序

```text
理解用户 → 理解场景 → 验证痛点 → 分析竞品 → 拆解需求 → 设计 MVP → 设计指标 → 测试发布 → 复盘迭代
```

## 3. 每一步要问的问题

| 阶段 | 要问的问题 |
|---|---|
| 用户 | 谁会用这个产品？ |
| 场景 | 他什么时候会遇到这个问题？ |
| 痛点 | 这个问题是否高频、强烈、值得解决？ |
| 竞品 | 现在别人怎么解决？ |
| MVP | 最小版本只需要验证什么？ |
| 指标 | 怎么判断产品是否有效？ |
| 测试 | 怎么证明功能能正常使用？ |
| 发布 | 上线前哪些风险必须检查？ |

## 4. 新手最容易犯的错

- 一开始就做大而全
- 把自己的想法当成用户需求
- 只看竞品界面，不看竞品策略
- 没有定义 MVP 成功标准
- 不知道用什么指标判断产品好坏
- 上线前没有测试和回滚方案

## 5. 最小行动清单

1. 写出目标用户
2. 写出 3 个真实使用场景
3. 写出 3 个用户痛点
4. 找 3 个竞品
5. 设计 1 个 MVP 核心流程
6. 定义 1 个北极星指标
7. 写出 5 条测试用例
"""
    write_text(Path(args.output), content)
    print(f"新手引导文档已生成：{Path(args.output).resolve()}")



def generate_raci_matrix(args):
    data = load_json(args.input)
    validate_brief(data)
    items = data.get("raci", [])
    lines = [
        "# RACI 责任矩阵",
        "",
        "| 事项 | R 负责执行 | A 最终负责 | C 协作咨询 | I 知会 |",
        "|---|---|---|---|---|",
    ]
    if not items:
        items = [
            {"task": "需求收集", "responsible": "产品经理", "accountable": "产品负责人", "consulted": "运营 / 数据 / 客服", "informed": "研发 / 设计"},
            {"task": "上线发布", "responsible": "研发 / 运维", "accountable": "项目负责人", "consulted": "产品 / 测试 / 安全", "informed": "全体相关方"},
        ]
    for item in items:
        lines.append(
            f"| {item.get('task', '')} | {item.get('responsible', '')} | {item.get('accountable', '')} | {item.get('consulted', '')} | {item.get('informed', '')} |"
        )
    write_text(Path(args.output), "\n".join(lines))
    print(f"RACI 责任矩阵已生成：{Path(args.output).resolve()}")


def generate_sop_checklist(args):
    data = load_json(args.input)
    validate_brief(data)
    sections = {
        "标准化流程": data.get("standardized_process", []),
        "组织协作": data.get("collaboration", []),
        "评审机制": data.get("reviews", []),
        "质量门禁": data.get("quality_gates", []),
        "阶段准入 / 准出标准": data.get("phase_gate_standards", []),
        "上线审批": data.get("launch_approval", []),
        "合规风险": data.get("compliance_risks", []),
    }
    lines = ["# 大厂产品交付 SOP 检查清单", "", "| 模块 | 检查项 | 是否完成 | 负责人 | 备注 |", "|---|---|---|---|---|"]
    for section, items in sections.items():
        for item in normalize_list(items):
            lines.append(f"| {section} | {item} | 是 / 否 |  |  |")
    write_text(Path(args.output), "\n".join(lines))
    print(f"SOP 检查清单已生成：{Path(args.output).resolve()}")


def generate_metric_dictionary(args):
    data = load_json(args.input)
    validate_brief(data)
    metrics = data.get("metric_definitions", [])
    lines = [
        "# 指标口径表",
        "",
        "| 指标名称 | 业务定义 | 计算公式 | 数据来源 | 更新频率 | 负责人 | 适用范围 | 异常处理 | 看板位置 |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for item in metrics:
        lines.append(
            f"| {item.get('name', '')} | {item.get('definition', '')} | {item.get('formula', '')} | {item.get('source', '')} | {item.get('frequency', '')} | {item.get('owner', '')} | {item.get('scope', '')} | {item.get('exception_handling', '')} | {item.get('dashboard_location', '')} |"
        )
    write_text(Path(args.output), "\n".join(lines))
    print(f"指标口径表已生成：{Path(args.output).resolve()}")


def generate_phase_gates(args):
    data = load_json(args.input)
    validate_brief(data)
    gates = data.get("phase_gate_standards", [])
    lines = [
        "# 阶段准入 / 准出标准表",
        "",
        "| 阶段 | 输入物 | 输出物 | 负责人 | 评审人 | 准入条件 | 准出条件 | 归档位置 |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for item in gates:
        lines.append(
            f"| {item.get('stage', '')} | {item.get('input', '')} | {item.get('output', '')} | {item.get('responsible', '')} | {item.get('reviewer', '')} | {item.get('entry_criteria', '')} | {item.get('exit_criteria', '')} | {item.get('archive_location', '')} |"
        )
    write_text(Path(args.output), "\n".join(lines))
    print(f"阶段准入 / 准出标准表已生成：{Path(args.output).resolve()}")


def generate_glossary(args):
    lines = ["# 产品经理术语表", "", "| 术语 | 新手解释 |", "|---|---|"]
    for term, explanation in GLOSSARY:
        lines.append(f"| {term} | {explanation} |")
    write_text(Path(args.output), "\n".join(lines))
    print(f"术语表已生成：{Path(args.output).resolve()}")


def main():
    parser = argparse.ArgumentParser(description="Universal Product Manager Skill Toolkit v2.1")
    subparsers = parser.add_subparsers(dest="command")

    init_parser = subparsers.add_parser("init", help="初始化产品项目目录")
    init_parser.add_argument("--name", required=True, help="项目名称")
    init_parser.add_argument("--force", action="store_true", help="覆盖已存在文件")
    init_parser.set_defaults(func=init_project)

    breakdown_parser = subparsers.add_parser("breakdown", help="生成产品拆解图")
    breakdown_parser.add_argument("--input", required=True, help="产品信息 JSON 文件")
    breakdown_parser.add_argument("--output", required=True, help="输出 Markdown 文件")
    breakdown_parser.add_argument("--type", choices=["tree", "mindmap", "mermaid"], default="tree", help="输出类型")
    breakdown_parser.set_defaults(func=generate_breakdown)

    validate_parser = subparsers.add_parser("validate", help="校验产品方案完整性")
    validate_parser.add_argument("--file", required=True, help="产品方案 Markdown 文件")
    validate_parser.add_argument("--complete", action="store_true", help="按完整版章节校验")
    validate_parser.set_defaults(func=validate_report)

    brief_parser = subparsers.add_parser("validate-brief", help="校验产品信息 JSON 模板")
    brief_parser.add_argument("--input", required=True, help="产品信息 JSON 文件")
    brief_parser.set_defaults(func=validate_brief_command)

    log_parser = subparsers.add_parser("log", help="追加项目日志")
    log_parser.add_argument("--project", required=True, help="项目目录")
    log_parser.add_argument("--type", choices=["decision", "issue", "release", "learning"], required=True, help="日志类型")
    log_parser.add_argument("--message", required=True, help="日志内容")
    log_parser.set_defaults(func=add_log)

    testcase_parser = subparsers.add_parser("testcase", help="生成测试用例模板")
    testcase_parser.add_argument("--input", required=True, help="产品信息 JSON 文件")
    testcase_parser.add_argument("--output", required=True, help="输出测试用例 Markdown 文件")
    testcase_parser.set_defaults(func=generate_test_cases)

    release_parser = subparsers.add_parser("release-checklist", help="生成发布检查清单")
    release_parser.add_argument("--input", required=True, help="产品信息 JSON 文件")
    release_parser.add_argument("--output", required=True, help="输出 Markdown 文件")
    release_parser.set_defaults(func=generate_release_checklist)

    beginner_parser = subparsers.add_parser("beginner-guide", help="生成产品经理新手引导文档")
    beginner_parser.add_argument("--output", required=True, help="输出 Markdown 文件")
    beginner_parser.set_defaults(func=generate_beginner_guide)

    glossary_parser = subparsers.add_parser("glossary", help="生成产品经理术语表")
    glossary_parser.add_argument("--output", required=True, help="输出 Markdown 文件")
    glossary_parser.set_defaults(func=generate_glossary)


    raci_parser = subparsers.add_parser("raci", help="生成 RACI 责任矩阵")
    raci_parser.add_argument("--input", required=True, help="产品信息 JSON 文件")
    raci_parser.add_argument("--output", required=True, help="输出 Markdown 文件")
    raci_parser.set_defaults(func=generate_raci_matrix)

    sop_parser = subparsers.add_parser("sop-checklist", help="生成大厂 SOP 检查清单")
    sop_parser.add_argument("--input", required=True, help="产品信息 JSON 文件")
    sop_parser.add_argument("--output", required=True, help="输出 Markdown 文件")
    sop_parser.set_defaults(func=generate_sop_checklist)

    metric_parser = subparsers.add_parser("metric-dictionary", help="生成指标口径表")
    metric_parser.add_argument("--input", required=True, help="产品信息 JSON 文件")
    metric_parser.add_argument("--output", required=True, help="输出 Markdown 文件")
    metric_parser.set_defaults(func=generate_metric_dictionary)

    phase_parser = subparsers.add_parser("phase-gates", help="生成阶段准入 / 准出标准表")
    phase_parser.add_argument("--input", required=True, help="产品信息 JSON 文件")
    phase_parser.add_argument("--output", required=True, help="输出 Markdown 文件")
    phase_parser.set_defaults(func=generate_phase_gates)

    args = parser.parse_args()
    if not hasattr(args, "func"):
        parser.print_help()
        return
    args.func(args)


if __name__ == "__main__":
    main()
