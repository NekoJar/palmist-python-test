#!/usr/bin/env python3
"""
Windows-compatible FastAPI startup script.
This script handles platform-specific configurations and gracefully handles uvloop on Windows.
"""

import sys
import os
import platform

def setup_event_loop():
    """Setup the appropriate event loop for the current platform."""
    if platform.system() == "Windows":
        # On Windows, use the default asyncio event loop
        print("Running on Windows - using default asyncio event loop")
        import asyncio
        if hasattr(asyncio, 'WindowsProactorEventLoopPolicy'):
            asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    else:
        # On Unix-like systems, try to use uvloop for better performance
        try:
            import uvloop
            uvloop.install()
            print("Using uvloop for enhanced performance")
        except ImportError:
            print("uvloop not available, using default asyncio event loop")

def main():
    """Main entry point for starting the FastAPI server."""
    setup_event_loop()
    
    # Import uvicorn after setting up the event loop
    import uvicorn
    
    # Start the FastAPI server
    uvicorn.run(
        "api.index:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    main()
