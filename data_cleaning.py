import pandas as pd

def load_sample():
    df = pd.DataFrame({"id":[1,2,2,3], "value":[10,20,20,30]})
    return df

def clean(df):
    df_clean = df.drop_duplicates().reset_index(drop=True)
    return df_clean

if __name__ == "__main__":
    df = load_sample()
    print("Original data:\n", df)
    print("\nCleaned data:\n", clean(df))
