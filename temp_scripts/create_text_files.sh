#!/bin/bash
filesPath="/home/vlad/Documents/Repo/python_string-search/text_sources"
for i in {1..2}; do
  cat $filesPath/vardai-pavardes.txt >> $filesPath/vardai-pavardes_x2.txt
  cat $filesPath/wiki-straipsnis.txt >> $filesPath/wiki-straipsnis_x2.txt
  cat $filesPath/wiki-kvant-teorija_2.txt >> $filesPath/wiki-kvant-teorija_x2.txt
done

for i in {1..4}; do
  cat $filesPath/vardai-pavardes.txt >> $filesPath/vardai-pavardes_x4.txt
  cat $filesPath/wiki-straipsnis.txt >> $filesPath/wiki-straipsnis_x4.txt
  cat $filesPath/wiki-kvant-teorija_2.txt >> $filesPath/wiki-kvant-teorija_x4.txt
done

for i in {1..10}; do
  cat $filesPath/vardai-pavardes.txt >> $filesPath/vardai-pavardes_x10.txt
  cat $filesPath/wiki-straipsnis.txt >> $filesPath/wiki-straipsnis_x10.txt
  cat $filesPath/wiki-kvant-teorija_2.txt >> $filesPath/wiki-kvant-teorija_x10.txt
done

for i in {1..20}; do
  cat $filesPath/vardai-pavardes.txt >> $filesPath/vardai-pavardes_x20.txt
  cat $filesPath/wiki-straipsnis.txt >> $filesPath/wiki-straipsnis_x20.txt
  cat $filesPath/wiki-kvant-teorija_2.txt >> $filesPath/wiki-kvant-teorija_x20.txt
done

for i in {1..50}; do
  cat $filesPath/vardai-pavardes.txt >> $filesPath/vardai-pavardes_x50.txt
  cat $filesPath/wiki-straipsnis.txt >> $filesPath/wiki-straipsnis_x50.txt
  cat $filesPath/wiki-kvant-teorija_2.txt >> $filesPath/wiki-kvant-teorija_x50.txt
done

for i in {1..100}; do
  cat $filesPath/vardai-pavardes.txt >> $filesPath/vardai-pavardes_x100.txt
  cat $filesPath/wiki-straipsnis.txt >> $filesPath/wiki-straipsnis_x100.txt
  cat $filesPath/wiki-kvant-teorija_2.txt >> $filesPath/wiki-kvant-teorija_x100.txt
done