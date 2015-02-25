#!/bin/bash
cd rosters
rm *.pdf
for i in *.html
do
if [ "$i" != "index.html" ]
then
gnome-web-print -m print --file "$i" "$i".pdf
fi
done
pdfunite *.pdf out
rm *.pdf
mv out ../rosters.pdf