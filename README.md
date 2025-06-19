# Fruit Search

An application to search for fruit products based on their respective category and tags.

## Prerequisites

- python >= 3.13.3

## Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd RemarcableProject
   ```

2. Install dependencies:
   ```
   python -m venv venv
   (On Windows) .\venv\Scripts\activate
   (On Linux) source venv/bin/activate
   pip install -r requirements.txt
   ``` 

## Run the App

To run the application:

```
python manage.py runserver
```

## Features

- Search for a fruit by its description
- Filter for fruits by category
- Filter for fruits by tag(s)

## DB Relationships

- A product has 1 category
- A product may have many tags
- A tag relates to many products

## AI Usage
- For creating a base for the DocStrings in views.py. All DocStrings were modified to what I thought related well to the intended functionality.
- To help create more than 5 fruits (apparently that is the ceiling of fruits I am aware of) and their descriptions.
- To assist in creating a more cohesive frontend.
