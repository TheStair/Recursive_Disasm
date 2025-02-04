#Author TheStair
#Recursive Descent Disassembler for x86 ELF binaries

import pandas as pd
import numpy as np
import os
import sys
import pyelftools as elftools
import argparse


#Define Data Structures


#Specific structure of Dataframe created by chatGPT
instruct_frame = pd.DataFrame([
    {"address": 0x1000, "opcode": "MOV", "target": "EAX", "source": "EBX"},
    {"address": 0x1004, "opcode": "ADD", "target": "EAX", "source": "5"},
    {"address": 0x1008, "opcode": "JMP", "target": 0x2000, "source": None},
])


#Just an idea, I may make it where each instruction is listed instead of just start 
# and end

function_frame = pd.DataFrame([
    {"address": 0x1000, "func_start": 0x1000, "func_end": 0x100F,},
])

bb_frame = pd.DataFrame([
    {"bbid": 0, "bb_start": 0x1000, "bb_end": 0x1003},
])

#Define Data
file_header = ""
section_headers = ""
symbol_table = ""
relocation_table = ""
instruction_table = ""

entry_point = 0x00000000

disassembly = ""



#Define Functions
def disassemble():
    return 0

def parse_elf():
    return 0

def parse_section_headers():
    return 0

def parse_symbol_table():
    return 0

def assign_symbols():
    return 0



#Ideas for options, output to file, output to terminal (default),
# I was using argparse, but I think I will use argparse instead.
# It sets up a switch case for the options and makes it simple to add more
#main
def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Disassembler script.")

    # Add arguments
    parser.add_argument("input_file", type=str, help="Path to the binary file to disassemble")
    parser.add_argument("-o", "--output", type=str, help="Output file to save disassembly results")

    # Parse arguments
    args = parser.parse_args()

    if args.output:
        print(f"Saving output to: {args.output}")

        with open(args.output, "w") as f:
            f.write("Disassembly output goes here...")  # Replace with actual disassembly data

    else:
        print("Printing disassembly to console:")
        print(disassembly)  # or df.print() instructions