# Variables
year ?= 2024
day ?= 1
step ?= 1
input ?= ""

# Directory and file paths
day_DIR = $(year)/day$(day)
SOLUTION = $(day_DIR)/solution.py

# Run solution.py
run:
	@if [ ! -f $(SOLUTION) ]; then \
		echo "Error: $(SOLUTION) not found. Ensure the file exists and try again."; \
		exit 1; \
	fi
	@echo "Running solution.py for year=$(year), day=$(day), step=$(step), input=$(input)"
	python $(SOLUTION) $(step) $(input)

# Create day directory if needed
create-day:
	@./generate_boilerplate $(year) $(day)

# Help command
help:
	@echo "Usage:"
	@echo "  make run year=<year> day=<day> step=<step> input=<input>"
	@echo "    - year: The year folder (default: 2024)"
	@echo "    - day: The day folder (default: 1)"
	@echo "    - step: Step number for solution.py (default: 1)"
	@echo "    - input: Optional input (example or nothing, default: empty)"
	@echo ""
	@echo "Example:"
	@echo "  make run year=2024 day=5 step=2 input=example"
	@echo ""
	@echo "Additional Commands:"
	@echo "  make create-day year=<year> day=<day>   # Create year and day folder structure"

