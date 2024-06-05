from agency_swarm.tools import BaseTool
from pydantic import Field
import os
import requests

# Define any constant variables like API keys globally
api_key = os.getenv("MUI_API_KEY")

class InitializeChatInterface(BaseTool):
    """
    Initialize a chat interface using MUI. Manage the chat session, including starting and ending the session.
    """

    # Define the fields with descriptions using Pydantic Field
    session_id: str = Field(
        ..., description="The unique identifier for the chat session."
    )
    action: str = Field(
        ..., description="The action to perform: 'start' or 'end'."
    )

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method should utilize the fields defined above to perform the task.
        """
        # Define the base URL for the MUI API
        base_url = "https://api.mui.com/chat"

        # Determine the endpoint based on the action
        if self.action == "start":
            endpoint = f"{base_url}/start"
        elif self.action == "end":
            endpoint = f"{base_url}/end"
        else:
            return "Invalid action. Please specify 'start' or 'end'."

        # Prepare the payload for the API request
        payload = {
            "session_id": self.session_id,
            "api_key": api_key
        }

        # Make the API request
        response = requests.post(endpoint, json=payload)

        # Check the response status and return the result
        if response.status_code == 200:
            return f"Chat session {self.action}ed successfully."
        else:
            return f"Failed to {self.action} chat session. Error: {response.text}"