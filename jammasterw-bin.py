#!/usr/bin/python

import sys
import jammasterw

def run_at_build_time():
    sys.stderr.write("run_at_build_time!\n")

def run_at_run_time():
    sys.stderr.write("run_at_run_time!\n")

if __name__ == "__main__":
    jammasterw.add_build_method(run_at_build_time)
    jammasterw.add_run_method(run_at_run_time)
    jammasterw.main()
