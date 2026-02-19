## Pydantic Practice (v2)

This repository contains my hands-on practice with Pydantic v2 while learning backend development with FastAPI.
I created small focused examples to understand how data validation works in real-world backend systems.

# What’s Covered

1. Field constraints using Field and Annotated
2. Type validation (PositiveInt, Literal, Optional, List)
3. Custom validation using @field_validator
4. Cross-field validation using @model_validator
5. Computed fields with @computed_field
6. Serialization & deserialization using model_validate
7. Environment configuration using BaseSettings
8. Basic FastAPI setup
Each file focuses on one concept so that it’s easy to understand and test individually.

# Why I Built This

While learning backend development, I realized that proper data validation is critical.
Instead of just watching tutorials, I wrote small examples to test each feature myself.

This repo is part of my backend foundation building.

# Tech Stack

* Python 3.10+
* Pydantic v2
* FastAPI
* pydantic-settings

# Next Steps

* Add nested models
* Add error handling patterns
* Connect models with API endpoints
* Integrate database layer
