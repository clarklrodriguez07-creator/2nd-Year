import json
import pandas as pd

class CSVExporter:
    def export(self, file_path):
        print("--- CSV DISPLAY REPORT ---")

        df = pd.read_excel(file_path)
        csv_data = df.to_csv(index=False)

        print(csv_data.strip())

        print("[END OF CSV REPORT]")

class JSONExporter:
    def export(self, file_path):
        print("--- JSON DISPLAY REPORT ---")

        df = pd.read_excel(file_path)
        json_data = df.to_dict(orient="records")

        print(json.dumps(json_data, indent=2))

        print("[END OF JSON REPORT]")

class PDFExporter:
    def export(self, file_path):
        print("[HEADER: Confidential Student Report]")

        df = pd.read_excel(file_path)

        for index, row in df.iterrows():
            print(f"Record #{index + 1}:")
            print(f"  ID: {row['ID']}")
            print(f"  NAME: {row['NAME']}")
            print(f"  COURSE: {row['COURSE']}")
            print("-" * 20)

def generate_report(exporter, file_path):
    exporter.export(file_path)


excel_file = "students.xlsx"

generate_report(CSVExporter(), excel_file)
generate_report(JSONExporter(), excel_file)
generate_report(PDFExporter(), excel_file)

