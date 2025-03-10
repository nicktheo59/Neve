"""
Base Tool module for the Neve framework.

This module contains base classes for tools:
- BaseTool: Abstract base class for all tools
- ToolResult: Standardized container for tool results
- ToolCollection: Utility for managing collections of tools
"""

from Neve.tools.base.tool import BaseTool
from Neve.tools.base.tool_result import ToolResult
from Neve.tools.base.tool_collection import ToolCollection

__all__ = ["BaseTool", "ToolResult", "ToolCollection"] 