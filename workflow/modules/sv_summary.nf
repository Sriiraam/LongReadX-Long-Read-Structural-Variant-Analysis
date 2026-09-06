process SV_SUMMARY {

    tag "final_sv_summary"

    cpus 1
    memory '1 GB'

    publishDir "${params.outdir}/summary",
        mode: 'copy',
        overwrite: true

    input:
    tuple path(annotated_csv),
          path(overlaps_tsv)

    path benchmark_csv

    output:
    path "longreadx_structural_variants.csv"
    path "sv_type_summary.csv"
    path "gene_overlap_summary.csv"
    path "longreadx.db"

    script:
    """
    mkdir -p summary_out

    python ${projectDir}/scripts/build_sv_summary.py \
        --sv ${annotated_csv} \
        --overlaps ${overlaps_tsv} \
        --benchmark ${benchmark_csv} \
        --outdir summary_out \
        --database summary_out/longreadx.db

    cp summary_out/longreadx_structural_variants.csv .
    cp summary_out/sv_type_summary.csv .
    cp summary_out/gene_overlap_summary.csv .
    cp summary_out/longreadx.db .
    """
}
