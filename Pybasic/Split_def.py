import sys
import json

def split_patent(input_file, out_file):
    try:
        with open(input_file, 'r') as p_data, open(out_file, 'w') as s_data:
            # Write the header line
            s_data.write("Application_Number|Filing_Date|Publication_Date|Grant_Date|Priority_Date\n")

            # Process each row in the input file
            for p_entry in p_data:
                # Parse JSON data
                patent = json.loads(p_entry)

                # Extract information from each row
                application_number = patent.get('application_number', '').strip()
                filing_date = patent.get('filing_date', '').strip()
                publication_date = patent.get('publication_date', '').strip()
                grant_date = patent.get('grant_date', '').strip()
                priority_date = patent.get('priority_date', '').strip()

                # Write data to the output file
                line_data = f"{application_number}|{filing_date}|{publication_date}|{grant_date}|{priority_date}\n"
                s_data.write(line_data)

        print(f"Data successfully extracted and written to {out_file}")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <output_file> <input_file>")
    else:
        output_file = sys.argv[1]
        input_file = sys.argv[2]
        split_patent(input_file, output_file)
