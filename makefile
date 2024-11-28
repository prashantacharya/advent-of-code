# Variables
YEAR ?= 2024
DAY ?= 01
STEP ?= 1
INPUT ?= ""

# Directory and file paths
DAY_DIR = $(YEAR)/day$(DAY)
SOLUTION = $(DAY_DIR)/solution.py

# Run solution.py
run:
	@if [ ! -f $(SOLUTION) ]; then \
		echo "Error: $(SOLUTION) not found. Ensure the file exists and try again."; \
		exit 1; \
	fi
	@echo "Running solution.py for year=$(YEAR), day=$(DAY), step=$(STEP), input=$(INPUT)"
	python $(SOLUTION) $(STEP) $(INPUT)

# Create day directory if needed
create-day:
	@./create_advent_folder.sh $(YEAR) $(DAY)

# Help command
help:
	@echo "Usage:"
	@echo "  make run YEAR=<year> DAY=<day> STEP=<step> INPUT=<input>"
	@echo "    - YEAR: The year folder (default: 2024)"
	@echo "    - DAY: The day folder (default: 01)"
	@echo "    - STEP: Step number for solution.py (default: 1)"
	@echo "    - INPUT: Optional input (example or nothing, default: empty)"
	@echo ""
	@echo "Example:"
	@echo "  make run YEAR=2024 DAY=05 STEP=2 INPUT=example"
	@echo ""
	@echo "Additional Commands:"
	@echo "  make create-day YEAR=<year> DAY=<day>   # Create year and day folder structure"

