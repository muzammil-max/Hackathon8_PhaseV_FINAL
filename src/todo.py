#!/usr/bin/env python3
import sys
import os

# Ensure project root is in path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import cli

def main():
    cli.main()

if __name__ == "__main__":
    main()