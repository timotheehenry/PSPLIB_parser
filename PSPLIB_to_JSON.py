# =============
# Test of PSPLIB Python parser
# =============
import json

filename = "PSPLIB_parser.py"
exec(open(filename).read())

filepath = "j1201_1.sm"
njobs, nres, nperiods, jobs, res, periods, succs, durations, demands, capacities = PSPLIB_parser(filepath)


# convert to json
jsonStr = json.dumps(jobs)

aList = {'njobs': njobs, 
          'nres': nres,
          'nperiods': nperiods,
          'periods': periods,
            'jobs': jobs,
            'res': res,
            'durations': durations,
            'succs': succs,
            'demands': demands,
            'capacities': capacities
            }
jsonStr = json.dumps(aList)
print(jsonStr)

