SPIEGELCaptions
===============

A Twitterbot parody of German magazine DER SPIEGEL’s image captions. Takes
existing captions and recombines them randomly, making just as much sense.
Live at [@SPIEGELCaptions](https://twitter.com/SPIEGELCaptions).

To download one year of DER SPIEGEL articles as PDFs:

    $ ./download YEAR

To convert all PDFs to TXT using `pdf2txt` and GNU Parallel (Tange 2011):

    $ find articles -name \*.pdf | sed -e 's/pdf/txt/' | parallel make

To extract caption halves from the text files:

    $ find articles -name \*.txt -exec cat {} \; | ./collect

This will overwrite `part1.txt` and `part2.txt`, which in their distributed
version are based on the DER SPIEGEL archives of 2001–2014.

To make a random tweet and post it:

    $ ./post

References
----------

    O. Tange (2011): GNU Parallel - The Command-Line Power Tool,
    ;login: The USENIX Magazine, February 2011:42-47.