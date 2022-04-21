# WbSearch

Search anything on main browser directly from terminal (both words and links).

`Installation:`

    $ pip install wbsearch

`Usage:`

    $ wbsearch argument

Replace argument with your own research. 
In case you want to search multiple words, you may need to use "\" before each space, 
or use double quotes around, depending on your operating system.

`Save a keyword:`

    $ wbsearch --set keyword link
    
    $ wbsearch -s keyword link

Replace keyword with your own keyword, and link with your own link. 
This method allows to locally set constant keywords.
The same method allows to edit the content of the keyword, simply entering the kewyord and then the new associated link 

`Remove a keyword:`

    $ wbsearch --remove keyword
    
    $ wbsearch -r keyword

Replace keyword with the keyword you want to remove from wbsearch user keywords.

`Display saved keywords:`

    $ wbsearch --keywords
    
    $ wbsearch -k

Shows all the saved keywords.

`Help:`

    $ wbsearch --help

Type this command to get help.

`Examples:`

- Search a link:
        
      $ wbsearch https://www.github.com/

- Search a word:

      $ wbsearch python

- Set a keyword:

      $ wbsearch --set github https://www.github.com/

      $ wbsearch -s pypi https://pypi.org/

- Use a keyword:

      $ wbsearch github 

    Opens the link associated with the keyword "github"


- Display all the saved keywords:

      $ wbsearch -k
        
      output:

        Saved keywords:
            github -> https://www.github.com/
            pypi -> https://pypi.org/

- Remove a keyword:

      $ wbsearch --remove github

      $ wbsearch -r pypi

- Get help:

      $ wbsearch --help
        
      output:

          Usage: wbsearch [OPTIONS] [ARGUMENT]

            Argument: url, word(s) or keyword. To search multiple words, wrap them
            around with double quotes or put "\" before each space

            Version: 2.2.1

          Options:
            -s, --set TEXT     Set keywords to access your links
            -r, --remove TEXT  Remove a keyword
            -k, --keywords     Show all the saved keywords
            --help             Show this message and exit.
