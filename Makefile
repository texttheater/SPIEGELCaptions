articles/%.txt : articles/%.pdf
	pdf2txt $< > $@
