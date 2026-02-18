### According to the documentation, why is the README file considered the most important file in a repository?
The README.md file shows by default on the homepage of your repo. It is used in order to provide information on what a tool does, or provide instructions on how to use or install it.
### What is a .gitignore file, and why is it important to use one when working with Python projects?
A .gitignore file tells Git what files to not track. In our Python projects the most helpful things to ignore are Build artifacts(\_\_pycache\_\_, \*.pyc), dev directories(venv/), OS specific files(.DS\_Store😡), sensitive data(.env, secrets/), various other tooling configs that you don't want to be default for other contributors.(.vscode/ ty.toml)
### What are the characteristics of a "good" commit message? Why shouldn't you just write "fixed stuff" for every commit?
A “good” commit message should clearly communicate what the changes are and their purpose. A good commit message has a specific(\<50 characters) header, as well as more detailed body text that explains more in depth changes and implementation details.
You shouldn’t just write “fixed stuff” for every commit because you will no longer know what you changed and why you made that change. Just writing “fixed stuff” makes it harder for you and other collaborators to understand what you are doing.
### Why is it important to include a LICENSE file in your repository, even if you are just a student?
It clarifies how others can use your work and how to attribute it when they do. It is important even as a student because it shows professionalism and helps others legally reuse/use your work.
### How do these best practices help a new person who has just been invited to collaborate on your repository for the first time?
These best practices help a new person who has just been invited to collaborate on your repository for the first time to understand what your code is doing or trying to do and they know how to navigate your work.
