FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

# System bioinformatics stack
# cuteSV remains in Ubuntu's compatible Python/NumPy environment
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    minimap2 \
    samtools \
    bcftools \
    tabix \
    bedtools \
    cutesv \
    wget \
    curl \
    gzip \
    && rm -rf /var/lib/apt/lists/*

# Separate modern Python environment for
# Sniffles2 + Truvari + LongReadX Python utilities
RUN python3 -m venv /opt/longreadx

RUN /opt/longreadx/bin/pip install --upgrade pip setuptools wheel && \
    /opt/longreadx/bin/pip install \
        sniffles==2.8.0 \
        truvari==5.4.0 \
        pandas \
        pysam \
        pytest

ENV PATH="/opt/longreadx/bin:${PATH}"

WORKDIR /workspace

CMD ["/bin/bash"]
