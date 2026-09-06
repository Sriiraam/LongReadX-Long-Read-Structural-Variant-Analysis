process BAM_QC {
    tag "HG002_chr20"

    cpus 2
    memory '2 GB'

    publishDir "${params.outdir}/bam_qc", mode: 'copy'

    input:
    tuple path(bam), path(bai)

    output:
    path "flagstat.txt"
    path "alignment_stats.txt"
    path "coverage.txt"

    script:
    """
    samtools quickcheck -v ${bam}

    samtools flagstat -@ ${task.cpus} ${bam} > flagstat.txt

    samtools stats -@ ${task.cpus} ${bam} > alignment_stats.txt

    samtools coverage \
        -r chr20:20000001-40000000 \
        ${bam} > coverage.txt
    """
}
