from agency_swarm.agents import Agent


class UserInterfaceAgent(Agent):
    def __init__(self):
        super().__init__(
            name="UserInterfaceAgent",
            description="Interacts with the user, asks follow-up questions to clarify project details, and ensures all necessary information is gathered.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )
        
    def response_validator(self, message):
        return message
