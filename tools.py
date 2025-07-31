# tools.py
import math
from langchain.tools import Tool

def calculator_tool(query: str) -> str:
    try:
        return str(eval(query, {"__builtins__": None}, math.__dict__))
    except Exception:
        return "Error: could not calculate expression."

calculator = Tool(
    name="Calculator",
    func=calculator_tool,
    description="Use this tool to evaluate math expressions."
)
