# Windows Setup Guide

This project has been configured to work on Windows by resolving the `uvloop` compatibility issue.

## What was implemented:

### 1. Platform-specific requirements
- **requirements.txt**: Modified to conditionally install uvloop only on non-Windows systems
- **requirements-windows.txt**: Windows-specific requirements file without uvloop

### 2. Cross-platform startup scripts
- **setup_and_run.py**: Automatically detects platform and uses appropriate requirements
- **start_fastapi.py**: Windows-compatible FastAPI startup with proper event loop setup
- **run_fastapi.bat**: Windows batch file for easy execution

### 3. Updated package.json
- Modified to use `python` instead of `python3` for Windows compatibility
- Uses the new cross-platform setup script

## Running the application:

### Option 1: Full development environment (recommended)
```bash
npm run dev
```
This starts both Next.js frontend and FastAPI backend concurrently.

### Option 2: FastAPI only
```bash
python setup_and_run.py
```
or
```bash
npm run fastapi-dev
```

### Option 3: Manual setup
```bash
npm run fastapi-dev-manual
```

## Servers:
- **Next.js Frontend**: http://localhost:3001 (or 3000 if available)
- **FastAPI Backend**: http://127.0.0.1:8000

## Key changes made:

1. **requirements.txt line 37**: 
   ```
   uvloop==0.19.0; sys_platform != "win32"
   ```

2. **api/index.py**: Added fallback to load .env file:
   ```python
   load_dotenv(".env.local")
   load_dotenv(".env")
   ```

3. **Event loop handling**: Automatically uses Windows-compatible asyncio event loop

## Troubleshooting:

If you encounter issues:
1. Ensure Python is in your PATH
2. Try running `python setup_and_run.py` directly
3. Check that your OpenAI API key is set in `.env` file
4. Use `requirements-windows.txt` directly if needed:
   ```bash
   pip install -r requirements-windows.txt
   ```
