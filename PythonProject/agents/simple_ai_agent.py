"""
Simple AI Agent with LLM
"""
from typing import Dict, Any
from openai import AzureOpenAI
from config.settings import settings


class SimpleAIAgent:
    """
    Simple AI Agent with Azure OpenAI integration
    """

    def __init__(self):
        self.client = AzureOpenAI(
            api_key="",
            api_version="2024-02-01",
            azure_endpoint="https://moshe-m6dfn51l-eastus2.services.ai.azure.com"
        )
        self.deployment_name = "gpt-4o"

    async def generate_response(self, prompt: str, context: Dict[str, Any] = None) -> str:
        """
        Generate response using LLM

        Args:
            prompt: The prompt/question to send to LLM
            context: Additional context data

        Returns:
            Generated response text
        """
        try:
            # Build the full prompt with context
            full_prompt = self._build_prompt(prompt, context)

            # Call Azure OpenAI
            response = self.client.chat.completions.create(
                model=self.deployment_name,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful AI assistant that helps users with their tasks."
                    },
                    {
                        "role": "user",
                        "content": full_prompt
                    }
                ],
                temperature=0.7,
                max_tokens=800
            )

            # Extract the response
            result = response.choices[0].message.content

            print(f"LLM Response generated successfully")
            return result

        except Exception as e:
            print(f"Error generating LLM response: {str(e)}")
            return "Sorry, I couldn't process your request at this time."

    def _build_prompt(self, prompt: str, context: Dict[str, Any] = None) -> str:
        """Build the full prompt with context"""
        if not context:
            return prompt

        context_str = "\n".join([f"{k}: {v}" for k, v in context.items()])
        return f"""Context:
{context_str}

User Request:
{prompt}

Please provide a helpful response."""


# Singleton
_simple_ai_agent = None


def get_simple_ai_agent() -> SimpleAIAgent:
    """Get or create simple AI agent singleton"""
    global _simple_ai_agent
    if _simple_ai_agent is None:
        _simple_ai_agent = SimpleAIAgent()
    return _simple_ai_agent
