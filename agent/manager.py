from agent.planner import create_plan
from agent.coder import generate_code
from agent.reviewer import review
from tools.file_tool import create_file
from tools.runner import run_python


class AgentManager:

    def run(self, requirement: str) -> dict:
        print("\n[1/5] Planning...")
        plan = create_plan(requirement)

        print("\n[2/5] Coding...")
        code_result = generate_code(plan)

        filename = code_result["filename"]
        code = code_result["code"]

        print(f"\n[3/5] Writing {filename}...")
        filepath = create_file(filename, code)

        print("\n[4/5] Running...")
        execution_result = run_python(filename)

        print("\n[5/5] Reviewing...")
        review_result = review(
            code,
            execution_result
        )

        return {
            "requirement": requirement,
            "plan": plan,
            "filename": filename,
            "filepath": filepath,
            "code": code,
            "execution": execution_result,
            "review": review_result
        }