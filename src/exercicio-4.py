
import pandas as pd

medias = {"Ana": 8.5, "Bruno": 6.3,"Carla":9.1}

df = pd.Series(medias).reset_index()

df.columns = ["aluno","media"]

df = df.sort_values('media', ascending=False).reset_index(drop=True)

print(df)
