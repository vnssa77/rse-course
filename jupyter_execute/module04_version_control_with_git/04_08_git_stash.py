#!/usr/bin/env python
# coding: utf-8

# # Git Stash

# Before you can `git pull`, you need to have committed any changes you have made. If you find you want to pull, but you're not ready to commit, you have to temporarily "put aside" your uncommitted changes.
# For this, you can use the `git stash` command, like in the following example:

# In[1]:


import os

top_dir = os.getcwd()
git_dir = os.path.join(top_dir, "learning_git")
working_dir = os.path.join(git_dir, "git_example")
os.chdir(working_dir)


# Remind ourselves which branch we are using:

# In[2]:


get_ipython().run_cell_magic('bash', '', 'git branch -vv\n')


# In[3]:


get_ipython().run_cell_magic('writefile', 'Wales.md', 'Mountains In Wales\n==================\n\n* Pen y Fan\n* Tryfan\n* Snowdon\n* Glyder Fawr\n* Fan y Big\n* Cadair Idris\n* Penygader\n')


# In[4]:


get_ipython().run_cell_magic('bash', '', 'git stash\n')


# In[5]:


get_ipython().run_cell_magic('bash', '', 'git pull\n')


# By stashing your work first, your repository becomes clean, allowing you to pull. To restore your changes, use `git stash apply`.

# In[6]:


get_ipython().run_cell_magic('bash', '', 'git stash apply\n')


# The "Stash" is a way of temporarily saving your working area, and can help out in a pinch.

# # Tagging
# 
# Tags are easy to read labels for revisions, and can be used anywhere we would name a commit.
# 
# Produce real results *only* with tagged revisions.
# 
# NB: we delete previous tags with the same name remotely and locally first, to avoid duplicates.

# ``` Bash
# git tag -a v1.0 -m "Release 1.0"
# git push --tags
# ```

# You can also use tag names in the place of commmit hashes, such as to list the history between particular commits:

# ``` Bash
# git log v1.0.. --graph --oneline
# ```

# If .. is used without a following commit name, HEAD is assumed.

# # Working with generated files: gitignore

# We often end up with files that are generated by our program. It is bad practice to keep these in Git; just keep the sources.

# Examples include `.o` and `.x` files for compiled languages, `.pyc` files in Python.

# In our example, we might want to make our .md files into a PDF with pandoc:

# In[7]:


get_ipython().run_cell_magic('writefile', 'Makefile', '\nMDS=$(wildcard *.md)\nPDFS=$(MDS:.md=.pdf)\n\ndefault: $(PDFS)\n\n%.pdf: %.md\n\tpandoc $< -o $@\n')


# In[8]:


get_ipython().run_cell_magic('bash', '', 'make\n')


# We now have a bunch of output .pdf files corresponding to each Markdown file.

# But we don't want those to show up in git:

# In[9]:


get_ipython().run_cell_magic('bash', '', 'git status\n')


# Use .gitignore files to tell Git not to pay attention to files with certain paths:

# In[10]:


get_ipython().run_cell_magic('writefile', '.gitignore', '*.pdf\n')


# In[11]:


get_ipython().run_cell_magic('bash', '', 'git status\n')


# In[12]:


get_ipython().run_cell_magic('bash', '', 'git add Makefile\ngit add .gitignore\ngit commit -am "Add a makefile and ignore generated files"\ngit push\n')


# # Git clean

# Sometimes you end up creating various files that you do not want to include in version control. An easy way of deleting them (if that is what you want) is the `git clean` command, which will remove the files that git is not tracking.

# In[13]:


get_ipython().run_cell_magic('bash', '', 'git clean -fX\n')


# In[14]:


get_ipython().run_cell_magic('bash', '', 'ls\n')


# * With -f: don't prompt
# * with -d: remove directories
# * with -x: Also remote .gitignored files
# * with -X: Only remove .gitignore files

# # Hunks
# 
# ## Git Hunks
# 
# A "Hunk" is one git change. This changeset has three hunks:

# ```python
# +import matplotlib
# +import numpy as np
# 
#  from matplotlib import pylab
#  from matplotlib.backends.backend_pdf import PdfPages
# 
# +def increment_or_add(key,hash,weight=1):
# +       if key not in hash:
# +               hash[key]=0
# +       hash[key]+=weight
# +
#  data_path=os.path.join(os.path.dirname(
#                         os.path.abspath(__file__)),
# -regenerate=False
# +regenerate=True
# ```

# ## Interactive add
# 
# `git add` and `git reset` can be used to stage/unstage a whole file,
# but you can use interactive mode to stage by hunk, choosing
# yes or no for each hunk.

# ``` bash
# git add -p myfile.py
# ```

# ``` python
# +import matplotlib
# +import numpy as np
# #Stage this hunk [y,n,a,d,/,j,J,g,e,?]?
# ```

# # GitHub pages
# 
# ## Yaml Frontmatter
# 
# GitHub will publish repositories containing markdown as web pages, automatically. 
# 
# You'll need to add this content:
# 
# > ```
# >    ---
# >    ---
# > ```
# 
# A pair of lines with three dashes, to the top of each markdown file. This is how GitHub knows which markdown files to make into web pages.
# [Here's why](https://jekyllrb.com/docs/front-matter/) for the curious. 

# In[15]:


get_ipython().run_cell_magic('writefile', 'test.md', '---\ntitle: Github Pages Example\n---\nMountains and Lakes in the UK\n===================\n\nEngerland is not very mountainous.\nBut has some tall hills, and maybe a mountain or two depending on your definition.\n')


# In[16]:


get_ipython().run_cell_magic('bash', '', 'git commit -am "Add github pages YAML frontmatter"\n')


# ## The gh-pages branch
# 
# GitHub creates github pages when you use a special named branch.
# By default this is `gh-pages` although you can change it to something else if you prefer.
# This is best used to create documentation for a program you write, but you can use it for anything.

# In[17]:


os.chdir(working_dir)


# In[18]:


get_ipython().run_cell_magic('bash', '', '\ngit checkout -b gh-pages\ngit push -uf origin gh-pages\n')


# The first time you do this, GitHub takes a few minutes to generate your pages. 
# 
# The website will appear at `http://username.github.io/repositoryname`, for example:
# 
# http://alan-turing-institute.github.io/github-example/

# ## Layout for GitHub pages
# 
# You can use GitHub pages to make HTML layouts, here's an [example of how to do it](http://github.com/UCL/ucl-github-pages-example), and [how it looks](http://ucl.github.com/ucl-github-pages-example). We won't go into the detail of this now, but after the class, you might want to try this.

# In[19]:


get_ipython().run_cell_magic('bash', '', '# Cleanup by removing the gh-pages branch \ngit checkout main\ngit push\ngit branch -d gh-pages\ngit push --delete origin gh-pages \ngit branch --remote\n')

