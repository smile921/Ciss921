# Build Notes

This is some basic instructions on how I setup my Python/Scipy/NumPy/Pandas/etc stack. This is really just for me and probably won't help anyone else. The only thing I am missing is a description of how to install pip.

## Basic Setup

1. Download and install Continuum Analytics's Anaconda

2. In the terminal, run:

	conda create -n py3k python=3 anaconda
	source activate py3k

## Activate py3k

source activate py3k

## Running iPython notebook with Anaconda's Python 3 Environment

1. Open the terminal

2. Run:

export PATH=/Users/chrisralbon/anaconda/envs/py3k/bin:$PATH
ipython notebook

## How to install a module, in this case pandas

export PATH=/Users/chrisralbon/anaconda/envs/py3k/bin:$PATH
pip install pandas

## How to install a module via condas, in this case pandas

conda install -n py3k pip

Note that py3k is the name of the acaconda environment we installed in the top of this document

## To make Python3 work with sublimetext3

1. Go to tools/build system/build new system, call it "Python3"

2. Paste in this (if you have Anaconda installed)

	{
    	"cmd":  ["/Users/chrisralbon/anaconda/envs/py3k/bin/python3", "-u", "$file"],
    	"file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    	"selector": "source.python",
    	"env": {"LANG": "en_US.UTF-8"}
	}

## To make Anaconda's Python2 work with sublimetext3

1. Go to tools/build system/build new system, call it "Python2"

2. Paste in this (if you have Anaconda installed)

	{
    	"cmd":  ["/Users/chrisralbon/anaconda/bin/python", "-u", "$file"],
    	"file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    	"selector": "source.python",
    	"env": {"LANG": "en_US.UTF-8"}
	}


# How to install a module from github.
# In this case, this module: https://github.com/wrobstory/climatic.git

export PATH=/Users/chrisralbon/anaconda/envs/py3k/bin:$PATH
pip install -e git+https://github.com/wrobstory/climatic.git#egg=climatic

# Upgrade a module, in this case pip

conda update pip -p /Users/chrisralbon/anaconda/envs/py3k

# Setup SublimeREPL to connect to Anaconda's Python3

In your Packages/User folder, create SublimeREPL/config/Python/Main.sublime-menu with the following contents:

	[
	    {
	        "id": "tools",
	        "children":
	        [{
	            "caption": "SublimeREPL",
	            "mnemonic": "r",
	            "id": "SublimeREPL",
	            "children":
	            [
	                {
	                    "caption": "Python",
	                    "id": "Python",

	                    "children":[
	                        {
	                            "command": "repl_open",
	                            "caption": "Python - Anaconda",
	                            "id": "repl_python",
	                            "mnemonic": "p",
	                            "args": {
	                                "type": "subprocess",
	                                "encoding": "utf8",
	                                "cmd": ["/Users/chrisralbon/anaconda/envs/py3k/bin/python3", "-i", "-u"],
	                                "cwd": "$file_path",
	                                "syntax": "Packages/Python/Python.tmLanguage",
	                                "external_id": "python",
	                                "extend_env": {"PYTHONIOENCODING": "utf-8"}
	                            }
	                        },
	                        {
	                            "command": "repl_open",
	                            "caption": "IPython - Anaconda",
	                            "id": "repl_python_ipython",
	                            "mnemonic": "p",
	                            "args": {
	                                "type": "subprocess",
	                                "encoding": "utf8",
	                                "autocomplete_server": true,
	                                "cmd": ["/Users/chrisralbon/anaconda/envs/py3k/bin/python3", "-u", "${packages}/SublimeREPL/config/Python/ipy_repl.py"],
	                                "cwd": "$file_path",
	                                "syntax": "Packages/Python/Python.tmLanguage",
	                                "external_id": "python",
	                                "extend_env": {
	                                    "PYTHONIOENCODING": "utf-8",
	                                    "SUBLIMEREPL_EDITOR": "$editor"
	                                }
	                            }
	                        }
	                    ]
	                }
	            ]
	        }]
	    }
	]


Save the file, and you should now have Tools -> SublimeREPL -> Python -> Python - Anaconda and IPython - Anaconda menu options to start REPLs with the Anaconda interpreter.

# To launch ipython notebook (with anaconda's python 3) in chrome

	source activate py3k
	BROWSER=/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome ipython notebook

