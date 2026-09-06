#!/usr/bin/env python3

import argparse
import pandas as pd

p = argparse.ArgumentParser()
p.add_argument("--input", required=True)
p.add_argument("--output", required=True)
args = p.parse_args()

df = pd.read_csv(args.input)

with open(args.output, "w") as f:
    for i, r in df.iterrows():
        start = max(int(r["pos"]) - 1, 0)
        end = max(int(r["end"]), start + 1)

        f.write(
            f'{r["chrom"]}\t{start}\t{end}\t{i}\t'
            f'{r["svtype"]}\t{r["svlen"]}\n'
        )
