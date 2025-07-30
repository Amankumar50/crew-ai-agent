# import os
# from typing import Optional

# from crewai.tools import BaseTool
# from crewai_tools import MCPServerAdapter, ScrapeWebsiteTool, SerperDevTool


# def get_tools() -> list[BaseTool]:
#     """
#     Returns a list of tools available for the marketing posts crew.
#     """
#     if os.getenv("MCP_SERVER_URL"):
#         return _get_tools_mcp()
#     return _get_tools_crewai()


# def _get_tools_crewai() -> list[BaseTool]:
#     return [SerperDevTool(), ScrapeWebsiteTool()]


# _server: Optional[MCPServerAdapter] = None


# def _get_tools_mcp() -> list[BaseTool]:
#     global _server
#     if _server is None:
#         _server = MCPServerAdapter(dict(url=os.getenv("MCP_SERVER_URL")))
#         print(f"Available MCP tools {[tool.name for tool in _server.tools]}")
#     return _server.tools


# import os
# from typing import Optional

# from crewai.tools import BaseTool
# from crewai_tools import MCPServerAdapter, ScrapeWebsiteTool, SerperDevTool


# def get_tools() -> list[BaseTool]:
#     """
#     Returns a list of tools available for the marketing posts crew.
#     """
#     if os.getenv("MCP_SERVER_URL"):
#         return _get_tools_mcp()
#     return _get_tools_crewai()


# def _get_tools_crewai() -> list[BaseTool]:
#     print(f"🔧 Using Serper API Key: {os.getenv('SERPER_API_KEY')}")
#     return [SerperDevTool(), ScrapeWebsiteTool()]


# _server: Optional[MCPServerAdapter] = None


# def _get_tools_mcp() -> list[BaseTool]:
#     global _server
#     if _server is None:
#         _server = MCPServerAdapter(dict(url=os.getenv("MCP_SERVER_URL")))
#         print(f"Available MCP tools {[tool.name for tool in _server.tools]}")
#     return _server.tools



import os
from typing import Optional

from crewai.tools import BaseTool
from crewai_tools import MCPServerAdapter, ScrapeWebsiteTool, SerperDevTool

# Import load_dotenv here if it's not handled globally in your app startup
# from dotenv import load_dotenv
# load_dotenv() # Ensure this is called somewhere before tools are initialized

def get_tools() -> list[BaseTool]:
    """
    Returns a list of tools available for the marketing posts crew.
    """
    if os.getenv("MCP_SERVER_URL"):
        return _get_tools_mcp()
    return _get_tools_crewai()


def _get_tools_crewai() -> list[BaseTool]:
    # Retrieve the SERPER_API_KEY from environment variables
    serper_api_key = os.getenv('SERPER_API_KEY')

    # Add a check to ensure the key is present before proceeding
    if not serper_api_key:
        print("Error: SERPER_API_KEY not found in environment variables. SerperDevTool will not work.")
        # Depending on your desired behavior, you might want to raise an error
        # or return only ScrapeWebsiteTool() if Serper is optional.
        # For now, we'll try to initialize it, but it will likely fail without the key.
        # It's better to raise an exception if it's a mandatory tool.
        raise ValueError("SERPER_API_KEY is required for SerperDevTool but not found.")


    print(f"🔧 Using Serper API Key (first 5 chars): {serper_api_key[:5]}...") # Print partial for security
    
    # Pass the retrieved API key to the SerperDevTool constructor
    return [SerperDevTool(api_key=serper_api_key), ScrapeWebsiteTool()]


return_server: Optional[MCPServerAdapter] = None