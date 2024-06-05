from agency_swarm.agents import Agent


class LumberCEO(Agent):
    def __init__(self):
        super().__init__(
            name="LumberCEO",
            description="Oversees the entire process, coordinates between different agents, and ensures the workflow is smooth.",
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
