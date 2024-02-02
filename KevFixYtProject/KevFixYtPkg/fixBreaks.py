'''
Created on Jan 25, 2024

@author: billw
'''
import os
import re

    
def replace_br_in_csv(input_path, output_path) -> str:
    rowCommentCounts = []
    commentIndex = 9 # Excel column J
    with open(input_path, 'r', newline='\n', errors='backslashreplace' ) as ytFile:
        print(ytFile.name)
        with open(output_path, 'w') as fixedFile:
            rawYT = ytFile.readlines()
            # print(f"{len(rawYT)} lines read.")
            matchIt = '\r<br>'
            for i, line in enumerate(rawYT):
                if 0 == i:
                    continue
                line = line[:-1]
                fixedYT = line.replace(matchIt," ").replace("<br>", " ").replace("</br>", " ").replace("&#39","'")
                fixedYT = re.sub(r'(\\x[0-9a-fA-F])','?', fixedYT)
                parts = fixedYT.split(",")
                if commentIndex + 1 < len(parts):
                    parts[commentIndex] = ",".join(parts[commentIndex:])
                comment = parts[commentIndex]
                commentWords = re.findall(r'([a-zA-Z]+)', comment)
                commentWordsCount = str(len(commentWords))
                commentCount = str(len(comment))
                fileParts = ytFile.name.split(os.sep)
                commentRow = '\t'.join([fileParts[-1], comment, commentCount, commentWordsCount])
                rowCommentCounts.append(commentRow) 
                trimParts = parts[:10]
                trimParts.append(commentCount)
                tabIt = '\t'.join(trimParts) + '\n'
                fixedFile.writelines(tabIt)
    # print(f"Finished fixing {ytFile.name} \n\tLines read: \t{len(rawYT)} \n\tLines fixed: \t{linesFixed} ")
    return rowCommentCounts

# Replace 'source_folder' and 'output_folder' with your actual folder paths
source_folder = r'E:\YTapi-Combo_PreClean' 
# source_folder = 'E:\LINEBREAKER\Test-Files'
# output_folder = r'E:\LINEBREAKER\1-15_LoFi-Scrape_BR-remove' 
output_folder = r'E:\AllRun'
countsFile = r'E:\ytCounts.tsv'
# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each CSV file in the source folder
commentLines = []
for filename in os.listdir(source_folder):
    if filename.endswith('.csv'):
        input_path = os.path.join(source_folder, filename)
        output_path = os.path.join(output_folder, filename.replace(".csv",".tsv"))
        commentLines += replace_br_in_csv(input_path, output_path)
with open(countsFile, 'w') as countDetails:
    commentId = 0
    for commentLine in commentLines:
        commentId += 1
        commentLine = '\t'.join([str(commentId), commentLine])
        countDetails.writelines(f"{commentLine}\n")
print("Finished Fixing Files")
