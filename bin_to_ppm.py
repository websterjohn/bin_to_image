import os
import math
import sys

if len(sys.argv) < 2:
    print("usage: bin_to_ppm.py [PATH]")
    print("PATH is the path to the binary file to inspect")
    sys.exit()

input_file_path = sys.argv[1]

input_file = open(input_file_path,"rb")
output_file = open('output.ppm', 'w')
file_array = []
pixels_written = 0

file_size = os.path.getsize(input_file_path)
width = 300
height = math.ceil(file_size/width)

output_file.write("P3 \n")#header
output_file.write(str(width) + " ")#width
output_file.write(str(height) + " \n")#height
output_file.write("255 \n")

byte = input_file.read(1) #get first byte
while byte: 
    x = str(int.from_bytes(byte, "big")) #endianness doesn't matter 
    output_file.write(x + " " + x + " " + x + " \n")
    pixels_written = pixels_written + 1
    byte = input_file.read(1) #get next byte

while pixels_written < (height * width): #finish up the grid
    output_file.write("0  0  0 \n")
    pixels_written = pixels_written + 1