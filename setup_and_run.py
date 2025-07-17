#!/usr/bin/env python3
"""
Cross-platform setup and run script for FastAPI.
Automatically detects the platform and installs appropriate dependencies.
"""

import sys
import os
import platform
import subprocess

def install_requirements():
    """Install requirements based on the current platform."""
    system = platform.system()
    
    if system == "Windows":
        requirements_file = "requirements-windows.txt"
        print(f"Detected Windows - using {requirements_file}")
    else:
        requirements_file = "requirements.txt"
        print(f"Detected {system} - using {requirements_file}")
    
    # Install requirements
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", requirements_file
        ])
        print(f"Successfully installed requirements from {requirements_file}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error installing requirements: {e}")
        return False

def setup_event_loop():
    """Setup the appropriate event loop for the current platform."""
    if platform.system() == "Windows":
        # On Windows, use the default asyncio event loop
        print("Setting up Windows-compatible event loop")
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
    """Main entry point."""
    print("Setting up FastAPI development environment...")
    
    # Install requirements
    if not install_requirements():
        print("Failed to install requirements. Exiting.")
        sys.exit(1)
    
    # Setup event loop
    setup_event_loop()
    
    # Import uvicorn after installing requirements and setting up event loop
    try:
        import uvicorn
    except ImportError:
        print("uvicorn not found. Please check your requirements installation.")
        sys.exit(1)
    
    # Start the FastAPI server
    print("Starting FastAPI server...")
    uvicorn.run(
        "api.index:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    main()
