# Discount codes generator function

This micro-service is intended to be a Google cloud function or AWS lambda,
it's only responsibility is get the needed information from the user to create discount codes,
once it gets it, an event will be published to the event bus when the concerned service will pick
up the event and initiates the creation process.

# How to use:
Please run the following commands depending on what is your need.

1. Install python requirements:

 `pip install -r requirements.txt`

2. Run the server:

  `make run`

3. Run the tests:

  `make test`

4. Run the linter:

  `make lint`

5. Call the Generate discount codes endpoint:

  `http POST :9000/generate_discount_codes user_id=1 number_of_codes:=10 code_length=8`
