#this is the file that actually does the formatting

from pytest import main

from arithmetic_arranger import arithmetic_arranger

#for a person who doesnt code this might look a little blursed but it's not much
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))


# Run unit tests automatically
main(['-vv'])
