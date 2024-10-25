#!/usr/bin/python3
"""READ from stdin."""
import sys
import signal

def handle_signal(signum, frame):
    """handle the controle C signal."""

    total_size = 0
    ttp_status = {}
    for i in range(0, 11):
        for line in sys.stdin:
            line_split = line.split()

            if len(line_split) == 9:
                try:
                    code = int(line_split[-2])
                    total_size += int(line_split[-1])
                    if code in http_status:
                        http_status[code] = int(http_status[code]) + 1
                    else:
                        http_status[code] = 1
                except Exception:
                    pass
    print(f"File size: {total_size}")
    for key, val in http_status.items():
        print(f"{key}: {val}")



signal.signal(signal.SIGINT, handle_signal)

total_size = 0
i = 0

http_status = {}
for line in sys.stdin:
    line_split = line.split()

    if len(line_split) == 9:
        try:
            code = int(line_split[-2])
            total_size += int(line_split[-1])
            if code in http_status:
                http_status[code] = int(http_status[code]) + 1
            else:
                http_status[code] = 1
        except Exception:
            pass
    
    i += 1

    if i == 10:
        i = 0
        print(f"File size: {total_size}")
        for key, val in http_status.items():
            print(f"{key}: {val}")
