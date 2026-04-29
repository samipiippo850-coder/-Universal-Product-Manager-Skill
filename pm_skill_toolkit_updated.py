#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Universal Product Manager Skill Toolkit

用途：
1. 初始化产品项目文档目录
2. 生成产品方案基础模板
3. 生成产品拆解图
4. 校验产品报告完整性
5. 追加项目日志
6. 根据功能模块生成测试用例模板

适用场景：
- 通用产品经理 Skill
- 产品方案输出
- MVP 规划
- 项目归档
- 产品拆解图生成
"""

import argparse
import json
from pathlib import Path
from datetime import datetime


REQUIRED_SECTIONS = [
    "需求理解",
    "领域知识补充",
    "需求拆解",
    "产品定位",
    "功能模块设计",
    "用户流程设计",
    "产品原型设计",
    "用户增长方案",
    "数据库结构设计",
    "DDD",
    "容器化部署方案",
    "服务器管理方案",
    "自动化测试方案",
    "文件整理",
    "风险分析",
    "MVP",
    "下一步行动",
    "产品拆解图",
]


BRIEF_REQUIRED_KEYS = [
    "product_name",
    "goals",
    "target_users",
    "scenarios",
    "pain_points",
    "features",
    "growth",
    "technology",
    "testing",
    "mvp",
    "risks",
    "next_steps",
]


BRIEF_LIST_KEYS = [
    "goals",
    "target_users",
    "scenarios",
    "pain_points",
    "features",
    "growth",
    "technology",
    "testing",
    "mvp",
    "risks",
    "next_steps",
]


ALLOWED_PRIORITIES = {"P0", "P1", "P2", "P3"}


DEFAULT_PROJECT_DIRS = [
    "01-requirements",
    "02-product-design",
    "03-technical-design",
    "04-growth",
    "05-testing",
    "06-operations",
    "07-review",
]


DEFAULT_FILES = {
    "01-requirements/user-requirements.md": "# 用户需求文档\n\n## 目标用户\n\n## 用户痛点\n\n## 用户场景\n\n## 用户需求列表\n",
    "01-requirements/business-requirements.md": "# 业务需求文档\n\n## 业务目标\n\n## 核心指标\n\n## 商业模式\n\n## 业务约束\n",
    "01-requirements/product-requirements.md": "# 产品需求文档 PRD\n\n## 产品背景\n\n## 产品目标\n\n## 功能需求\n\n## 非功能需求\n\n## 验收标准\n",
    "02-product-design/product-solution.md": "# 产品方案报告\n\n## 1. 需求理解\n\n## 2. 领域知识补充\n\n## 3. 需求拆解\n\n## 4. 产品定位\n\n## 5. 功能模块设计\n\n## 6. 用户流程设计\n\n## 7. 产品原型设计\n\n## 8. 用户增长方案\n\n## 9. 数据库结构设计\n\n## 10. DDD 领域建模\n\n## 11. 容器化部署方案\n\n## 12. 服务器管理方案\n\n## 13. 自动化测试方案\n\n## 14. 文件整理与日志归档方案\n\n## 15. 风险分析\n\n## 16. MVP 版本计划\n\n## 17. 下一步行动清单\n\n## 18. 产品拆解图\n",
    "02-product-design/user-flow.md": "# 用户流程设计\n\n## 核心用户流程\n\n## 异常流程\n\n## 权限差异\n",
    "02-product-design/information-architecture.md": "# 信息架构\n\n## 页面结构\n\n## 导航结构\n\n## 数据结构关系\n",
    "02-product-design/product-breakdown-map.md": "# 产品拆解图\n\n",
    "03-technical-design/database-design.md": "# 数据库结构设计\n\n## 核心实体\n\n## 数据表设计\n\n## 索引设计\n\n## 数据安全\n",
    "03-technical-design/domain-model.md": "# DDD 领域模型\n\n## 核心领域\n\n## 子领域\n\n## 限界上下文\n\n## 聚合根\n\n## 领域事件\n",
    "03-technical-design/api-design.md": "# API 设计\n\n## API 列表\n\n## 请求参数\n\n## 响应结构\n\n## 错误码\n",
    "03-technical-design/deployment-plan.md": "# 部署方案\n\n## 本地开发\n\n## 测试环境\n\n## 生产环境\n\n## 回滚方案\n",
    "04-growth/growth-strategy.md": "# 用户增长方案\n\n## 增长目标\n\n## 获客策略\n\n## 激活策略\n\n## 留存策略\n\n## 转化策略\n",
    "04-growth/metrics-dashboard.md": "# 指标看板设计\n\n## 北极星指标\n\n## 用户指标\n\n## 业务指标\n\n## 技术指标\n",
    "05-testing/test-plan.md": "# 测试计划\n\n## 测试目标\n\n## 测试范围\n\n## 测试类型\n\n## 验收标准\n",
    "05-testing/test-cases.md": "# 测试用例\n\n",
    "05-testing/bug-log.md": "# Bug 记录\n\n| 日期 | 问题 | 影响范围 | 优先级 | 状态 |\n|---|---|---|---|---|\n",
    "06-operations/server-management.md": "# 服务器管理方案\n\n## 服务器配置\n\n## 安全配置\n\n## 监控方案\n\n## 备份方案\n",
    "06-operations/release-log.md": "# 发布日志\n\n| 版本 | 日期 | 内容 | 风险 | 状态 |\n|---|---|---|---|---|\n",
    "06-operations/incident-log.md": "# 故障记录\n\n| 时间 | 故障 | 影响 | 原因 | 处理方案 | 状态 |\n|---|---|---|---|---|---|\n",
    "07-review/weekly-review.md": "# 周复盘\n\n## 本周完成\n\n## 遇到问题\n\n## 下周计划\n",
    "07-review/project-retrospective.md": "# 项目复盘\n\n## 项目目标\n\n## 实际结果\n\n## 经验总结\n\n## 后续优化\n",
}


def load_json(file_path: str) -> dict:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"找不到文件：{file_path}")

    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def validate_brief(data: dict):
    """校验产品信息 JSON 的必要字段和字段类型。"""

    if not isinstance(data, dict):
        raise TypeError("产品信息 JSON 顶层结构必须是对象（dict）。")

    missing = [key for key in BRIEF_REQUIRED_KEYS if key not in data]
    if missing:
        raise ValueError(f"产品信息 JSON 缺少字段：{', '.join(missing)}")

    product_name = data.get("product_name")
    if not isinstance(product_name, str) or not product_name.strip():
        raise TypeError("字段 product_name 必须是非空字符串。")

    for key in BRIEF_LIST_KEYS:
        if not isinstance(data.get(key), list):
            raise TypeError(f"字段 {key} 必须是列表（list）。")

    for key in BRIEF_LIST_KEYS:
        if key == "features":
            continue

        for index, item in enumerate(data.get(key, []), start=1):
            if not isinstance(item, str) or not item.strip():
                raise TypeError(f"字段 {key} 的第 {index} 项必须是非空字符串。")

    for index, item in enumerate(data.get("features", []), start=1):
        if isinstance(item, str):
            if not item.strip():
                raise TypeError(f"features 的第 {index} 项不能为空字符串。")
            continue

        if not isinstance(item, dict):
            raise TypeError(f"features 的第 {index} 项必须是字符串或对象。")

        for field in ["name", "description", "priority"]:
            value = item.get(field)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"features 的第 {index} 项缺少非空字段：{field}")

        priority = item.get("priority", "").strip()
        if priority not in ALLOWED_PRIORITIES:
            raise ValueError(
                f"features 的第 {index} 项 priority 应为 P0、P1、P2 或 P3，当前为：{priority}"
            )


def write_text(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def init_project(args):
    project_name = args.name
    root = Path(project_name)

    root.mkdir(exist_ok=True)

    for directory in DEFAULT_PROJECT_DIRS:
        (root / directory).mkdir(parents=True, exist_ok=True)

    for file_path, content in DEFAULT_FILES.items():
        full_path = root / file_path
        if not full_path.exists() or args.force:
            write_text(full_path, content)

    readme = f"""# {project_name}

## 项目说明

这是由 Universal Product Manager Skill Toolkit 初始化的产品项目工作目录。

## 推荐工作流程

1. 填写用户需求文档
2. 编写产品方案报告
3. 生成产品拆解图
4. 设计数据库结构与 DDD 模型
5. 制定增长方案
6. 设计原型与测试用例
7. 完成部署与服务器管理方案
8. 持续记录日志与复盘

## 目录说明

- 01-requirements：需求文档
- 02-product-design：产品设计文档
- 03-technical-design：技术设计文档
- 04-growth：用户增长文档
- 05-testing：测试文档
- 06-operations：运维与发布文档
- 07-review：复盘文档
"""
    write_text(root / "README.md", readme)

    print(f"项目已初始化：{root.resolve()}")


def generate_tree(data: dict) -> str:
    product_name = data.get("product_name", "产品项目")

    goals = data.get("goals", [])
    users = data.get("target_users", [])
    scenarios = data.get("scenarios", [])
    pain_points = data.get("pain_points", [])
    features = data.get("features", [])
    growth = data.get("growth", [])
    tech = data.get("technology", [])
    testing = data.get("testing", [])
    mvp = data.get("mvp", [])
    risks = data.get("risks", [])
    next_steps = data.get("next_steps", [])

    def lines_from_list(items, prefix="│   ├──"):
        if not items:
            return [f"{prefix} 待补充"]
        return [f"{prefix} {item}" for item in items]

    content = []
    content.append("# 产品拆解图（树状图）")
    content.append("")
    content.append("```text")
    content.append(product_name)

    content.append("├── 1. 产品目标")
    content.extend(lines_from_list(goals))

    content.append("├── 2. 用户与场景")
    content.append("│   ├── 目标用户")
    for user in users or ["待补充"]:
        content.append(f"│   │   ├── {user}")
    content.append("│   ├── 核心场景")
    for scenario in scenarios or ["待补充"]:
        content.append(f"│   │   ├── {scenario}")
    content.append("│   └── 用户痛点")
    for pain in pain_points or ["待补充"]:
        content.append(f"│       ├── {pain}")

    content.append("├── 3. 功能模块")
    if features:
        for feature in features:
            if isinstance(feature, dict):
                name = feature.get("name", "未命名功能")
                priority = feature.get("priority", "P?")
                desc = feature.get("description", "待补充")
                content.append(f"│   ├── {priority} {name}：{desc}")
            else:
                content.append(f"│   ├── {feature}")
    else:
        content.append("│   ├── 待补充")

    content.append("├── 4. 用户增长")
    content.extend(lines_from_list(growth))

    content.append("├── 5. 数据与技术")
    content.extend(lines_from_list(tech))

    content.append("├── 6. 原型与测试")
    content.extend(lines_from_list(testing))

    content.append("├── 7. MVP 范围")
    content.extend(lines_from_list(mvp))

    content.append("├── 8. 风险分析")
    content.extend(lines_from_list(risks))

    content.append("└── 9. 下一步行动")
    if next_steps:
        for i, step in enumerate(next_steps):
            branch = "    └──" if i == len(next_steps) - 1 else "    ├──"
            content.append(f"{branch} {step}")
    else:
        content.append("    └── 待补充")

    content.append("```")
    return "\n".join(content)


def generate_mindmap(data: dict) -> str:
    product_name = data.get("product_name", "产品项目")

    sections = {
        "产品目标": data.get("goals", []),
        "目标用户": data.get("target_users", []),
        "核心场景": data.get("scenarios", []),
        "用户痛点": data.get("pain_points", []),
        "功能模块": [
            f"{item.get('priority', 'P?')} {item.get('name', '未命名功能')}"
            if isinstance(item, dict)
            else str(item)
            for item in data.get("features", [])
        ],
        "用户增长": data.get("growth", []),
        "数据与技术": data.get("technology", []),
        "原型与测试": data.get("testing", []),
        "MVP 范围": data.get("mvp", []),
        "风险分析": data.get("risks", []),
        "下一步行动": data.get("next_steps", []),
    }

    content = []
    content.append("# 产品拆解图（思维导图）")
    content.append("")
    content.append(f"- {product_name}")

    for section, items in sections.items():
        content.append(f"  - {section}")
        if items:
            for item in items:
                content.append(f"    - {item}")
        else:
            content.append("    - 待补充")

    return "\n".join(content)


def generate_mermaid(data: dict) -> str:
    product_name = data.get("product_name", "产品项目")

    sections = {
        "产品目标": data.get("goals", []),
        "目标用户": data.get("target_users", []),
        "核心场景": data.get("scenarios", []),
        "用户痛点": data.get("pain_points", []),
        "功能模块": [
            f"{item.get('priority', 'P?')} {item.get('name', '未命名功能')}"
            if isinstance(item, dict)
            else str(item)
            for item in data.get("features", [])
        ],
        "用户增长": data.get("growth", []),
        "数据与技术": data.get("technology", []),
        "原型与测试": data.get("testing", []),
        "MVP范围": data.get("mvp", []),
        "风险分析": data.get("risks", []),
        "下一步行动": data.get("next_steps", []),
    }

    content = []
    content.append("# 产品拆解图（Mermaid Mindmap）")
    content.append("")
    content.append("```mermaid")
    content.append("mindmap")
    content.append(f"  root(({product_name}))")

    for section, items in sections.items():
        content.append(f"    {section}")
        if items:
            for item in items:
                safe_item = str(item).replace(":", "：").replace("(", "（").replace(")", "）")
                content.append(f"      {safe_item}")
        else:
            content.append("      待补充")

    content.append("```")
    return "\n".join(content)


def generate_breakdown(args):
    data = load_json(args.input)
    validate_brief(data)

    output_type = args.type

    if output_type == "tree":
        content = generate_tree(data)
    elif output_type == "mindmap":
        content = generate_mindmap(data)
    elif output_type == "mermaid":
        content = generate_mermaid(data)
    else:
        raise ValueError("type 只能是 tree、mindmap 或 mermaid")

    output_path = Path(args.output)
    write_text(output_path, content)
    print(f"产品拆解图已生成：{output_path.resolve()}")


def validate_report(args):
    path = Path(args.file)

    if not path.exists():
        raise FileNotFoundError(f"找不到文件：{args.file}")

    content = path.read_text(encoding="utf-8")

    missing = []
    existing = []

    for section in REQUIRED_SECTIONS:
        if section in content:
            existing.append(section)
        else:
            missing.append(section)

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

    score = int(len(existing) / len(REQUIRED_SECTIONS) * 100)
    print(f"\n完整度评分：{score}%")

    if missing:
        print("\n建议补充缺失章节后，再作为完整产品方案输出。")


def add_log(args):
    project = Path(args.project)
    log_type = args.type
    message = args.message
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if log_type == "decision":
        log_file = project / "06-operations" / "decision-log.md"
        title = "# 决策日志\n\n| 时间 | 决策内容 |\n|---|---|\n"
        row = f"| {now} | {message} |\n"
    elif log_type == "issue":
        log_file = project / "06-operations" / "incident-log.md"
        title = "# 问题 / 故障日志\n\n| 时间 | 问题内容 | 状态 |\n|---|---|---|\n"
        row = f"| {now} | {message} | 待处理 |\n"
    elif log_type == "release":
        log_file = project / "06-operations" / "release-log.md"
        title = "# 发布日志\n\n| 时间 | 发布内容 |\n|---|---|\n"
        row = f"| {now} | {message} |\n"
    else:
        raise ValueError("type 只能是 decision、issue 或 release")

    log_file.parent.mkdir(parents=True, exist_ok=True)

    if not log_file.exists():
        log_file.write_text(title, encoding="utf-8")

    with log_file.open("a", encoding="utf-8") as f:
        f.write(row)

    print(f"日志已追加：{log_file.resolve()}")


def generate_test_cases(args):
    data = load_json(args.input)
    validate_brief(data)
    features = data.get("features", [])

    content = []
    content.append("# 自动化测试用例模板")
    content.append("")
    content.append("| 用例编号 | 功能模块 | 测试场景 | 前置条件 | 操作步骤 | 预期结果 | 优先级 |")
    content.append("|---|---|---|---|---|---|---|")

    if not features:
        content.append("| TC001 | 待补充 | 待补充 | 待补充 | 待补充 | 待补充 | P0 |")
    else:
        for i, feature in enumerate(features, start=1):
            if isinstance(feature, dict):
                name = feature.get("name", "未命名功能")
                priority = feature.get("priority", "P0")
            else:
                name = str(feature)
                priority = "P0"

            case_id = f"TC{i:03d}"
            content.append(
                f"| {case_id} | {name} | 正常使用流程 | 用户已登录 | 进入功能页面并完成核心操作 | 操作成功，数据正确保存 | {priority} |"
            )

    output_path = Path(args.output)
    write_text(output_path, "\n".join(content))
    print(f"测试用例已生成：{output_path.resolve()}")


def validate_brief_file(args):
    data = load_json(args.input)
    validate_brief(data)
    print(f"产品信息 JSON 校验通过：{Path(args.input).resolve()}")


def main():
    parser = argparse.ArgumentParser(
        description="Universal Product Manager Skill Toolkit"
    )

    subparsers = parser.add_subparsers(dest="command")

    init_parser = subparsers.add_parser("init", help="初始化产品项目目录")
    init_parser.add_argument("--name", required=True, help="项目名称")
    init_parser.add_argument("--force", action="store_true", help="覆盖已存在文件")
    init_parser.set_defaults(func=init_project)

    breakdown_parser = subparsers.add_parser("breakdown", help="生成产品拆解图")
    breakdown_parser.add_argument("--input", required=True, help="产品信息 JSON 文件")
    breakdown_parser.add_argument("--output", required=True, help="输出 Markdown 文件")
    breakdown_parser.add_argument(
        "--type",
        choices=["tree", "mindmap", "mermaid"],
        default="tree",
        help="输出类型：tree / mindmap / mermaid",
    )
    breakdown_parser.set_defaults(func=generate_breakdown)

    validate_parser = subparsers.add_parser("validate", help="校验产品方案完整性")
    validate_parser.add_argument("--file", required=True, help="产品方案 Markdown 文件")
    validate_parser.set_defaults(func=validate_report)

    brief_parser = subparsers.add_parser("validate-brief", help="校验产品信息 JSON 模板")
    brief_parser.add_argument("--input", required=True, help="产品信息 JSON 文件")
    brief_parser.set_defaults(func=validate_brief_file)

    log_parser = subparsers.add_parser("log", help="追加项目日志")
    log_parser.add_argument("--project", required=True, help="项目目录")
    log_parser.add_argument(
        "--type",
        choices=["decision", "issue", "release"],
        required=True,
        help="日志类型",
    )
    log_parser.add_argument("--message", required=True, help="日志内容")
    log_parser.set_defaults(func=add_log)

    testcase_parser = subparsers.add_parser("testcase", help="生成测试用例模板")
    testcase_parser.add_argument("--input", required=True, help="产品信息 JSON 文件")
    testcase_parser.add_argument("--output", required=True, help="输出测试用例 Markdown 文件")
    testcase_parser.set_defaults(func=generate_test_cases)

    args = parser.parse_args()

    if not hasattr(args, "func"):
        parser.print_help()
        return

    try:
        args.func(args)
    except (FileNotFoundError, json.JSONDecodeError, TypeError, ValueError) as exc:
        print(f"错误：{exc}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()