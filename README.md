# Fair-biller                         [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Description                       
A command-line program that helps a hosted application provider generate fair billing for its customers' use of it application depending on the duration of sessions.
The program achieves analyses and processes usage data contained in a log file and generates a report with the details below:
    Name of user
    Number of sessions used
    Total duratation

Tools/Technologies - Python, VSCode, Git, GitHub and GitBash.


## Table of Contents 
[Description](#description)

[Installation](#installation)

[Usage](#usage)

[License](#license)

[Contributing](#contributing)

[Tests](#tests)
 
[Questions](#questions)

## Installation 
1. Install Python2.7 on your local machine.
2. Clone the repository to a directory of choice and navigate to the directory using terminal.
3. Run 'python2.7 fair-biller.py session-log' at the prompt. 

## Usage
1. See step 3 of the installation instructions. 

## License 
MIT

Copyright (c) 2024 Oluwaseun Olusanya
    
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
    
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Contributing 
1. Fork the project.
2. Create a feature branch from your main branch.
3. Make some commits to improve the project.
4. Push this branch to your GitHub project.
5. Open a Pull Request on GitHub.
6. Discuss, and optionally continue committing.
7. The request will be reviewed, merged and closed.
8. You can then pull the main to your fork and continue contributing.

## Tests
1. Open 'session-log' file.
2. Add more entries to the content. For example,
   - 15:03:37 ADE End
   - 15:04:05 ALICE99 End
   - 15:44:23 SEUN End
   - 16:04:41 CHARLIE Start
3. Save and close the file
4. Type 'python2.7 fair-biller.py session-log' at the terminal.

## Questions
Please engage with me on https://github.com/https://github.com/oluwaseunolusanya if you have questions about the project. You can also reach me at oluwaseun_olusanya@yahoo.com.
