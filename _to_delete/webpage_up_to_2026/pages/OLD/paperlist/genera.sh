export TMPDIR=.
bibtex2html -s abbrv -nokeys -noheader -nofooter -nodoc -citefile citefile -nf pdf "pdf" biblio.bib
perl -i -pe's|March||' biblio.html
perl -i -pe's|February||' biblio.html
cp biblio.html ../publications_list.html

perl -i -pe's|biblio.html\S+"|publications.html"|;' biblio_bib.html
cp biblio_bib.html ../biblio_bib.html
