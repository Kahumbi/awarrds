# Awwards
​
## Author [David Kahumbi]
​
## Description
Awwards app is an app built with django rest framework to build an api from scratch and fetch raw json data response and display it in a python fomat, authenticated users can interract with the app by searching and posting projects.
​
## Technologies Used
python 3.8
Django
Html
CSS
Bootstrap

## User Stories
Users will be able to:
*Create projects
*Search for projects
*Post new projects
*View posted projects
*Delete projects
 

## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Create a new user | **Add a new profile** | New users can create a project |
| Post a project | **Add a project** | Post project image  |
| hover on project title link | **Click on project link** | Get redirect to posted project |
| Add a new project | **Fields are required** | Display the new project |
​
​
## Known Bugs
If you find a bug please feel free to alert me. To fix the bug:
​
Fork the repository
Open your terminal
Create a new branch
Make the changes, then (git add) to add changes
Commit the changes you have made(git commit -m"Fix bug")
Push changes made and click pull request so that I can access the changes made.
​
​
## SetUp / Installation Requirements
### Prerequisites
* python3.8
* pip
* virtualenv
​
### Api View and Routes

* https://kusakahiiapi.herokuapp.com/postList/
* https://kusakahiiapi.herokuapp.com/postCreate/
* https://kusakahiiapi.herokuapp.com/postDetail/1/
* https://kusakahiiapi.herokuapp.com/postUpdate/1/
* https://kusakahiiapi.herokuapp.com/postDelete/1/

### Cloning
* In your terminal:
​
        $ git clone https://github.com/kahumbi/awarrds.git
        $ cd Pitch
​
## Running the Application
* Creating the virtual environment
​
        $ python3.8 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python
        $ pip install Django
​

## License
​
License
MIT Copyright (c) 2022 David Kahumbi
​
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
​
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
​
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
​
=======
​
Kahumbi kusakahiiapi