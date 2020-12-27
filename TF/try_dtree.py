import pandas as pd
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import graphviz
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
import numpy as np

data = {
	"Age": [36,42,23,52,43,44],
	"Experience": [10,12,4,4,21,14],
	"Rank": [9,4,6,4,8,5],
	"Nationality": ['UK','USA','N',"USA",'USA',"UK"],
	"Go": ['No', 'No', "Yes", 'Yes', 'Yes', 'No']
}

df = pd.DataFrame(data)

print(df)

d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'Yes': 1, 'No': 0}
df['Go'] = df['Go'].map(d)

print(df)

features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
y = df['Go']

print(X)
print(y)

dtree = DecisionTreeClassifier()
dtree.fit(X, y)

print(dtree.predict([[40, 10, 7, 1]]))

print(dtree.predict([[50, 4, 6, 1]]))

print("[1] means 'GO'")
print("[0] means 'NO'")

fig = dtree.fit(X, y)
graph = tree.plot_tree(fig)
plt.show()

cn=['GO', 'NO']
fig1, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=300)
tree.plot_tree(dtree,
               feature_names = features, 
               class_names=cn,
               filled = True);
fig1.savefig('dtree.png')

# graphviz graph not shown 

dot_data = tree.export_graphviz(dtree, out_file=None, 
                                feature_names=features,  
                                class_names=cn,
                                filled=True)

graph = graphviz.Source(dot_data, format="png") 
graph

# https://stackoverflow.com/questions/27817994/visualizing-decision-tree-in-scikit-learn
# https://towardsdatascience.com/visualizing-decision-trees-with-python-scikit-learn-graphviz-matplotlib-1c50b4aa68dc
# https://stackoverflow.com/questions/42493045/graphviz-not-drawing-graph
