# ZenML Notes

Guide Given by ZenML Team: https://github.com/zenml-io/zenbytes/tree/main

Look at the .ipynb files to just get the idea, do not run them. The Code there is old and very buggy.

https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce/data is the datset used but it is combined in to one and the main data link is https://github.com/ayush714/customer-satisfaction-mlops/blob/main/data/olist_customers_dataset.csv

To run a notebook -> python -m notebook

To Create a Environment Folder -> python -m venv myenv
To Activate Environment -> myenv\Scripts\activate
To Quit from it -> deactivate

To Put all Requirements into a text file -> pip freeze > requirements.txt
And to install from folder -> pip install -r requirements.txt

Usually in industry we do not directly work with csv but with sql.

OOPs in Python

`__init__` is the name of constructor and not name of the class. It always takes self as a parameter.
`_` means protected
`__` means private

`self` is basically `this` in python, just that it is always used to acces the variables in python like self.a, self.mse, etc..

How Inheritance works in python -> class A : ... then class B(A)
Now `super.__init__()` calls the parent's constructor

What we write --> a = A(10)
What Happens Internally:
`obj = A.__new__(A)`
`A.__init__(obj,10)`

`__init__.py` is industry standard naming convention for production codebases.

Starting..

To initialize -> zenml init