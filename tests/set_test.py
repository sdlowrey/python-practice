from timeit import Timer

t = Timer('len(needles & haystack)',
          setup='needles = set(range(1000)); haystack = set(range(10**6))')
t.repeat()
