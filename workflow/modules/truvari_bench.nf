process TRUVARI_BENCH {

    tag "${caller}"

    cpus 1
    memory '2 GB'

    publishDir "${params.outdir}/benchmarking/${caller}",
        mode: 'copy',
        overwrite: true

    input:
    tuple val(caller),
          path(call_vcf),
          path(call_tbi)

    tuple path(truth_vcf),
          path(truth_tbi),
          path(benchmark_bed),
          path(reference),
          path(ref_fai)

    output:
    tuple val(caller),
          path("${caller}.summary.json"),
          path("${caller}.tp-base.vcf.gz"),
          path("${caller}.tp-comp.vcf.gz"),
          path("${caller}.fp.vcf.gz"),
          path("${caller}.fn.vcf.gz")

    script:
    """
    rm -rf truvari_out

    truvari bench \
        -b ${truth_vcf} \
        -c ${call_vcf} \
        -f ${reference} \
        --includebed ${benchmark_bed} \
        -o truvari_out

    cp truvari_out/summary.json ${caller}.summary.json
    cp truvari_out/tp-base.vcf.gz ${caller}.tp-base.vcf.gz
    cp truvari_out/tp-comp.vcf.gz ${caller}.tp-comp.vcf.gz
    cp truvari_out/fp.vcf.gz ${caller}.fp.vcf.gz
    cp truvari_out/fn.vcf.gz ${caller}.fn.vcf.gz
    """
}
