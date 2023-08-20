#!/bin/bash

: '
    Title: Memory USAGE MONITORING
    AUTHOR: SAGAR UTEKAR
    DATE: 20TH AUGUST, 2023
'

function mem_stats {
    echo "........................................"
    echo "..........MEMORY USAGE.............."
    echo "........................................"
    ps -eocomm,pmem | grep -E -v '(0.0)' >> "$1".txt
}