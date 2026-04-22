from scraper import scrape_headlines
from reporter import generate_numbered_list, get_top_titles_by_length, count_items, write_report

def main():
    output_file_path = input ("Name output file (default: report.txt): ")
    if output_file_path == "":
        output_file_path = "report.txt"
    
    if not output_file_path.endswith(".txt"):
        output_file_path += ".txt"
    
    user_input = input("How many top titles? (default: 2)")
    if user_input == "":
        n = 2
    else:
        try:
            n = int(user_input)
        except ValueError:
            print("Invalid input, using default value (2).")
            n = 2
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
    print("Report generated:" , output_file_path)


if __name__ == "__main__":
    main()


