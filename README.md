# IU Graduate Programs MCP Server

A lightweight MCP (Model Context Protocol) server that provides official webpage URLs and contact page links for Indiana University graduate schools. Designed to work alongside ChatAIU's knowledge sources as a supplement.

## Architecture

- **Knowledge sources** (trained URLs in ChatAIU) handle content questions (program details, courses, requirements)
- **This MCP server** handles structured link data (program page URLs, contact/admissions page URLs)
- ChatAIU's LLM invokes both as needed and merges results into a single response

## Tools

| Tool | Purpose | When LLM invokes it |
|------|---------|-------------------|
| `get_program_links` | Returns official program page URL for a school | Student asks about programs, degrees, courses, curriculum |
| `get_contact_info` | Returns official contact/admissions page URL | Student asks about applications, deadlines, requirements, fees, contacts |

## Setup

### Prerequisites
- Python 3.10 or higher
- pip

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run locally

```bash
python server.py
```

The server starts on `http://localhost:8000` with SSE transport.

### Run tests

```bash
python -m pytest tests/ -v
```

### Test with MCP Inspector

```bash
npx @modelcontextprotocol/inspector
```

Then connect to `http://localhost:8000/sse` and test the tools interactively.

## Production deployment

For production, use uvicorn directly:

```bash
uvicorn server:app --host 0.0.0.0 --port 8000
```

### Deploy to Render

1. Push this repo to GitHub
2. Create a new Web Service on Render
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `uvicorn server:app --host 0.0.0.0 --port $PORT`
5. Copy the public URL and configure it in ChatAIU

## ChatAIU Configuration

1. Go to **Settings > AI Agents > +Add**
2. Set Agent Type: **MCP Server Agent**
3. Set Name: **Graduate Programs Link Assistant**
4. Set Description: *Provides official webpage URLs and contact page links for all 15 Indiana University graduate schools. Use this agent to supply students with direct links to program pages, admissions contacts, and school directories. Does not answer content questions directly; the knowledge source handles that.*
5. Set Endpoint: `https://mcpserver-fvod.onrender.com/sse` 
6. Set Status: **Active**
7. Link the agent to your project in **Project Setup > Linked Agents**

## Project structure

```
iu-grad-mcp-server/
|-- server.py           # MCP server with tool definitions
|-- schools.py          # School data (names, keywords, URLs)
|-- matching.py         # Keyword -> school lookup logic
|-- requirements.txt    # Python dependencies
|-- README.md           # This file
|-- tests/
|   |-- test_matching.py   # Unit tests for school matching
|   |-- test_tools.py      # Unit tests for tool responses
```

## Adding or updating schools

Edit `schools.py`:
- To add a school: append a new dictionary to the `SCHOOLS` list
- To update a URL: edit the `program_url` or `contact_url` field
- To add keywords: append to the school's `keywords` list

No ChatAIU reconfiguration needed -- just redeploy the server.

## Supported schools (15)

1. Hamilton Lugar School of International Studies
2. Luddy School of Informatics, Computing, and Engineering
3. Kelley School of Business
4. College of Arts and Sciences
5. Eskenazi School of Art, Architecture + Design
6. Jacobs School of Music
7. Maurer School of Law
8. O'Neill School of Public and Environmental Affairs
9. School of Education
10. School of Medicine
11. School of Nursing
12. School of Optometry
13. School of Public Health
14. School of Social Work
15. The Media School
