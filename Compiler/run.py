from generator import compile
import sys

f = open("final_result.txt", 'w')
sys.stdout = f

compile()

f.close
