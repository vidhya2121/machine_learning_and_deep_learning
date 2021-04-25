# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:48:26 2021

@author: vidhya
"""
import re

format_pat= re.compile(
    r"(?P<host>[\d\.]+)\s"
    r"(?P<identity>\S*)\s"
    r"(?P<user>\S*)\s"
    r"\[(?P<time>.*?)\]\s"
    r'"(?P<request>.*?)"\s'
    r"(?P<status>\d+)\s"
    r"(?P<bytes>\S*)\s"
    r'"(?P<referer>.*?)"\s'
    r'"(?P<user_agent>.*?)"\s*'
)

log_path = "access_log.txt"

url_counts = {}
c = 1

with open(log_path, "r") as f:
    for line in f:
        match = format_pat.match(line)
        if match:
            access = match.groupdict()
            agent = access['user_agent']
            if (not('bot' in agent or 'spider' in agent or
                    'Bot' in agent or 'Spider' in agent or
                    'W3 Total Cache' in agent or agent == '-')):
                request = access['request']
                fields = request.split()
                if (len(fields) == 3):
                    (action, url, protocaol) = fields
                    if (url.endswith("/") and "/feed" not in url):
                        if action == 'GET':
                            if url in url_counts:
                                url_counts[url] = url_counts[url] + 1
                            else:
                                url_counts[url] = 1
                                
results = sorted(url_counts, key=lambda i: int(url_counts[i]), reverse=True)

for result in results[:20]:
    print(result + ": " , url_counts[result])
