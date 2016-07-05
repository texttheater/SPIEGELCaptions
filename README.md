SPIEGELCaptions
===============

A Twitterbot parody of German magazine DER SPIEGEL’s image captions. Takes
existing captions and recombines them randomly, making just as much sense.
Live at [@SPIEGELCaptions](https://twitter.com/SPIEGELCaptions).

To download one year of DER SPIEGEL articles as PDFs:

    $ ./download YEAR

To convert all PDFs to TXT using `pdf2txt` and GNU Parallel (Tange 2011):

    $ find articles -name \*.pdf | sed -e 's/pdf/txt/' | parallel make

To extract captions halves from the text files:

    $ find articles -name \*.txt -exec cat {} \; | ./collect | ./filter > captions.txt

After adding new filters to `filter`, re-run the above command. Or, if you
don’t have the article text files anymore:

    $ make refilter

This will overwrite `captions.txt`.

The `captions.txt` currently in the repository is based on the DER SPIEGEL
archives of issues 22/1996—52/2015 (selected for PDF availability and
quality).

To make a random tweet and post it:

    $ ./post

References
----------

    O. Tange (2011): GNU Parallel - The Command-Line Power Tool,
    ;login: The USENIX Magazine, February 2011:42-47.
