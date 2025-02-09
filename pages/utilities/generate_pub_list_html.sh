export TMPDIR=.

JOURNALSYEARS=(2024 2023 2022 2020 2019 2018 2017 2016 2015 2014 2013 2012 2011 2010 2009 2008)
CONFERENCESYEARS=(2025 2024 2023 2022 2021 2020 2019 2018 2017 2016 2015 2014 2013 2012 2008 2007 2006 2005 2004)
TECHREPYEARS=(2021 2020 2019 2018 2017 2016 2015 2013 2012 2009 2007 2006)

for i in ${JOURNALSYEARS[*]}; do 
	./bib2bib --no-comment -oc ZZ/trash -ob "ZZ/journals$i.bib" -c "year=$i" journals.bib;
	./bibtex2html -s abbrv -nobibsource -nokeys -noheader -nofooter -nodoc -citefile citefileWEB -nf url "link" -nf pdf "pdf" -nf code "code" -nf pdfsup "supplementary material" -nf award "Best Paper Award" "ZZ/journals$i.bib";
done
for i in ${CONFERENCESYEARS[*]}; do 
	./bib2bib --no-comment -oc ZZ/trash -ob "ZZ/conferences$i.bib" -c "year=$i" conferences.bib;
	./bibtex2html -s abbrv -nobibsource -nokeys -noheader -nofooter -nodoc -citefile citefileWEB -nf url "link" -nf pdf "pdf" -nf code "code" -nf pdfsup "supplementary material" -nf award "Best Paper Award" "ZZ/conferences$i.bib";
done    
./bibtex2html -s abbrv -nokeys -nobibsource -noheader -nofooter -nodoc -citefile citefileWEB -nf url "link" -nf pdf "pdf" -nf code "code" discussions.bib
#for i in ${TECHREPYEARS[*]}; do 
#	bib2bib --no-comment -oc ZZ/trash -ob "ZZ/techrep$i.bib" -c "year=$i" techrep.bib;
#	bibtex2html -s abbrv -nokeys -noheader -nofooter -nodoc -citefile citefileWEB -nf pdf "pdf" -nf code "code" -nf pdfsup "supplementary material" -nf award "Best Paper Award" "ZZ/techrep$i.bib";
#done    
./bibtex2html -s abbrv -nokeys -nobibsource -noheader -nofooter -nodoc -citefile citefileWEB -nf url "link" -nf pdf "pdf" -nf code "code" theses.bib
# bibtex2html -s abbrv -nokeys -noheader -nofooter -nodoc -citefile citefileWEB -nf pdf "pdf" -nf code "code" magazines.bib








# # bibtex2html -s abbrv -nokeys -noheader -nofooter -nodoc -citefile citefileWEB -nf pdf "pdf" -nf code "code" -nf pdfsup "supplementary material" -nf award "Best Paper Award" journals.bib
# # bibtex2html -s abbrv -nokeys -noheader -nofooter -nodoc -citefile citefileWEB -nf pdf "pdf" -nf code "code" conferences.bib
# # bibtex2html -s abbrv -nokeys -noheader -nofooter -nodoc -citefile citefileWEB -nf pdf "pdf" -nf code "code" discussions.bib
# # bibtex2html -s abbrv -nokeys -noheader -nofooter -nodoc -citefile citefileWEB -nf pdf "pdf" -nf code "code" techrep.bib
# # bibtex2html -s abbrv -nokeys -noheader -nofooter -nodoc -citefile citefileWEB -nf pdf "pdf" -nf code "code" theses.bib
# # bibtex2html -s abbrv -nokeys -noheader -nofooter -nodoc -citefile citefileWEB -nf pdf "pdf" -nf code "code" magazines.bib


echo \<b id=\"journals\"\>Journals\<\/b\>\<ul\> >publications_list.html
for i in ${JOURNALSYEARS[*]}; do 
	echo \<div class=\"strikethrough\"\>$i\<\/div\> >>publications_list.html
	perl -pe's|<p>|<li><p>|' journals$i.html >>publications_list.html
done
# echo \<br\> \<a class\=\"note\" href\=\"http\:\/\/dx.doi.org\/10.1016\/j.patcog.2010.08.001\" target\=\"\_blank\"\>This paper has been chosen to be the best paper published in 2008 in the journal Pattern Recognition\<\/a\> >>publications_list.html
echo \<\/ul\> >>publications_list.html

echo \<b id=\"conferences\"\>Conferences\<\/b\>\<ul\> >>publications_list.html
for i in ${CONFERENCESYEARS[*]}; do 
  echo \<div class=\"strikethrough\"\>$i\<\/div\> >>publications_list.html
	perl -pe's|<p>|<li><p>|' conferences$i.html >>publications_list.html
done
echo \<\/ul\> >>publications_list.html

echo \<b id=\"discussions\"\>Discussions\<\/b\>\<ul\> >>publications_list.html
perl -pe's|<p>|<li><p>|' discussions.html >>publications_list.html
echo \<\/ul\> >>publications_list.html

#echo \<b id=\"technical_reports\"\>Technical Reports\<\/b\>\<ul\> >>publications_list.html
#for i in ${TECHREPYEARS[*]}; do 
#	echo \<div class=\"strikethrough\"\>$i\<\/div\> >>publications_list.html
#	perl -pe's|<p>|<li><p>|' techrep$i.html >>publications_list.html
#done
#echo \<\/ul\> >>publications_list.html

echo \<b id=\"theses\"\>Theses\<\/b\>\<ul\> >>publications_list.html
perl -pe's|<p>|<li><p>|' theses.html >>publications_list.html
echo \<\/ul\> >>publications_list.html

#echo \<b id=\"magazines\"\>Magazines\<\/b\>\<ul\> >>publications_list.html
#perl -pe's|<p>|<li><p>|' magazines.html >>publications_list.html
#echo \<\/ul\> >>publications_list.html

rm bib2html*

# perl -i -pe's|journals.+_bib.html|biblio_bib.html|' publications_list.html
# perl -i -pe's|conferences._+bib.html|biblio_bib.html|' publications_list.html
# perl -i -pe's|discussions_bib.html|biblio_bib.html|' publications_list.html
# # perl -i -pe's|techrep.+_bib.html|biblio_bib.html|' publications_list.html
# perl -i -pe's|theses_bib.html|biblio_bib.html|' publications_list.html
# # perl -i -pe's|magazines_bib.html|biblio_bib.html|' publications_list.html

# perl -i -pe's|>pdf</a>| onclick="var that=this;_gaq.push(['\''_trackEvent'\'','\''Download'\'','\''PDF'\'',this.href]);setTimeout(function(){location.href=that.href;},200);return false;">pdf</a>|' publications_list.html

# cp publications_list.html tmp
# perl -i -pe's|.+strikethrough.+||' tmp
# perl -i -pe's|<p>||' tmp
# perl -i -pe's|</p>||' tmp
# perl -i -pe's|&nbsp;| |g' tmp

# ./html2latex tmp
# mv tmp.tex publications_list.tex
# awk 'FNR>5' publications_list.tex >tmp
# sed '$d' tmp >publications_list.tex
# perl -i -pe's|\[.+\]||' publications_list.tex
# perl -i -pe's|}\n|}|' publications_list.tex

mv publications_list.html ..

# for i in ${JOURNALSYEARS[*]}; do 
# 	perl -i -pe's|journals.+.html\S+"|publications.html"|;' journals"$i"_bib.html
# done    
# for i in ${CONFERENCESYEARS[*]}; do 
# 	perl -i -pe's|conferences.+.html\S+"|publications.html"|;' conferences"$i"_bib.html
# done    
# #for i in ${TECHREPYEARS[*]}; do 
# #	perl -i -pe's|techrep.+.html\S+"|publications.html"|;' techrep"$i"_bib.html
# #done    



# # perl -i -pe's|journals.html\S+"|publications.html"|;' journals_bib.html
# # perl -i -pe's|conferences.html\S+"|publications.html"|;' conferences_bib.html
# perl -i -pe's|discussions.html\S+"|publications.html"|;' discussions_bib.html
# # perl -i -pe's|techrep.html\S+"|publications.html"|;' techrep_bib.html
# perl -i -pe's|theses.html\S+"|publications.html"|;' theses_bib.html
# # perl -i -pe's|magazines.html\S+"|publications.html"|;' magazines_bib.html

# cat journals*_bib.html >biblio_bib.html
# cat conferences*_bib.html >>biblio_bib.html
# cat discussions_bib.html >>biblio_bib.html
# # cat techrep*_bib.html >>biblio_bib.html
# cat theses_bib.html >>biblio_bib.html
# # cat magazines_bib.html >>biblio_bib.html

rm journals*.html 
rm conferences*.html 
rm discussions.html 
# rm techrep*.html 
rm theses.html 
# rm magazines.html 

# mv biblio_bib.html ..


# pdflatex cv_en.tex
# pdflatex cv_it.tex









# bibtex2html -s abbrv -nokeys -noheader -nofooter -nodoc -citefile citefileSCV -nf pdf "pdf" -nf award "Best Paper Award" journals.bib
# bibtex2html -s abbrv -nokeys -noheader -nofooter -nodoc -citefile citefileSCV -nf pdf "pdf" conferences.bib
# bibtex2html -s abbrv -nokeys -noheader -nofooter -nodoc -citefile citefileSCV -nf pdf "pdf" discussions.bib
# # bibtex2html -s abbrv -nokeys -noheader -nofooter -nodoc -citefile citefileSCV -nf pdf "pdf" techrep.bib
# bibtex2html -s abbrv -nokeys -noheader -nofooter -nodoc -citefile citefileSCV -nf pdf "pdf" theses.bib
# # bibtex2html -s abbrv -nokeys -noheader -nofooter -nodoc -citefile citefileSCV -nf pdf "pdf" magazines.bib


# echo \<ul\> >publications_list_scv.html
# perl -pe's|<p>|<li><p>|' journals.html >>publications_list_scv.html
# perl -pe's|<p>|<li><p>|' conferences.html >>publications_list_scv.html
# perl -pe's|<p>|<li><p>|' discussions.html >>publications_list_scv.html
# echo \<\/ul\> >>publications_list_scv.html

# rm journals.html 
# rm conferences.html 
# rm discussions.html 

# perl -i -pe's|journals_bib.html|biblio_bib.html|' publications_list_scv.html
# perl -i -pe's|conferences_bib.html|biblio_bib.html|' publications_list_scv.html
# perl -i -pe's|discussions_bib.html|biblio_bib.html|' publications_list_scv.html

cp qq.html tmp
perl -i -pe's|.+strikethrough.+||' tmp
perl -i -pe's|<p>||' tmp
perl -i -pe's|</p>||' tmp
perl -i -pe's|&nbsp;| |g' tmp

./html2latex tmp
mv tmp.tex publications_list.tex
awk 'FNR>5' publications_list.tex >tmp
sed '$d' tmp >publications_list.tex
perl -i -pe's|\[.+\]||' publications_list.tex
perl -i -pe's|}\n|}|' publications_list.tex

# rm journals_bib.html 
# rm conferences_bib.html 
# rm discussions_bib.html 

pdflatex cv_en.tex
pdflatex short_cv.tex

# mv *.pdf ../cv/
