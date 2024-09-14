#!/bin/bash
# specific conversion script for my html files to php
LIST="$(ls *.html)"
for i in "$LIST"; do
	NEWNAME=$(ls "$i" | sed -e 's/html/php')
	cat beginfile > "$NEWNAME"
	cat $i" | sed -e '1,25d' | tac | sed -e '1,21d' | tac >> "$NEWNAME"
	cat endfile >> "$NEWNAME"
done
