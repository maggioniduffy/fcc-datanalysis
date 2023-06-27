import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def is_overweight(kg,meters):
    bmi = kg/(meters*meters)
    if bmi > 25:
        return 1
    else:
        return 0
 
# Import data
df = pd.read_csv('./medical_examination.csv')

# Add 'overweight' column
overweights = []
for index, row in df.iterrows():
    overweights.append(is_overweight(row['weight'],row['height']/100))
df['overweight'] = overweights

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

#Normalize the data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, make the value 0. If the value is more than 1, make the value 1.
gluc = df['gluc']
new_gluc = []
for g in gluc:
    if g == 1:
        new_gluc.append(0)
    elif g > 1:
        new_gluc.append(1)
    else:
        new_gluc.append(g)
df['gluc'] = new_gluc

cholesterol = df['cholesterol']
new_cholesterol = []
for g in cholesterol:
    if g == 1:
        new_cholesterol.append(0)
    elif g > 1:
        new_cholesterol.append(1)
    else:
        new_cholesterol.append(g)
df['cholesterol'] = new_cholesterol

for column in df.columns:
    df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min()) 

#df = df.round(1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values 
    # from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    #print(list(df.columns))
    df_cat = pd.melt(df, value_vars=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"], id_vars="cardio")
    fig, ax = plt.subplots()
    fig = sns.catplot(data=df_cat, kind="count", x="variable", hue="value", col="cardio", ax=ax)
    fig.set_axis_labels("variable","totals")
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    indexAge = df[ (df['ap_lo'] <= df['ap_hi']) | 
              (df['height'] <= df['height'].quantile(0.025)) |
              (df['height'] > df['height'].quantile(0.975)) |
              (df['weight'] <= df['weight'].quantile(0.025)) |
              (df['weight'] > df['weight'].quantile(0.975))].index
    df.drop(indexAge , inplace=True)
    d = pd.DataFrame(data=df,
                 columns=list(df.columns))

    # # Calculate the correlation matrix
    corr = d.corr()

    # # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))

    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(230, 20, as_cmap=True)

    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0, annot=True,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
