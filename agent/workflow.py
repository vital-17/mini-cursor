from agent.state import AgentState

from agent.planner import create_plan
from agent.coder import generate_code
from agent.reviewer import review

from tools.file_tool import create_file
from tools.runner import run_python



class AgentWorkflow:


    def run(self, requirement):

        state = AgentState(
            requirement=requirement
        )


        self.plan(state)

        self.code(state)

        self.execute(state)

        self.review(state)


        return state



    def plan(self,state):

        print("Planning...")

        state.plan = create_plan(
            state.requirement
        )



    def code(self,state):

        print("Coding...")

        result = generate_code(
            state.plan
        )


        state.filename = result["filename"]

        state.code = result["code"]



    def execute(self,state):

        print("Executing...")


        create_file(
            state.filename,
            state.code
        )


        state.execution = run_python(
            state.filename
        )



    def review(self,state):

        print("Reviewing...")


        state.review = review(
            state.code,
            state.execution
        )