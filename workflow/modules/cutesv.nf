process CUTESV {

    tag "HG002_chr20"

    cpus 4
    memory '3 GB'

    publishDir "${params.outdir}/sv_calls/cutesv",
        mode: 'copy',
        overwrite: true

    input:
    tuple path(bam), path(bai)
    tuple path(reference), path(fai)

    output:
    path "HG002_cutesv.vcf"

    script:
    """
    mkdir -p cutesv_tmp

    cuteSV \
        ${bam} \
        ${reference} \
        HG002_cutesv.vcf \
        cutesv_tmp \
        --threads ${task.cpus} \
        --min_size 50 \
        --genotype
    """
}
