# test_setup.py
"""Test script to verify your environment is working"""
import sys
print(f"Python version: {sys.version}")
try:
    import pandas as pd
    print("✓ pandas installed")
except ImportError:
    print("✗ pandas NOT installed")

try:
    import matplotlib
    print("✓ matplotlib installed")
except ImportError:
    print("✗ matplotlib NOT installed")

print("Next: Run 'pip install -r requirements.txt' to install packages")

