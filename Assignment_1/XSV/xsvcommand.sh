#xsv headers command
xsv headers cs-training.csv
xsv headers cs-test.csv

#xsv statistics command
xsv stats cs-training.csv --everything | xsv table
xsv stats cs-test.csv --everything | xsv table
