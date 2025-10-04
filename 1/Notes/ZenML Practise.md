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

Then created files in steps folder. Kind of a blueprint and not the actual code.
Also try to Document what each function does in commets. One line explanation, One line on Arguments and one on Returning Value

Then putting a pipeline file to take in all the steps.

Then write a run_pipeline.py and run via py run_pipeline.py, pipeline will be created. Make sure to use `__main__` and not forget underscores. Here `__name__ == "__main__"` is so that the file is directly run as py run_pipeline.py and no by another source as import run_pipeline and run from there. Basically only run via main file and not and dependency type.

Then in terminal enter -> zenml login --local --blocking
It will create a local server where you can look the pipelines that you have created. Login by user as `default`

(enable_cache = False) -> Training from Start
(enable_cache = True) -> This Cache's the Step's data in a local folder and The MLOps Framework checks if any change is there in steps, if not, it reuses cached artifacts. This for a faster and a better run.

Till Now this is the blueprint of the task.