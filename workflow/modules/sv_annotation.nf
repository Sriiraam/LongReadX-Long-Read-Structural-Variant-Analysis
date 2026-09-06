process SV_ANNOTATION {

    tag "sniffles2"

    cpus 1
    memory '1 GB'

    publishDir "${params.outdir}/annotation",
        mode: 'copy',
        overwrite: true

    input:
    tuple val(caller),
          path(vcf),
          path(tbi)

    path genes_bed

    output:
    tuple path("annotated_structural_variants.csv"),
          path("sv_gene_overlaps.tsv")

    script:
    """
    python ${projectDir}/scripts/annotate_sv.py \
        --vcf ${vcf} \
        --out annotated_structural_variants.csv

    python ${projectDir}/scripts/make_sv_bed.py \
        --input annotated_structural_variants.csv \
        --output sv_intervals.bed

    bedtools intersect \
        -a sv_intervals.bed \
        -b ${genes_bed} \
        -wa -wb \
        > sv_gene_overlaps.tsv
    """
}
