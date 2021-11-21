#! /usr/bin/python3
import sys

def txt_to_matrix(filename):
    data = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            eachline = line.split()
            read_data = [int(x) for x in eachline]
            if read_data!= []:
                data.append(read_data)
            line = f.readline()
        return data

#print(txt_to_matrix("hw153.input"))
if __name__ == "__main__":
    start = txt_to_matrix(sys.argv[1])
    print(start)
