# Emeritus MCP Server

This project is an MCP (Microservice Control Platform) server implementation for the Emeritus API. It provides a standardized interface to interact with Emeritus services, including user management, tag operations, order management, and leads import.

## Features

- **Authentication**: Secure token-based authentication with the Emeritus API
- **User Management**: Create, fetch, and update user information
- **Tag Management**: Create, manage, and assign tags to users
- **Order Management**: Fetch order details and lists, including financial records
- **Leads Management**: Import leads from raw data
- **MCP API**: RESTful API endpoints with standardized response format
- **Error Handling**: Comprehensive error handling and reporting

## Requirements

- Python 3.10 or higher
- uv package manager (for Python dependency management)
- mcp-sdk >= 1.2.0

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd emeritus-mcp
```

2. Create a virtual environment and install dependencies using uv (Python package manager):

```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e .
```

3. Create a `.env` file based on the provided `.env.example`:

```bash
cp .env.example .env
```

4. Edit the `.env` file with your Emeritus API credentials and MCP settings.

## Configuration

The following environment variables need to be set in the `.env` file:

- `EMERITUS_API_HOST`: The Emeritus API host URL
- `EMERITUS_USER_ID`: Your Emeritus User ID
- `EMERITUS_API_SECRET`: Your Emeritus API Secret
- `MCP_API_KEY`: Your MCP API Key for client authentication
- `DEBUG`: Set to `True` for development, `False` for production

## Usage

### Running the Server

Start the server with uvicorn (not to be confused with uv, which is the package manager):

```bash
uvicorn emeritus_mcp.main:app --reload
```

The server will be available at `http://localhost:8000`.


### Authentication

All API endpoints require authentication using a Bearer token:

```
Authorization: Bearer <MCP_API_KEY>
```

## API Endpoints

### User Endpoints

- `POST /api/v5/entity/user/create`: Create a user by mobile number or email
- `GET /api/v5/entity/profile/fetch`: Get a user's profile information
- `POST /api/v5/entity/user/owner/update`: Update a user's owner
- `POST /api/v5/entity/user/pool/update`: Update a user's pool
- `POST /api/v5/entity/user/email/update`: Update a user's email
- `GET /api/v5/entity/user/contact/fetch`: Fetch a user's contact information

### Tag Endpoints

- `POST /api/v5/entity/tags/group/create`: Create a tag group
- `GET /api/v5/entity/tags/group/list`: Get a list of tag groups
- `POST /api/v5/entity/tags/group/update`: Update a tag group
- `POST /api/v5/entity/tags/group/deactivate`: Deactivate a tag group
- `POST /api/v5/entity/tags/group/activate`: Activate a tag group
- `POST /api/v5/entity/user/tags/assign`: Assign a tag to a user
- `GET /api/v5/entity/user/tags/list`: List tags assigned to a user

### Order Endpoints

- `GET /api/v5/entity/order/fetch`: Get details for a specific order
- `GET /api/v5/entity/order/list`: Get a list of orders
- `GET /api/v5/entity/order/financial/list`: Get a list of order financial records

### Leads Endpoints

- `POST /api/v5/entity/leads/import`: Import leads from raw data

## Project Structure

```
emeritus-mcp/
├── pyproject.toml        # Project dependencies and configuration
├── README.md             # Project documentation
├── .env.example          # Example environment variables
├── src/
│   └── emeritus_mcp/     # Main package
│       ├── __init__.py   # Package initialization
│       ├── main.py       # FastAPI application
│       ├── api/          # API endpoints
│       │   ├── __init__.py
│       │   ├── router.py # Main API router
│       │   └── v5/       # V5 API endpoints
│       │       ├── __init__.py
│       │       ├── user.py       # User endpoints
│       │       ├── tag.py        # Tag endpoints
│       │       ├── order.py      # Order endpoints
│       │       └── leads.py      # Leads endpoints
│       ├── auth/         # Authentication utilities
│       ├── config/       # Configuration settings
│       ├── models/       # Data models
│       ├── services/     # Service layer
│       └── utils/        # Utility functions
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

## License

This project is licensed under the MIT License - see the LICENSE file for details.
