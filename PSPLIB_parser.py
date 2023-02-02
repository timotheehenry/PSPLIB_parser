# =========================================================================
# based on code from source: https://www.gams.com/latest/gamslib_ml/libhtml/gamslib_rcpsp.html
# =========================================================================

def ints(strs): return [ int(s) for s in strs ]

#def myset(prefix, cardinality):
#    return [f'{prefix}{i+1}' for i in range(cardinality)]

def myset(cardinality):
  return list(range(1, cardinality + 1))

def index_of_line(lines, substr):
    return next(i for i,line in enumerate(lines) if substr in line)

def rhs_part(lines, prefix):
    return lines[index_of_line(lines, prefix)].split(':')[1]

#def succs_from_line(line): return [ f'j{j}' for j in line.split()[3:] ]

def succs_from_line(line): return [ int(j) for j in line.split()[3:] ]

def column(lines, col, rowStart, rowCount):
    return [int(lines[rowIx].split()[col]) for rowIx in range(rowStart, rowStart+rowCount)]


def PSPLIB_parser(filepath):
  # --------------------------------
  # Python parser for PSPLIB files
  # input: filepath to PSPLIB file
  # output: lists of all the data
  #         in following order:
  #         njobs, nperiods, jobs, res, periods, succs, durations, demands, capacities
  # --------------------------------
  with open(filepath) as fp: lines = fp.readlines()
  
  njobs = int(rhs_part(lines, 'jobs (incl. supersource'))
  
  nres = int(rhs_part(lines, '- renewable').split()[0])
  nperiods = int(rhs_part(lines, 'horizon'))
  prec_offset = index_of_line(lines, 'PRECEDENCE RELATIONS:')+2
  attrs_offset = index_of_line(lines, 'REQUESTS/DURATIONS')+3
  caps_offset = index_of_line(lines, 'RESOURCEAVAILABILITIES')+2
  
  #jobs, res, periods = myset('j', njobs), myset('r', nres), myset('t', nperiods)
  jobs, res, periods = myset(njobs), myset(nres), myset(nperiods)
  
  succs = { j: succs_from_line(lines[prec_offset+ix]) for ix,j in enumerate(jobs) }
  durations = column(lines, 2, attrs_offset, njobs)
  demands = [ ints(lines[ix].split()[3:]) for ix in range(attrs_offset, attrs_offset+njobs) ]
  capacities = ints(lines[caps_offset].split())
  
  return (njobs, nres, nperiods, jobs, res, periods, succs, durations, demands, capacities)


