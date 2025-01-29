import urllib.request
import json
import os
import ssl
from typing import Dict, Optional


class RAGClient:
    def __init__(self, endpoint_url: str, api_key: str):
        """Initialize the RAG client.

        Args:
            endpoint_url (str): The Azure endpoint URL
            api_key (str): The API key for authentication
        """
        self.endpoint_url = endpoint_url
        self.api_key = api_key
        self._setup_ssl()

    def _setup_ssl(self):
        """Setup SSL context for self-signed certificates."""
        if not os.environ.get("PYTHONHTTPSVERIFY", "") and getattr(
            ssl, "_create_unverified_context", None
        ):
            ssl._create_default_https_context = ssl._create_unverified_context

    def ask_question(self, question: str, **kwargs) -> Dict:
        """Send a question to the RAG endpoint.

        Args:
            question (str): The question to ask
            **kwargs: Additional parameters to pass to the endpoint

        Returns:
            Dict: The parsed JSON response

        Raises:
            Exception: If the request fails
        """
        # Prepare the request data
        data = {"question": question, **kwargs}

        # Encode the request body
        body = str.encode(json.dumps(data))

        # Setup headers
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

        # Create the request
        req = urllib.request.Request(self.endpoint_url, body, headers)

        try:
            # Send the request
            response = urllib.request.urlopen(req)
            result = response.read()

            # Parse and return the response
            return json.loads(result)

        except urllib.error.HTTPError as error:
            error_message = f"""
            Request failed with status code: {error.code}
            Headers: {error.info()}
            Response: {error.read().decode("utf8", "ignore")}
            """
            raise Exception(error_message)


def main():
    # Example usage
    endpoint_url = (
        "https://brochure-flow-endpoint.swedencentral.inference.ml.azure.com/score"
    )
    api_key = "aVQq5YMzUvoc4HjSa2QsfkwaT5yfCyy4"

    # Create the client
    rag_client = RAGClient(endpoint_url, api_key)

    # Example questions to test
    questions = [
        "propose please some hotels in dubai",
        "what are the best attractions in dubai?",
        "tell me about transportation in dubai",
    ]

    # Test each question
    for question in questions:
        print(f"\nQuestion: {question}")
        try:
            response = rag_client.ask_question(question)
            print("Response:", json.dumps(response, indent=2))
        except Exception as e:
            print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
