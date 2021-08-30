# Pretends to run rosetta

import sys
import os
import time

# Prints contents of filename, replacing keys in d with values in d
def output(filename, d):
  f = open(filename)
  for line in f:
    for p, v in d.items():
      if p in line:
        if not os.path.exists(v):
          print('[ ERROR ] File: ' + v + ' not found!')
          if is_abinitio:
            print('AN INTERNAL ERROR HAS OCCURED. PLEASE SEE THE CONTENTS OF ROSETTA_CRASH.log FOR DETAILS.')
            crash_f = open('ROSETTA_CRASH.log', 'a')
            crash_f.write(time.ctime(time.time()) + '\n')
            crash_f.write('[ ERROR ] File: ' + v + ' not found!\n\n')
            crash_f.close()
          return
        line = line.replace(p, v)
    if '/home/angelica' in line:
      line = line.replace('/home/angelica', os.path.expanduser('~') + '/compbio-badges/badge-hs')
    print(line.strip())
  if is_abinitio:
    os.system('cp ~/compbio-badges/badge-hs/rosetta/main/source/.out/1elw_fold_silent.out .')
    os.system('mv 1elw_fold_silent.out ' + d['/home/angelica/trash/1elw_fold_silent.out'])
    os.system('cp ~/compbio-badges/badge-hs/rosetta/main/source/.out/score.fsc .')
  if is_silent:
    os.system('cp ~/compbio-badges/badge-hs/rosetta/main/source/.out/S_00000001.pdb .')
  return

# extract_pdbs or AbinitioRelax?
is_silent = False
is_abinitio = False
if sys.argv[1] == 'silent':
  is_silent = True
elif sys.argv[1] == 'abinitio':
  is_abinitio = True

if is_abinitio:

  # Opens flags file
  try:
    flags = open(sys.argv[2])
  except:
    print('Option file open failed for: ' + sys.argv[2])
    sys.exit()

  # Maps my input/output file paths to theirs
  paths = dict()
  paths['/home/angelica/trash/flags'] = sys.argv[2]
  for line in flags:
    if line.strip().startswith('-database'):
      paths['/home/angelica/rosetta/main/database'] = line.strip().split('-database')[1].strip()
    elif line.strip().startswith('-in:file:native'):
      paths['/home/angelica/trash/1elw.pdb'] = line.strip().split('-in:file:native')[1].strip()
    elif line.strip().startswith('-in:file:fasta'):
      paths['/home/angelica/trash/rcsb_pdb_1ELW.fasta'] = line.strip().split('-in:file:fasta')[1].strip()
    elif line.strip().startswith('-in:file:frag3'):
      paths['/home/angelica/trash/aat000_03_05.200_v1_3'] = line.strip().split('-in:file:frag3')[1].strip()
    elif line.strip().startswith('-in:file:frag9'):
      paths['/home/angelica/trash/aat000_09_05.200_v1_3'] = line.strip().split('-in:file:frag9')[1].strip()
    elif line.strip().startswith('-psipred_ss2'):
      paths['/home/angelica/trash/t000_.psipred_ss2'] = line.strip().split('-psipred_ss2')[1].strip()
    elif line.strip().startswith('-out:file:silent'):
      paths['/home/angelica/trash/1elw_fold_silent.out'] = line.strip().split('-out:file:silent')[1].strip()

  flags.close()

  # Prints abinitio output message, replacing my paths with theirs
  outf_name = os.path.expanduser('~') + '/compbio-badges/badge-hs/rosetta/main/source/.out/abinitio_out.txt'
  output(outf_name, paths)

if is_silent:

  # Maps my input/output file paths to theirs
  paths = dict()
  paths['trash/1elw_fold_silent.out'] = sys.argv[2].strip()

  # Prints output message of extracting silent file, replacing my paths with theirs
  outf_name = os.path.expanduser('~') + '/compbio-badges/badge-hs/rosetta/main/source/.out/silent_out.txt'
  output(outf_name, paths)
