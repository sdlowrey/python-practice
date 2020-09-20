from collections import Counter
import re
import sys

path = sys.argv[1]
count = Counter(re.findall(r'\w+', open(path).read().lower()))
common = count.most_common()
print(common)
