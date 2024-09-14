# Command Used to create the file
ls *.xml > list
for i in `cat list`; do cp "$i" "$i".bak ; done

# This one lists the files in /sbin that are just plain text files, and possibly scripts:
for i in `ls /sbin`; do file /sbin/$i | grep ASCII; done
