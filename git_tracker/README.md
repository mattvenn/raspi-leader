# Visual Code tracking 

The idea is to help understand how people learn to code, and to be able to give specific help when it's required.

By fetching the student's code regularly we can look at a some basic metrics to better understand their progress:

* syntax errors - using the Python compile library
* lines of code

These are plotted against time and shown using your browser. 

Code is added to a local git repo for change tracking and later we could add some kind of code browsing functionality.

# Setup on student's computer

    cd work
    mkdir myname
    cd myname
    #edit code

The newest file in each student's directory in ~/work will be used for code tracking.

# Setup on main pc

* edit config.py to add hosts for scp,
* run ./init.py to create local repo and initialise,
* regulary run crontab ./fetch.py to fetch all work
* regulary run ./generate.py to create the graph.html
* I serve the file with `python -mSimpleHTTPServer` and fetch at [http://127.0.0.1/graph.html]

# Requirements

* flot graphing, download and extract in the directory https://github.com/flot/flot

# Todo

* only show most recent single file from each user's dir
* browse versions of code
