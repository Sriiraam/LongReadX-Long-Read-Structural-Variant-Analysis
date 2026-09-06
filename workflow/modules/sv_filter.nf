process SV_FILTER {

    tag "${caller}"

    cpus 1
    memory '1 GB'

    publishDir "${params.outdir}/filtered/${caller}",
        mode: 'copy',
        overwrite: true

    input:
    tuple val(caller), path(vcf)

    output:
    tuple val(caller),
          path("${caller}.filtered.vcf.gz"),
          path("${caller}.filtered.vcf.gz.tbi")

    script:
    """
    bgzip -c ${vcf} > ${caller}.raw.vcf.gz

    tabix -f -p vcf ${caller}.raw.vcf.gz

    bcftools view \
        -r ${params.region} \
        -i 'FILTER="PASS" && (INFO/SVTYPE="DEL" || INFO/SVTYPE="INS") && abs(INFO/SVLEN)>=50' \
        ${caller}.raw.vcf.gz \
        -Oz \
        -o ${caller}.filtered.vcf.gz

    tabix -f -p vcf ${caller}.filtered.vcf.gz
    """
}
