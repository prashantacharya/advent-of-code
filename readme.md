# Advent of Code 

This project provides a streamlined workflow for managing Advent of Code challenges. It includes a Bash script to create year and day folders with necessary files, a Python solution template, and a Makefile to automate running solutions.

---

## Setup Instructions

1. **Clone or Download the Repository**  
   Ensure the repository contains the following files:
   - `generate_boilerplate`: Script to create folder structures and files.
   - `template/template.py`: Python template for solutions.
   - `Makefile`: For running solutions and managing the project.

2. **Make `generate_boilerplate` Executable**  
   Run the following command to make the script executable:
   ```bash
   chmod +x generate_boilerplate

3. **Ensure Required Tools are Installed**
Python: Required to run the solution scripts.
Bash: Needed for running the generate_boilerplate script.
Make: Required to use the Makefile.

4. **Folder and File Creation**
To create the necessary folder structure for a specific year and day, use the create-day target in the Makefile:

```bash
make create-day YEAR=2022 DAY=1
```

This will create the following folder structure:
```
.
├── README.md
├── template
│   └── template.py
├── 2022
│   └── day1
│       ├── example
│       ├── challenge
│       └── solution.py
```

5. **Poplulating the example and challenge files**
- Add the example content from AOC to the example file
- Add the challenge content from AOC to the challenge file

6. **Write the solution**

7. **Running the solution**
To run the solution, use the run-day target in the Makefile:

```bash
make run YEAR=<year> DAY=<day> STEP=<step> INPUT=<'eaxmple' or nothing>
```

If nothing is provided for input, challenge will be used as the default.
If nothing is provided for step, 1 will be used as the default.

For example, to run the solution for day 1 of 2022, use the following command:
```bash
make run YEAR=2022 DAY=1 STEP=1 INPUT=example
```

