from agency_swarm.tools import BaseTool
from pydantic import Field
import os
import requests

# Define any constant variables like API keys globally
api_key = os.getenv("MUI_API_KEY")

class HandleUserInput(BaseTool):
    """
    Capture user inputs from the chat interface. Provide appropriate responses based on the user's input.
    Ensure the conversation flow is maintained.
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
        # Define the base URL for the MUI API
        base_url = "https://api.mui.com/chat"

        # Prepare the payload for the API request
        payload = {
            "session_id": self.session_id,
            "user_input": self.user_input,
            "api_key": api_key
        }

        # Make the API request to capture user input and get a response
        response = requests.post(f"{base_url}/handle_input", json=payload)

        # Check the response status and return the result
        if response.status_code == 200:
            return response.json().get("response", "No response provided by the API.")
        else:
            return f"Failed to handle user input. Error: {response.text}"