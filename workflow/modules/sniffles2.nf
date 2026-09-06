process SNIFFLES2 {

    tag "HG002_chr20"

    cpus 4
    memory '3 GB'

    publishDir "${params.outdir}/sv_calls/sniffles2",
        mode: 'copy',
        overwrite: true

    input:
    tuple path(bam), path(bai)
    tuple path(reference), path(fai)

    output:
    path "HG002_sniffles2.vcf"

    script:
    """
    sniffles \
        --input ${bam} \
        --vcf HG002_sniffles2.vcf \
        --reference ${reference} \
        --threads ${task.cpus} \
        --minsvlen 50
    """
}
