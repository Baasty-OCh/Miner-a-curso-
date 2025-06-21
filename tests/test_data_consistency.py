import pandas as pd


def test_anime_data_consistency():
    df_main = pd.read_csv("anime.csv")
    df_stats = pd.read_csv("anime-stats.csv")

    assert len(df_main) == len(df_stats)
    assert df_main["title"].iloc[0] == df_stats["title"].iloc[0]
    assert df_main["title"].iloc[-1] == df_stats["title"].iloc[-1]
