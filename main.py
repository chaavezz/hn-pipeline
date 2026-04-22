from scraper import scrape_headlines
from reporter import generate_numbered_list, get_top_titles_by_length, count_items, write_report
import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--top" , type=int, default=2)
    parser.add_argument("--output", type=str, default="report.txt")

    args = parser.parse_args()

    n = args.top
    output_file_path = args.output
    if not output_file_path.endswith(".txt"):
        output_file_path += ".txt"

    if n <= 0:
        print("Invalid input, using default value (2).")
        n = 2
         
    data = scrape_headlines()
    if data is None:
        return
    numbered_list = generate_numbered_list(data)
    top_titles_by_length = get_top_titles_by_length(data, n)
    total_items = count_items(data)
    write_report(output_file_path, numbered_list, top_titles_by_length, total_items)
    print("Report generated:", output_file_path)


if __name__ == "__main__":
    main()


