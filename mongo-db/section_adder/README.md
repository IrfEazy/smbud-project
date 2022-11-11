# Section Adder
Adds an array of sections object to the papers dataset

## Dependency
Run this script with python3

## Usage
python3 section_adder.py IN_FILE [OUT_FILE]

The parameters in [...] are optional

IN_FILE: the file from which the data will be read (the papers dataset) to add the sections
OUT_FILE: the file where to save the newly modified data of IN_FILE

If OUT_FILE is not given then IN_FILE will be overriden

## Section object structure
{
    title: string,
    paragraphs: [string],
    subsections: [ {title: string,
    		    paragraphs: [string]}
		 ]
}
