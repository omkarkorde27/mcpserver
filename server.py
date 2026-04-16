"""
IU Graduate Programs MCP Server

A lightweight MCP server that provides official webpage URLs and contact
page links for Indiana University graduate schools. Designed to work
alongside ChatAIU's knowledge sources as a supplement, not a replacement.

The knowledge sources handle content questions (program details, courses,
requirements). This server handles structured link data (program page URLs,
contact/admissions page URLs).

Transport: SSE (Server-Sent Events) over HTTP
Framework: FastMCP (official Python MCP SDK)

Usage:
    Development:  python server.py
    Production:   uvicorn server:app --host 0.0.0.0 --port 8000
"""

from mcp.server.fastmcp import FastMCP
from schools import SCHOOLS, FALLBACK_URL
from matching import find_school, find_multiple_schools
from starlette.routing import Route
from starlette.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


mcp = FastMCP(
    "IU Graduate Programs",
    host="0.0.0.0",
    port=10000,
    allowed_hosts=["mcpserver-1-2ico.onrender.com", "localhost", "127.0.0.1"],
    instructions=(
        "Provides official webpage URLs and contact page links for all 15 "
        "Indiana University graduate schools. Use this server to supply "
        "students with direct links to program pages and admissions contacts."
    ),
)

async def health(request):
    return JSONResponse({"status": "ok"})


@mcp.tool()
def get_program_links(school_name: str) -> str:
    """Returns the official graduate programs webpage URL for an Indiana
    University school. Use this to provide students with a direct link
    to explore program details, degree options, and curriculum information
    on the school's website.

    Args:
        school_name: Name or keyword identifying the school.
                     Examples: "Luddy", "Kelley", "Data Science",
                     "Business", "O'Neill", "Public Health"
    """
    # Check if query might reference multiple schools
    schools = find_multiple_schools(school_name)

    if not schools:
        return (
            f"Could not identify a specific IU school from '{school_name}'.\n"
            f"IU Graduate Programs: {FALLBACK_URL}"
        )

    if len(schools) == 1:
        school = schools[0]
        return (
            f"{school['full_name']}\n"
            f"Graduate Programs: {school['program_url']}"
        )

    # Multiple schools matched
    lines = ["Here are the program pages for the schools mentioned:\n"]
    for school in schools:
        lines.append(f"{school['full_name']}")
        lines.append(f"{school['program_url']}\n")
    return "\n".join(lines)


@mcp.tool()
def get_contact_info(school_name: str) -> str:
    """Returns the official contact and admissions page URL for an Indiana
    University school. Use this when a student needs to reach the school
    directly about applications, deadlines, requirements, fees, or any
    admissions-related questions.

    Args:
        school_name: Name or keyword identifying the school.
                     Examples: "Luddy", "Kelley", "Law",
                     "Nursing", "Maurer", "MBA"
    """
    # Check if query might reference multiple schools
    schools = find_multiple_schools(school_name)

    if not schools:
        return (
            f"Could not identify a specific IU school from '{school_name}'.\n"
            f"IU Graduate Admissions: {FALLBACK_URL}"
        )

    if len(schools) == 1:
        school = schools[0]
        return (
            f"{school['full_name']}\n"
            f"Contact/Admissions: {school['contact_url']}"
        )

    # Multiple schools matched
    lines = ["Here are the contact pages for the schools mentioned:\n"]
    for school in schools:
        lines.append(f"{school['full_name']}")
        lines.append(f"{school['contact_url']}\n")
    return "\n".join(lines)


class HostRewriteMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        request.scope["headers"] = [
            (b"host", b"localhost") if k == b"host" else (k, v)
            for k, v in request.scope["headers"]
        ]
        return await call_next(request)

app = mcp.sse_app()
app.add_middleware(HostRewriteMiddleware)


if __name__ == "__main__":
    mcp.run(transport="sse")
