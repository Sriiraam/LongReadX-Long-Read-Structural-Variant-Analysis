#!/usr/bin/env python3

import argparse
import csv
import pysam


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--vcf", required=True)
    p.add_argument("--out", required=True)
    return p.parse_args()


def main():
    args = parse_args()
    vcf = pysam.VariantFile(args.vcf)

    with open(args.out, "w", newline="") as f:
        w = csv.writer(f)

        w.writerow([
            "chrom",
            "pos",
            "end",
            "svtype",
            "svlen",
            "filter",
            "genotype",
            "support"
        ])

        for rec in vcf.fetch():
            svtype = rec.info.get("SVTYPE", ".")
            svlen = rec.info.get("SVLEN")

            if isinstance(svlen, tuple):
                svlen = svlen[0]

            if svlen is None:
                svlen = rec.stop - rec.pos

            genotype = "."

            if rec.samples:
                sample = next(iter(rec.samples.values()))
                gt = sample.get("GT")
                if gt:
                    genotype = "/".join(
                        "." if x is None else str(x)
                        for x in gt
                    )

            support = (
                rec.info.get("SUPPORT")
                or rec.info.get("RE")
                or rec.info.get("DV")
                or "."
            )

            filt = ";".join(rec.filter.keys()) if rec.filter.keys() else "."

            w.writerow([
                rec.chrom,
                rec.pos,
                rec.stop,
                svtype,
                abs(int(svlen)),
                filt,
                genotype,
                support
            ])


if __name__ == "__main__":
    main()
