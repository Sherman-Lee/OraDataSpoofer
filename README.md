# OraDataSpoofer

OraDataSpoofer allows you to mock structured data and download them as csv in seconds

  - Supported Data Types so far: Strings, Floats, Ints, Dates, Emails, Zip Codes

### Prerequisites
  - Python 3.7
  - numpy 1.15.1
  - pandas 0.23.4

### How to install and run
To install, open your terminal window and run the following commands:
```
git clone https://github.com/Sherman-Lee/OraDataSpoofer.git
```

To run, run these commands inside the OraDataSpoofer directory:
```
cd OraDataSpoofer
python gui.py
```
### How to use
1. Put your desired name of the data column into "FieldName".
2. Choose the type of the data column with the radio button.
3. Enter the values for "Min" and "Max", which represents the range that OraDataSpoofer will randomize data from.  For example, entering a "Min" of 0 and a "Max" of 100 means that the app will randomly pick 100 different values for the particular data column.  "Min" must be greater than or equal to zero.
4. Enter the values for "Dictionary" if desired, which is used for the "Strings" data type ONLY.  Enter one value per line in the text area, and the total number of values must be greater than the previous value of "Max".  If no values are entered in the text area, OraDataSpoofer will choose strings from a default nounlist for generation.
5. Click "Add Field" to confirm column.  You will see the confirmed column details below if successful.
6. Iterate thru step 1 to step 5 until all columns are confirmed.
7. Enter the value for "Number of records" to decide the number of rows to be generated after all columns are added for confirmation.
8. Click "Next" to generate the data.  Output will be saved as "output.csv" in the project directory

###Notes
- Dates are generated with a random base date from 2010-01-01, in the format of YYYY-MM-DD
- Emails are generated with a random alphanumeric string and a @ora.com ending
- Zips are generated with a random five-digit format from 00000 to 99999
- Value of "Number of records" must be greater than value of "Max"
    
### To Do
- Specific statistic distributions of data
- More data types
- More application features
- Containerize it
- Tests

Let me know what kinds of improvements you would like!
