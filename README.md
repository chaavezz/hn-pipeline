JSON Headlines Pipeline

Python tool that scrapes Hacker News headlines and generates a structured report.

Features

* Scrapes headlines from Hacker News
* Processes data in memory (no intermediate JSON needed)
* Ranks longest titles
* Generates TXT report
* CLI arguments support

Usage

Run with default values:

python main.py

Run with custom options:

python main.py –top 5
python main.py –output myreport.txt
python main.py –top 3 –output custom.txt

Arguments

–top
Number of longest titles to include (default: 2)

–output
Name of the output file (default: report.txt)

Tech

* Python
* requests
* BeautifulSoup
* argparse