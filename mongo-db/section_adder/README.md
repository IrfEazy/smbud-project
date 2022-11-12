# Section Adder
Adds an array of sections object to the papers dataset  

## Dependency
Run this script with python3  

Download the Reviews.csv dataset from https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews and put it in the data directory.  

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
        figures: [ {URL: string,
                caption:string}
            ]
        subsections: [ {title: string,
        		    paragraphs: [string],
    		    figures: [{URL: string, caption: string}
    		],
        figures: [{URL: string, caption: string}]
    
    }

## Descritpion
The **Reviews.csv** has this schema:  

Id | ProductId | UserId | ProfileName | HelpfulnessNumerator | HelpfulnessDenominator | Score | Time | Summary | Text  

The field  `title` of our object structure is the `Summary` in the csv, while the `paragraphs` are obtained by the  
`Text` field in the csv.
