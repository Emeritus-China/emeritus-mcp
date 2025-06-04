# Emeritus MCP Server

This project is a Model Context Protocol (MCP) server implementation for the Emeritus API. It provides a standardized interface for AI models to interact with Emeritus services, including user management, tag operations, order management, and leads import.

## About Model Context Protocol (MCP)

The Model Context Protocol (MCP) is an open standard introduced by Anthropic that enables seamless integration between LLM applications and external data sources and tools. Think of MCP as a "USB-C for AI applications" - it provides a standardized way to connect AI models with external systems.

MCP uses a client-server architecture where:
- **MCP Servers** expose capabilities (tools, resources, prompts) in a standardized way
- **MCP Clients** (within AI applications) connect to these servers
- **JSON-RPC 2.0** is used for communication between clients and servers

## Features

This MCP server provides:

- **Tools**: Functions that AI models can execute to interact with Emeritus services
  - User management (create, fetch, update users)
  - Tag operations (create groups, assign tags)
  - Order management (fetch orders and financial records)
  - Leads import functionality
- **Resources**: Access to Emeritus data sources
- **Secure Authentication**: Token-based authentication with the Emeritus API
- **Error Handling**: Comprehensive error reporting and validation

## Requirements

- Python 3.10 or higher
- Access to Emeritus API credentials
- An MCP-compatible client (like Claude Desktop, or any application using MCP SDKs)

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd emeritus-mcp
```

2. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e .
```

3. Create a `.env` file based on the provided `.env.example`:

```bash
cp .env.example .env
```

4. Edit the `.env` file with your Emeritus API credentials.

## Configuration

Set the following environment variables in the `.env` file:

- `EMERITUS_API_HOST`: The Emeritus API host URL
- `EMERITUS_USER_ID`: Your Emeritus User ID
- `EMERITUS_API_SECRET`: Your Emeritus API Secret
- `DEBUG`: Set to `True` for development, `False` for production

## Usage

### Running the MCP Server

Start the server using the MCP standard way:

```bash
python -m emeritus_mcp
```

Or run directly:

```bash
python src/emeritus_mcp/server.py
```

### Connecting to the Server

This MCP server can be used with any MCP-compatible client. For example:

#### Claude Desktop

Add the server to your Claude Desktop configuration:

```json
{
  "mcpServers": {
    "emeritus": {
      "command": "python",
      "args": ["-m", "emeritus_mcp"],
      "env": {
        "EMERITUS_API_HOST": "your-api-host",
        "EMERITUS_USER_ID": "your-user-id",
        "EMERITUS_API_SECRET": "your-secret"
      }
    }
  }
}
```

#### Other MCP Clients

Use the standard MCP connection protocols (stdio, SSE) supported by your client.

## Available Tools

The server exposes the following tools that AI models can use:

### User Management
- `create_user`: Create a user by mobile number or email
- `fetch_user_profile`: Get a user's profile information
- `update_user_owner`: Update a user's owner
- `update_user_pool`: Update a user's pool
- `update_user_email`: Update a user's email
- `fetch_user_contact`: Fetch a user's contact information

### Tag Management
- `create_tag_group`: Create a tag group
- `list_tag_groups`: Get a list of tag groups
- `update_tag_group`: Update a tag group
- `deactivate_tag_group`: Deactivate a tag group
- `activate_tag_group`: Activate a tag group
- `assign_user_tag`: Assign a tag to a user
- `list_user_tags`: List tags assigned to a user

### Order Management
- `fetch_order`: Get details for a specific order
- `list_orders`: Get a list of orders
- `list_order_financials`: Get a list of order financial records

### Leads Management
- `import_leads`: Import leads from raw data

## Project Structure

```
emeritus-mcp/
├── pyproject.toml           # Project dependencies and configuration
├── README.md                # Project documentation
├── .env.example             # Example environment variables
├── src/
│   └── emeritus_mcp/        # Main package
│       ├── __init__.py      # Package initialization
│       ├── __main__.py      # CLI entry point
│       ├── server.py        # MCP server implementation
│       ├── tools/           # MCP tools implementation
│       │   ├── __init__.py
│       │   ├── user.py      # User management tools
│       │   ├── tag.py       # Tag management tools
│       │   ├── order.py     # Order management tools
│       │   └── leads.py     # Leads management tools
│       ├── services/        # Emeritus API integration
│       │   ├── __init__.py
│       │   └── emeritus_client.py
│       └── config/          # Configuration management
│           ├── __init__.py
│           └── settings.py
```

## Development

### Testing

Run tests with pytest:

```bash
pytest
```

### Code Formatting

Format code with Black and isort:

```bash
black src tests
isort src tests
```

### Type Checking

Run type checking with mypy:

```bash
mypy src
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Ensure all tests pass
6. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## More About MCP

To learn more about the Model Context Protocol:
- [Official MCP Documentation](https://modelcontextprotocol.io/)
- [MCP Specification](https://spec.modelcontextprotocol.io/)
- [Anthropic's MCP Introduction](https://www.anthropic.com/news/model-context-protocol)
