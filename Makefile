format:
	@echo "Running autoflake..."
	autoflake --remove-all-unused-imports --remove-unused-variables --in-place --recursive .

	@echo "Running isort..."
	isort . --profile black

	@echo "Running black..."
	black .
