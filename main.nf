nextflow.enable.dsl=2

include { READ_QC } from './workflow/modules/read_qc'
include { MINIMAP2_ALIGN } from './workflow/modules/minimap2_align'
include { BAM_QC } from './workflow/modules/bam_qc'

include { SNIFFLES2 } from './workflow/modules/sniffles2'
include { CUTESV } from './workflow/modules/cutesv'

include { SV_FILTER as FILTER_SNIFFLES2 } from './workflow/modules/sv_filter'
include { SV_FILTER as FILTER_CUTESV } from './workflow/modules/sv_filter'

include { TRUVARI_BENCH as TRUVARI_SNIFFLES2 } from './workflow/modules/truvari_bench'
include { TRUVARI_BENCH as TRUVARI_CUTESV } from './workflow/modules/truvari_bench'

include { BENCHMARK_SUMMARY } from './workflow/modules/benchmark_summary'
include { SV_ANNOTATION } from './workflow/modules/sv_annotation'
include { SV_SUMMARY } from './workflow/modules/sv_summary'


params.reads = 'data/raw/HG002_HiFi_chr20_20M_40M.fastq.gz'

params.reference = 'data/reference/GRCh38_chr20.fa'
params.ref_fai = 'data/reference/GRCh38_chr20.fa.fai'

params.truth_vcf = 'data/truth/region/HG002_chr20_20M_40M.truth.vcf.gz'
params.truth_tbi = 'data/truth/region/HG002_chr20_20M_40M.truth.vcf.gz.tbi'

params.benchmark_bed = 'data/truth/region/HG002_chr20_20M_40M.benchmark.bed'

params.genes_bed = 'data/reference/annotation/gencode_chr20_genes.bed'

params.region = 'chr20:20000001-40000000'
params.outdir = 'results'


workflow {

    /*
     * INPUT CHANNELS
     */

    reads_qc_ch = Channel.fromPath(
        params.reads,
        checkIfExists: true
    )

    reads_align_ch = Channel.fromPath(
        params.reads,
        checkIfExists: true
    )

    reference_align_ch = Channel.fromPath(
        params.reference,
        checkIfExists: true
    )

    reference_bundle_ch = Channel.value([
        file(params.reference),
        file(params.ref_fai)
    ])

    truth_bundle_ch = Channel.value([
        file(params.truth_vcf),
        file(params.truth_tbi),
        file(params.benchmark_bed),
        file(params.reference),
        file(params.ref_fai)
    ])

    genes_bed_ch = Channel.fromPath(
        params.genes_bed,
        checkIfExists: true
    )


    /*
     * READ QC
     */

    READ_QC(
        reads_qc_ch
    )


    /*
     * ALIGNMENT
     */

    aligned = MINIMAP2_ALIGN(
        reads_align_ch,
        reference_align_ch
    )


    /*
     * BAM QC
     */

    BAM_QC(
        aligned
    )


    /*
     * SV CALLING
     */

    sniffles_raw = SNIFFLES2(
        aligned,
        reference_bundle_ch
    )

    cutesv_raw = CUTESV(
        aligned,
        reference_bundle_ch
    )


    /*
     * SV FILTERING
     */

    sniffles_filtered = FILTER_SNIFFLES2(
        sniffles_raw.map { vcf ->
            tuple('sniffles2', vcf)
        }
    )

    cutesv_filtered = FILTER_CUTESV(
        cutesv_raw.map { vcf ->
            tuple('cutesv', vcf)
        }
    )


    /*
     * TRUVARI BENCHMARK
     */

    sniffles_bench = TRUVARI_SNIFFLES2(
        sniffles_filtered,
        truth_bundle_ch
    )

    cutesv_bench = TRUVARI_CUTESV(
        cutesv_filtered,
        truth_bundle_ch
    )


    /*
     * BENCHMARK SUMMARY
     */

    benchmark_summary_out = BENCHMARK_SUMMARY(
        sniffles_bench,
        cutesv_bench
    )


    /*
     * PRIMARY SV ANNOTATION
     */

    annotation_out = SV_ANNOTATION(
        sniffles_filtered,
        genes_bed_ch
    )


    /*
     * FINAL STRUCTURED DATASET + SQLITE
     */

    SV_SUMMARY(
        annotation_out,
        benchmark_summary_out
    )
}
