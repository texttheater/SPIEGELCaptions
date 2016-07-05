articles/%.txt : articles/%.pdf
	pdf2txt $< > $@

captions.txt :
	# Before 1/1994: PDFs contain only images
	# Before 22/1996: pratically all extracted captions are riddled with extra spaces
	cat articles/1996/{22..52}/*.txt articles/{1997..2015}/*/*.txt | ./collect | ./filter | uniq > $@

.PHONY : refilter
refilter :
	cat captions.txt | ./filter > captions.txt.tmp
	mv captions.txt.tmp captions.txt
