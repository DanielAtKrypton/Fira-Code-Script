import sys, getopt
from .parse import Parse

def main(argv):
   inputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:m:",["ifile=", "mname="])
   except getopt.GetoptError:
      print('test.py -i <inputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -i <inputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-m", "--mname"):
         method_name = arg
   print ('Processing {} ...'.format(inputfile))
   parse = Parse()
   parse_method = getattr(parse, method_name)
   parse_method(inputfile.rstrip())

if __name__ == "__main__":
   main(sys.argv[1:])