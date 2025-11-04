# InfiniteARC: API

An auto-generated repository containing a growing collection of synthetic 
ARC-style task generators and solvers.

A dataset containing the tasks in JSON format, including metadata, can be 
found on HuggingFace at [conor99/InfiniteARC](https://huggingface.co/datasets/conor99/InfiniteARC).

## Usage

```
git clone https://github.com/conor-99/InfiniteARC-API.git --depth 1
```

```python
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from infinitearc.task_list import task_list

tasks = task_list()
generate, p = tasks["46ff664a"]

example = generate()
grid_in, grid_out_gen = example["input"], example["output"]
grid_out_sol = p(grid_in)
```
