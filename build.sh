#!/bin/bash
cd rosters
for i in *.html
do
if [ "$i" != "index.html" ]
then
gnome-web-print -m print --file "$i" "../pdf/$i.pdf"
fi
done
cd ../pdf
pdfunite *.pdf out
mv out ../rosters.pdf