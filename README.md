# Backend Task - Clean Architecture

This project is a very naive implementation of a simple shop system. It mimics in its structure a real world example of a service that was prepared for being split into microservices and uses the current Helu backend tech stack.

## Goals

Please answer the following questions:

1. Why can we not easily split this project into two microservices?
   - One of the issues that I was able to identify, is that the user cart needs to to have user and item ids.
   - This creates runtime coupling, and also these dependencies break isolation and scalability purpose of microservices.

2. Why does this project not adhere to the clean architecture even though we have seperate modules for api, repositories, usecases and the model?
   - Breaking down the code into separate files does not necessarily means clean architecture is been follow to the letter, this just make the code easier to read and to re-use. 
   - Repositories, entities, and use cases were sometimes referenced bewteen layers improperly, this violates clean architecture goals.
3. What would be your plan to refactor the project to stick to the clean architecture?

    The plan was to define different layers following clean architecture and making sure the dependency inyection was propertly use.
   - entities: Business models, no dependencies.
   - use_cases: Business logic, dependents only on interfaces.
   - interfaces: FastAPI routers.
   - repositories: in-memory implementations with no database connections or SQL queries.
4. How can you make dependencies between modules more explicit?

   - Inject dependencies into use cases and routers at initialization time.
   - Using typing module to enforce contracts with tools like mypy or pydantic.
   - Preventing improper cross-imports using tools like flake8, isort, import-linter.

*Please do not spend more than 2-3 hours on this task.*

Stretch goals:
* Fork the repository and start refactoring
* Write meaningful tests
* Replace the SQL repository with an in-memory implementation

## References
* [Clean Architecture by Uncle Bob](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
* [Clean Architecture in Python](https://www.youtube.com/watch?v=C7MRkqP5NRI)
* [A detailed summary of the Clean Architecture book by Uncle Bob](https://github.com/serodriguez68/clean-architecture)

## How to use this project

If you have not installed poetry you find instructions [here](https://python-poetry.org/).

1. `docker-compose up` - runs a postgres instance for development
2. `poetry install` - install all dependency for the project
3. `poetry run schema` - creates the database schema in the postgres instance
4. `poetry run start` - runs the development server at port 8000
5. `/postman` - contains an postman environment and collections to test the project

## Other commands

* `poetry run graph` - draws a dependency graph for the project
* `poetry run tests` - runs the test suite
* `poetry run lint` - runs flake8 with a few plugins
* `poetry run format` - uses isort and black for autoformating
* `poetry run typing` - uses mypy to typecheck the project

## Specification - A simple shop

* As a customer, I want to be able to create an account so that I can save my personal information.
* As a customer, I want to be able to view detailed product information, such as price, quantity available, and product description, so that I can make an informed purchase decision.
* As a customer, I want to be able to add products to my cart so that I can easily keep track of my intended purchases.
* As an inventory manager, I want to be able to add new products to the system so that they are available for customers to purchase.