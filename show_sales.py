import sys
from itertools import islice


with open('bakery.csv', 'r', encoding='utf-8') as f:
    if len(sys.argv) == 2:
        f.seek(0)
        num_start = int(sys.argv[1])
        lines = islice(f, num_start, None)
        print(*lines)

    if len(sys.argv) == 3:
        f.seek(0)
        num_start = int(sys.argv[1])
        num_end = int(sys.argv[2])+1
        lines = islice(f, num_start, num_end)
        print(*lines)
    else:
        print(f.read())

