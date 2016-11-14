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

bad_records_but_from_0 = \
    """left	right	node	children	time	population
0.000000	0.398041    7	0,2	    0.000000	0
0.398041	0.894875	7	2,8	    0.000000	0
0.894875	1.000000	6	0,2	    0.000000	0
0.398041	0.894875	6	0,9     0.000000	0
0.000000	0.478687	5	1,3	    0.000000	0
0.478687	0.481614	5	3,10    0.000000	0
0.481614	1.000000	4	1,3	    0.000000	0
0.478687	0.481614	4	1,10    0.000000	0
"""

good_but_no_zero = \
    """left	right	node	children	time	population
0.000000	0.390000	3	1,2	0.000000	0
0.390000	1.000000	4	1,2	0.000000	0
"""
good = \
    """left	right	node	children	time	population
0.000000	0.390000	2	0,1	0.000000	0
0.390000	1.000000	3	0,1	0.000000	0
"""

records = {'redundant_records': bad_records,
           'redundant_records_but_from_zero': bad_records_but_from_0,
           'simple_records_but_dont_start_at_zero': good_but_no_zero,
           'simple_records': good
           }

def main(key=None):
    for desc, recs in records.items():
        try:
            with tempfile.NamedTemporaryFile(mode='w') as f:
                f.writelines(recs)
                f.flush()
                ts = msprime.load_txt(f.name)
            print(desc, ">> can load")
            if key is not None and desc == key:
                return(ts)
            try:
                for t in ts.trees():
                    pass
                print(desc, ">> can iterate over trees")
            except Exception as e:
                print("!",  desc, "<< FAILS to iterate over trees")
                print("   raises:", e)
                print("The trees were:")
                for t in trees(list(ts.records())):
                    print(t)
        except IndexError as ie:
            print("! Causes IndexError in trees.py")
            print(ie)
        except Exception as e:
            print("!", desc, "<< FAILS to load")
            print(e)
        print("\n")

if __name__ == "__main__":
    main()
