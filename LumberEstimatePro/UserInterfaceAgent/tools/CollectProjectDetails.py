from agency_swarm.tools import BaseTool
from pydantic import Field

class CollectProjectDetails(BaseTool):
    """
    Ask follow-up questions to gather all necessary project details. Store the collected details for further processing.
    """

    # Define the fields with descriptions using Pydantic Field
    session_id: str = Field(
        ..., description="The unique identifier for the chat session."
    )
    user_input: str = Field(
        ..., description="The input provided by the user in the chat interface."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method should utilize the fields defined above to perform the task.
        """
        # Access the shared state to get or update project details
        project_details = self.shared_state.get("project_details", {})

        # Define follow-up questions based on the current state of project details
        follow_up_questions = {
            "project_name": "What is the name of your project?",
            "project_description": "Can you provide a brief description of your project?",
            "deadline": "What is the deadline for this project?",
            "budget": "What is the budget for this project?",
            "team_size": "How many team members will be involved in this project?"
        }

        # Determine the next question to ask based on the current state of project details
        for key, question in follow_up_questions.items():
            if key not in project_details:
                # Store the current user input in the project details
                if self.user_input:
                    project_details[key] = self.user_input
                    self.shared_state.set("project_details", project_details)
                    return f"Thank you! {question}"

                # Ask the next follow-up question
                return question

        # If all details are collected, store them and return a confirmation message
        self.shared_state.set("project_details", project_details)
        return "Thank you! All necessary project details have been collected."