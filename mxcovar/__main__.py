#!/usr/bin/env python

"""Python 3 
"""

import argparse
import sys 

def ParseArgs(args=None):
    if args is None:
        args = sys.argv[1:]
        
    parser = argparse.ArgumentParser(description='Process VCF file(s) and build covariance matrices ready for use with MetaXcan')
    parser.add_argument("--vcf", type=argparse.FileType('r'), help='Single VCF file')
    parser.add_argument("--pop", '-p', type=argparse.FileType('r'), help='Text file with IDs to be kept for the final matrices')
    parser.add_argument("db", type=argparse.FileType('r'), nargs='+', help='One or more MetaXcan DB files to be used locus filtering')
    
    args = parser.parse_args()
    
    print(args)
    
ParseArgs()