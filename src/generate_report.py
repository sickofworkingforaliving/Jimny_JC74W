import pandas as pd
import os

def generate_csv(uk_listings, jp_processed):
    df = pd.DataFrame(jp_processed)

    output_path = os.path.join("data", "jimny-weekly-report.csv")
    df.to_csv(output_path, index=False)
