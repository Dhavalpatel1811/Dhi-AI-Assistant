# core/groq_engine.py — Groq API engine (primary)

from groq import Groq
from config import GROQ_API_KEY, GROQ_MODEL, SYSTEM_PROMPT
from tools.web_search import web_search
import json

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search the internet for current, real-time information such as stock prices, news, weather, sports scores, or recent events. Do NOT use for casual conversation or general knowledge.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "A clear and specific search query."
                    }
                },
                "required": ["query"]
            }
        }
    }
]

TOOL_MAP = {
    "web_search": web_search
}


class GroqEngine:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)
        self.model = GROQ_MODEL
        self.conversation_history = []
        self.conversation_history.append({
            "role": "system",
            "content": SYSTEM_PROMPT
        })

    def _run_tool(self, tool_name: str, tool_args: dict) -> str:
        print(f"\n⚙️  Using tool: {tool_name}")
        print(f"🔍 Query: {tool_args}\n")
        if tool_name in TOOL_MAP:
            return TOOL_MAP[tool_name](**tool_args)
        return f"Tool '{tool_name}' not found."

    def chat(self, user_input: str) -> str:
        self.conversation_history.append({
            "role": "user",
            "content": user_input
        })

        # First call — does it need a tool?
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.conversation_history,
            tools=TOOLS,
            tool_choice="auto",
            max_tokens=1024
        )

        message = response.choices[0].message

        # Tool call requested?
        if message.tool_calls:
            self.conversation_history.append({
                "role": "assistant",
                "content": message.content or "",
                "tool_calls": [
                    {
                        "id": tc.id,
                        "type": "function",
                        "function": {
                            "name": tc.function.name,
                            "arguments": tc.function.arguments
                        }
                    } for tc in message.tool_calls
                ]
            })

            for tool_call in message.tool_calls:
                try:
                    tool_name = tool_call.function.name
                    # Clean tool name — remove anything after = or space
                    tool_name = tool_name.split("=")[0].split(" ")[0].strip()

                    # Parse arguments safely
                    raw_args = tool_call.function.arguments
                    if isinstance(raw_args, str):
                        tool_args = json.loads(raw_args)
                    else:
                        tool_args = raw_args

                    tool_result = self._run_tool(tool_name, tool_args)
                    print(f"✅ Tool result received\n")

                except Exception as e:
                    print(f"⚠️ Tool execution error: {e}")
                    tool_result = f"Tool failed: {str(e)}"

                self.conversation_history.append({
                    "role": "tool",
                    "content": tool_result,
                    "tool_call_id": tool_call.id
                })

            # Second call — respond using tool results
            final_response = self.client.chat.completions.create(
                model=self.model,
                messages=self.conversation_history,
                max_tokens=1024
            )
            assistant_reply = final_response.choices[0].message.content

        else:
            assistant_reply = message.content

        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_reply
        })

        return assistant_reply