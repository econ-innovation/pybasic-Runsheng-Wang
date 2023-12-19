# Split the patent data

import json

out_file = 'split100.txt'
input_file = 'google100.txt'

with open(input_file, 'r') as p_data, open(out_file, 'w') as s_data:

    # write the title of top
    s_data.write("Applicatin_Number|Filing_Date|Publication_Date|Grant_Date|Priority_Date\n ")

    # loop to read each row of input file
    for p_entry in p_data:

        # transform into json
        patent = json.loads(p_entry)

        # extract info from each row
        application_number = patent.get('application_number').strip()
        filing_date = patent.get('filing_date', '').strip()
        publication_date = patent.get('publication_date', '').strip()
        grant_date = patent.get('grant_date', '').strip()
        priority_date = patent.get('priority_date', '').strip()

        # write in output file
        tempdata = f"{application_number}|{filing_date}|{publication_date}|{grant_date}|{priority_date}\n"
        s_data.write(tempdata)



