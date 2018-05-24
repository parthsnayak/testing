import sys

check = sys.argv[0]

if ( type(check) == "str" ):
    print "What you entered is string"
else:
  print( "What you enteres is not a string! " )
