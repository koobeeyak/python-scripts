import sys,csv

# Merchant category codes (MCCs) are four digit codes used by credit card companies
# They are used to classify and define different types of business
# This script can be used to quickly get information about any particular cc
 
# USAGE: python define_mcc.py 4821
# TO BE USED with mcc_codes.csv in the same directory

def make_dictionary(file):
    """
    Use csv.reader to parse mcc csv file.
    We're interested in the mcc code, description, and category (if it exists).
    Let's make a dictionary of these.
    """
    with open(file,'rU') as infile:
        mcc_csv = csv.reader(infile)
        mcc_dict = {}
        first_row_skipped = False
        for row in mcc_csv:
            if not first_row_skipped: #labels are in first row of csv
                first_row_skipped = True
                continue
            mcc,description=int(row[0]),row[1]
            if row[4]: #not all mccs have a category
                category=row[4]
            else:
                category=None
            mcc_dict[mcc] = {'description':description,'category':category}
    return mcc_dict

def search_and_print_dictionary(d, number):
    """
    Search dictionary for mcc number.
    Print mcc information.
    """
    code = int(number)
    if code in d.keys():
        description=d[code]['description']
        if d[code]['category']:
            category=d[code]['category']
        else:
            category = False
        if category:
            print 'MCC %s is %s of category %s'% (code,description,category)
        else:
            print 'MCC %s is %s'% (code,description)
    else:
        no_value = 'MCC not found'
        print no_value

if __name__=="__main__":
    mccs=make_dictionary('mcc_codes.csv')
    desc=search_and_print_dictionary(mccs,sys.argv[1])
