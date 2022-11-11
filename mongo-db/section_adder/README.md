# Section Adder
Adds an array of sections object to the papers dataset

## Usage
Run this script with python3

section_adder papers_dataset_file_name [out_file]

The parameters in [...] are optional

## Section object structure
{
    title: string,
    paragraphs: [string],
    subsections: 
	[
	    {
		title: string,
		paragraphs: [string]
	    }
	]
}
