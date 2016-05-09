"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
""">>> Brand.query.get(8)
"""


"""
SELECT brands.brand_id AS brands_brand_id, brands.name AS brands_name, brands.founded AS brands_founded, brands.headquarters AS brands_headquarters, brands.discontinued AS brands_discontinued
FROM brands
WHERE brands.brand_id = %(param_1)s
INFO sqlalchemy.engine.base.Engine {'param_1': 8}
<__main__.Brand object at 0x10fc68c10>
"""


# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
""">>> q = Model.query
>>> q.filter(Model.name == 'Corvette', Model.brand_name == 'Chevrolet').all()
"""


"""
SELECT models.model_id AS models_model_id, models.year AS models_year, models.brand_name AS models_brand_name, models.name AS models_name
FROM models
WHERE models.name = %(name_1)s AND models.brand_name = %(brand_name_1)s
INFO sqlalchemy.engine.base.Engine {'brand_name_1': 'Chevrolet', 'name_1': 'Corvette'}
"""

# Get all models that are older than 1960.

""">>> q.filter(Model.year < 1960).all()
"""


"""
SELECT models.model_id AS models_model_id, models.year AS models_year, models.brand_name AS models_brand_name, models.name AS models_name
FROM models
WHERE models.year < %(year_1)s
INFO sqlalchemy.engine.base.Engine {'year_1': 1960}
"""

# Get all brands that were founded after 1920.

""">>> q.filter(Model.year > 1920).all()
"""


"""
SELECT models.model_id AS models_model_id, models.year AS models_year, models.brand_name AS models_brand_name, models.name AS models_name
FROM models
WHERE models.year > %(year_1)s
INFO sqlalchemy.engine.base.Engine {'year_1': 1920}
"""

# Get all models with names that begin with "Cor".

""">>> q.filter(Model.name == 'Cor%').all()

Note: there should be 12 results for the query. Why only getting one?
"""


"""
SELECT models.model_id AS models_model_id, models.year AS models_year, models.brand_name AS models_brand_name, models.name AS models_name
FROM models
WHERE models.name = %(name_1)s
"""

# Get all brands that were founded in 1903 and that are not yet discontinued.

""">>> q.filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()
"""
# Remember that None can't be in ALL Upper case ---> NONE


"""
SELECT models.model_id AS models_model_id, models.year AS models_year, models.brand_name AS models_brand_name, models.name AS models_name
FROM models, brands
WHERE brands.founded = %(founded_1)s AND brands.discontinued IS NULL
INFO sqlalchemy.engine.base.Engine {'founded_1': 1903}
"""


# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.

""">>> q.filter(or_(Brand.founded < 1950, Brand.discontinued.isnot_(None)).all()

    Kept thinking... (not sure what was the issue.)
"""


# Get any model whose brand_name is not Chevrolet.
"""q.filter(Brand.name != 'Chevrolet').all()
"""


"""
SELECT models.model_id AS models_model_id, models.year AS models_year, models.brand_name AS models_brand_name, models.name AS models_name
FROM models, brands
WHERE brands.name != %(name_1)s
INFO sqlalchemy.engine.base.Engine {'name_1': 'Chevrolet'}
"""

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

   #  This is the query needed:

   # """SELECT model, brand_name, headquarters FROM models JOIN brands WHERE year == (year)""" 
   
   # def __repr__(self):

   #      return "<The model is %s, the brand is %s, and the headquarters is %s>" % (self.model, self.name, self.headquarters)

   # is a repr fun. needed or a print can suffice the purpose?

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    # Select name, model from brands JOIN model WHERE name == 'name'

    # Need a for loop to print out all the model names. 
    # def __repr__(self):

    #     return "<The brand is %s, the model %s, and the headquarters is %s>" % (self.model, self.name, self.headquarters)

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

"""It returns an object: <flask_sqlalchemy.BaseQuery object at 0x10fcb8610>
"""

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

""" It is a table that can be connected to other tables. The association table can have different relationships one to many, many to many, and one to one. They can be connected through primary keys or foreign keys.
"""

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass
