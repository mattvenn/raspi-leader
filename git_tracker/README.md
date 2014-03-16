# todo

* only show most recent single file from each user's dir
* only show .py files

# setup on pi

    git init work
    while true; do git add -A *py ; git commit --allow-empty-message  -m '' ; sleep 1; done

Ideally, no setup will be minimal:

    cd work
    mkdir myname
    cd myname
    tightvncserver

then the newest file in each directory in ~/work will be used for code tracker

#setup on main pc

    git clone work
    #to update
    while true; do git pull; sleep 5; done

    #to fetch commits
    git log --pretty=format:%H > ../commits

    #to step through them
    for a in $(tac ../commits); do echo $a; git checkout $a; ipython ttest.py; gvim -fu ../vimrc ttest.py;  done
