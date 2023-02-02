# PSPLIB_parser

PSPLIB is a library a standard way to define RCPSP (resource constrained project scheduling problems).
More information here: https://www.om-db.wi.tum.de/psplib/library.html

Data files can be found here:
https://www.om-db.wi.tum.de/psplib/data.html

How to use the PSPLIB_parser:

```
# read the parser code
filename = "PSPLIB_parser.py"
exec(open(filename).read())

# get path to the PSPLIB input file
filepath = "j301_1.sm"
njobs, nres, nperiods, jobs, res, periods, succs, durations, demands, capacities = PSPLIB_parser(filepath)

print(njobs, nperiods)
print(jobs, res, periods)
print(succs, durations, demands, capacities)
```

