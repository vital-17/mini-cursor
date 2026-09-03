from dataclasses import dataclass, field


@dataclass
class AgentState:

    # 用户需求
    requirement: str = ""

    # Planner输出
    plan: str = ""

    # Coder输出
    filename: str = ""
    code: str = ""

    # 执行结果
    execution: dict = field(
        default_factory=dict
    )

    # Reviewer输出
    review: str = ""

    # 重试次数
    retry_count: int = 0