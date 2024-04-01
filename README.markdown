## Readme

web2py is a free open source full-stack framework for rapid development of fast, scalable, secure and portable database-driven web-based applications.

It is written and programmable in Python. LGPLv3 License

Learn more at http://web2py.com

## web2py directory structure

    project/
        README
        LICENSE
        VERSION                    > this web2py version
        web2py.py                  > the startup script
        anyserver.py               > to run with third party servers
        ...                        > other handlers and example files
        gluon/                     > the core libraries
            packages/              > web2py submodules
              dal/
            contrib/               > third party libraries
            tests/                 > unittests
        applications/              > are the apps
            admin/                 > web based IDE
                ...
            examples/              > examples, docs, links
                ...
            welcome/               > the scaffolding app (they all copy it)
                ABOUT
                LICENSE
                models/
                views/
                controllers/
                sessions/
                errors/
                cache/
                static/
                uploads/
                modules/
                cron/
                tests/
            ...                    > your own apps
        examples/                  > example config files, mv .. and customize
        extras/                    > other files which are required for building web2py
        scripts/                   > utility and installation scripts
        handlers/
            wsgihandler.py         > handler to connect to WSGI
            ...                    > handlers for Fast-CGI, SCGI, Gevent, etc
        site-packages/             > additional optional modules
        logs/                      > log files will go in there
        deposit/                   > a place where web2py stores apps temporarily

## Please Check Resources Folder
Import DATABASE
Follow API documentation and here i attached API Collection

## For local installation
Clone the repository and run the following command
'python web2py.py'

Note: application/welcome/models/config_db.py check db configuration

## for docker 
Build: docker build -t learner .
Run : docker run learner

But there is some issue i can not complete with db configuration in docker there is some lacking of my efforts. Project proper run.

## Thanks and Regards TAMIM

