import altair as alt
import pandas as pd

# get data
domain = pd.read_csv("data/artificial-intelligence-training-computation.csv")
research = pd.read_csv("data/artificial-intelligence-training-computation-by-researcher-affiliation.csv")
merged = pd.concat([domain, research['Researcher_affiliation']],axis=1)
print(merged.head())
alt.data_transformers.disable_max_rows()  # enable altair to load data >5000 rows

# Show the data
chart1 = (
    alt.Chart(merged)
    .mark_circle(size=70)
    .encode(
        alt.X("Day:T", title="Publication Date"),
        alt.Y("Training_computation_petaflop:Q", scale=alt.Scale(type="log"), title="petaFLOP"),
        row='Researcher_affiliation:N',
        color=alt.Color("Domain:N"),
        tooltip=["Entity", "year", "Researcher_affiliation"]
    ).interactive()
    #.properties(width=600, height=500, title="Development of AI") #for unfaceted
    .properties(width=600, height=100, title="Development of AI") #for faceted
).configure_title(fontSize=20, anchor="start")

chart1.show()
#chart1.save("./output/chart1.html")

