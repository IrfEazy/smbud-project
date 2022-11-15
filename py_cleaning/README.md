# Global cleaner
Applies all the cleaning operation emerged in neo4j and MongoDB

## Dependency
Run this script with python3  

Download the Reviews.csv dataset from https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews and put it in the data directory.  

## Usage
python3 main.py IN_FILE [OUT_FILE]  

The parameters in [...] are optional  

IN_FILE: the file from which the data will be read (the papers dataset) to add the sections  
OUT_FILE: the file where to save the newly modified data of IN_FILE  

If OUT_FILE is not given then IN_FILE will be overriden
