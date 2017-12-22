#!/bin/sh
rm -rf Mooduino
curl -l -k https://codeload.github.com/cratrifork/Mooduino/zip/master > archive.zip
unzip archive.zip -d .
mv Mooduino-master Mooduino
rm -f archive.zip