# Let's use police pandas to do the work
import pandas as police


# run this in terminal: pip install pandas


# Read in the CSV and skip any leading rows (company name/other, but keep the headers)
original_data = police.read_csv('SampleData.csv', skiprows=2)


# ----------------------------------------------------------------------
# Let's do some pre-processing of the file and data in memory if needed
# ----------------------------------------------------------------------

# Duplicate detection if needed? # Can also check for empty cells
temp_df2 = original_data.drop_duplicates()
if temp_df2.shape[0] != original_data.shape[0]:
    print("\nDuplicates Found - We could add a print out of them? \n")
# Cleanup, since these arrays can be large, why keep them
del temp_df2

# Let's frame the data in a new framed matrix
framed_data = police.DataFrame(original_data)

# Cleanup the un-formatted data, not the file, just the in-memory stuff
del original_data
DEBUG: print(framed_data.info(), '\n')   # DEBUG: Checking the DataFrame data types
DEBUG: print(framed_data.head(3), '\n')  # DEBUG: Print out first 3 rows to check data


# ----------------------------------------------------------------------
# Now we have 1 object in memory, 'framed_data', ready for processing
# ----------------------------------------------------------------------

# Build a list of all unique CustIDs
ReducedCustIDs = framed_data['CustID']
ReducedCustIDs.drop_duplicates(inplace=True)
DEBUG: print("Number Of CustIDs with more than 1 entry: ",
             framed_data.shape[0] - ReducedCustIDs.shape[0],
             '\n\n')

# CustIDtoNameLinks[ReducedCustIDs[0:]]



revenue = framed_data['Total'].sum()


print("Total of Revenue Column: ")
print(revenue)



exit(0)