from scraper import scrape_headlines
from reporter import generate_numbered_list, get_top_titles_by_length, count_items, write_report, write_json
import argparse
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--top" , type=int, default=2)
    parser.add_argument("--output", type=str, default="report.txt")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    return parser.parse_args()

def run_pipeline(n, output_file_path, output_file_path_json, export_json, verbose):
    data = scrape_headlines()
    if data is None:
        return

    numbered_list = generate_numbered_list(data)
    top_titles_by_length = get_top_titles_by_length(data, n)
    total_items = count_items(data)

    if verbose:
        print(f"Fetched {len(data)} headlines")
        print(f"Computed top {n} longest titles")
        print(f"TXT output: {output_file_path}")
        if export_json:
            print(f"JSON output: {output_file_path_json}")
        print("Generating report...")

    write_report(output_file_path, numbered_list, top_titles_by_length, total_items)

    if export_json:
        write_json(output_file_path_json, data)
        print("JSON generated:", output_file_path_json)

    print("Report generated:", output_file_path)

def main():
    args = parse_args()
    n = args.top

    base_name = args.output.removesuffix(".txt").removesuffix(".json")
    output_file_path = base_name + ".txt"
    output_file_path_json = base_name + ".json"

    if n <= 0:
        print("Invalid input, using default value (2).")
        n = 2

    run_pipeline(
        n,
        output_file_path,
        output_file_path_json,
        args.json,
        args.verbose
    )

if __name__ == "__main__":
    main()


