# PC Cleaner

A simple but effective PC cleaning utility that helps remove temporary and unwanted files from your Windows system.

## Features

- Cleans Windows temporary folders
- Cleans Windows Prefetch files
- Removes empty directories
- Generates detailed logs of cleaning operations
- Shows human-readable file size statistics
- Tracks number of files cleaned and space freed

## Requirements

- Windows operating system
- Python 3.x
- Administrator privileges (recommended for full access to system files)

## How to Use

1. Right-click on `pc_cleaner.py` and select "Run as administrator" (recommended)
2. Alternatively, double-click the file to run with normal user privileges
3. The program will automatically start cleaning temporary files
4. A summary will be displayed showing the number of files removed and space freed
5. Check `cleaner_log.txt` for detailed information about the cleaning process

## Safety Features

- Focuses only on known temporary file locations
- Logs all operations for review
- Provides warning when running without admin privileges

## Note

It's recommended to close all applications before running the cleaner to ensure temporary files can be properly removed.
