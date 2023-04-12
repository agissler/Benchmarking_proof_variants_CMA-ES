    #!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Launcher for any number of batches.

Example to launch 8 batches::

    python launch.py example_experiment2.py budget_multiplier=3 8

executes::

    nohup nice python -u example_experiment2.py budget_multiplier=3 batch=i/8

for ``i in range(8)``.

After that::

    ps ax -o  uid,uname,pid,ni,%mem,%cpu,time,etime,pid,cmd | sort -n  | tail -n 33

shows running processes.

"""
from __future__ import division, print_function, unicode_literals
del division, print_function, unicode_literals

import os, sys

def cmd(s):
    print(s)
    os.system(s)  # comment for dry run

if __name__ == "__main__":
    python_name = 'python'  # './python' + os.getcwd()[-3:]
    script_name = "../%s/%s" % (os.path.split(os.getcwd())[-1], sys.argv[1])
    # cmd("cp -p %s %s" % (sys.executable, python_name))  # only to show different names in top

    if sys.argv[1].startswith('experiment.py'):
        if len(sys.argv) < 3:
            raise ValueError("need at least python file and number of batches as argument")
        batches = int(sys.argv[-1])  # last arg is number of batches

        for i in range(batches):
            cmd(("nohup nice %s -u %s " % (python_name, script_name)) +
                ' '.join(sys.argv[2:-1]) +
                ' batch=%d/%d > out.txt%d 2> err.txt%d &' % (i, batches, i, i)
                )
    else:
        print("command file %s not found" % sys.argv[1])

