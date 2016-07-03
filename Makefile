articles/%.txt : articles/%.pdf
	pdf2txt $< > $@

captions.txt :
	cat articles/*/*/*.txt | ./collect | ./filter < $@

.PHONY : refilter
refilter :
	cat captions.txt | ./filter > captions.txt.tmp
	mv captions.txt.tmp captions.txt
