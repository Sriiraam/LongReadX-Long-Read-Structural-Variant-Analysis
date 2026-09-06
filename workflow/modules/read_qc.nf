process READ_QC {
    tag "HG002_HiFi"

    cpus 2
    memory '2 GB'

    publishDir "${params.outdir}/qc", mode: 'copy'

    input:
    path reads

    output:
    path "read_stats.txt"

    script:
    """
    seqkit stats -a -T ${reads} > read_stats.txt
    """
}
