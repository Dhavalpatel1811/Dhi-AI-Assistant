# core/agent.py — The agent that decides which tool to use

import json
import ollama
from config import MODEL_NAME, SYSTEM_PROMPT
from tools.web_search import web_search


# Define available tools for the LLM
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search the internet for ONLY current, real-time information such as stock prices, news, weather, sports scores, or recent events. Do NOT use this for casual conversation or general knowledge.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "A clear and specific search query. For stock prices include the word 'stock price today'. For news include 'latest' or 'today'."
                    }
                },
                "required": ["query"]
            }
        }
    }
]

# Map tool names to actual Python functions
TOOL_MAP = {
    "web_search": web_search
}


class Agent:
    def __init__(self):
        self.model = MODEL_NAME
        self.conversation_history = []
        self.conversation_history.append({
            "role": "system",
            "content": SYSTEM_PROMPT
        })

    def _run_tool(self, tool_name: str, tool_args: dict) -> str:
        """Execute the tool and return its result."""
        print(f"\n⚙️  Using tool: {tool_name}")
        print(f"🔍 Query: {tool_args}\n")
        if tool_name in TOOL_MAP:
            result = TOOL_MAP[tool_name](**tool_args)
            return result
        return f"Tool '{tool_name}' not found."

    def _is_raw_json(self, text: str) -> bool:
        """Check if model returned raw JSON instead of calling the tool properly."""
        if not text:
            return False
        stripped = text.strip()
        return stripped.startswith('{"name"') or stripped.startswith("{'name'")

    def chat(self, user_input: str) -> str:
        # Add user message
        self.conversation_history.append({
            "role": "user",
            "content": user_input
        })

        # First LLM call — decide if tool is needed
        response = ollama.chat(
            model=self.model,
            messages=self.conversation_history,
            tools=TOOLS
        )

        message = response["message"]
        content = message.get("content", "") or ""

        # Fix: detect raw JSON bug and handle gracefully
        if self._is_raw_json(content):
            print("⚠️  Raw JSON detected — fixing response...\n")
            try:
                parsed = json.loads(content.replace("'", '"'))
                tool_name = parsed.get("name", "")
                tool_args = parsed.get("parameters", {})
                # Clean up args if nested
                if "query" in tool_args and isinstance(tool_args["query"], dict):
                    tool_args["query"] = tool_args["query"].get("description", user_input)
                if tool_name in TOOL_MAP:
                    tool_result = self._run_tool(tool_name, tool_args)
                    self.conversation_history.append({
                        "role": "tool",
                        "content": tool_result
                    })
                    final_response = ollama.chat(
                        model=self.model,
                        messages=self.conversation_history
                    )
                    assistant_reply = final_response["message"]["content"]
                    self.conversation_history.append({
                        "role": "assistant",
                        "content": assistant_reply
                    })
                    return assistant_reply
            except Exception:
                pass

        # Normal tool call flow
        if message.get("tool_calls"):
            self.conversation_history.append(message)

            for tool_call in message["tool_calls"]:
                tool_name = tool_call["function"]["name"]
                tool_args = tool_call["function"]["arguments"]

                tool_result = self._run_tool(tool_name, tool_args)
                print(f"✅ Tool result received\n")

                self.conversation_history.append({
                    "role": "tool",
                    "content": tool_result
                })

            # Second LLM call — respond using tool results
            final_response = ollama.chat(
                model=self.model,
                messages=self.conversation_history
            )
            assistant_reply = final_response["message"]["content"]

        else:
            # No tool needed — normal reply
            assistant_reply = content

        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_reply
        })

        return assistant_reply