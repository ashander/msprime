import tempfile
import msprime
from trees import trees

bad_records = \
    """left	right	node	children	time	population
0.000000	0.398041	8	1,3	    0.000000	0
0.398041	0.894875	8	3,9	    0.000000	0
0.894875	1.000000	7	1,3	    0.000000	0
0.398041	0.894875	7	1,10    0.000000	0
0.000000	0.478687	6	2,4	    0.000000	0
0.478687	0.481614	6	4,11    0.000000	0
0.481614	1.000000	5	2,4	    0.000000	0
0.478687	0.481614	5	2,11    0.000000	0
"""

good_records = \
    """left	right	node	children	time	population
0.000000	0.390000	3	1,2	0.000000	0
0.390000	1.000000	4	1,2	0.000000	0
0.390000	0.481614	5	1,2	0.000000	0
"""

if __name__ == "__main__":
    with tempfile.NamedTemporaryFile(mode='w') as f:
        f.writelines(bad_records)
        f.flush()
        ts_bad = msprime.load_txt(f.name)

    with tempfile.NamedTemporaryFile(mode='w') as f:
        f.writelines(good_records)
        f.flush()
        ts_good = msprime.load_txt(f.name)

    for t in trees(list(ts_good.records())):
        print(t)
