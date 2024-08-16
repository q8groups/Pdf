import PyPDF2
import csv

def extract_titles_and_page_numbers(pdf_path):
    titles_and_pages = []
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                title = text.split('\n')[1]  # Assuming the title is the first line of text
                titles_and_pages.append((title, page_num - 1))
    return titles_and_pages
# Example usage:
# titles_and_pages = extract_titles_and_page_numbers('example.pdf')
# for title, page in titles_and_pages:
#     print(f"Title: {title}, Page Number: {page}")


def export_titles_and_page_numbers_to_csv(titles_and_pages, csv_path):
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title', 'Page Number'])
        for title, page in titles_and_pages:
            writer.writerow([title, page])


def main():
    pdf_path = 'example.pdf'
    titles_and_pages = extract_titles_and_page_numbers(pdf_path)
    for title, page in titles_and_pages:
        if(page < 10):
            print(f"Title: {title[:-1]}, Page Number: {page}")
        else:
            print(f"Title: {title[:-2]}, Page Number: {page-1}")
    export_titles_and_page_numbers_to_csv(titles_and_pages, 'output.csv')

if __name__ == "__main__":
    main()