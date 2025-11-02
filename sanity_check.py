import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from infinitearc.task_list import task_list

tasks = task_list()
generate, p = tasks["46ff664a"]

example = generate()
grid_in, grid_out_gen = example["input"], example["output"]
grid_out_sol = p(grid_in)

assert grid_out_gen == grid_out_sol
