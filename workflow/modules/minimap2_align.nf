process MINIMAP2_ALIGN {
    tag "HG002_chr20"

    cpus 4
    memory '4 GB'

    publishDir "${params.outdir}/alignment", mode: 'copy'

    input:
    path reads
    path reference

    output:
    tuple path("HG002_chr20.sorted.bam"),
          path("HG002_chr20.sorted.bam.bai")

    script:
    """
    minimap2 -t ${task.cpus} -ax map-hifi ${reference} ${reads} |
        samtools sort -@ ${task.cpus} -o HG002_chr20.sorted.bam -

    samtools index -@ ${task.cpus} HG002_chr20.sorted.bam
    """
}
