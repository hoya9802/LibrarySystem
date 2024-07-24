import csv
import pandas as pd

def csv_to_list(file_path):
    f = open(file_path)
    csv_list = csv.reader(f)
    csv_list = list(csv_list)
    return csv_list

def display_csv_data(tree, status_label, file_path, name):
    df = pd.read_csv(file_path)
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            tree.delete(*tree.get_children())
            tree["columns"] = header
            for col in header:
                tree.heading(col, text=col)
                tree.column(col, width=100)
            for row in csv_reader:
                tree.insert("", "end", values=row)

            status_label.config(text=f"Total {name}: {len(df.values)}")

    except Exception as e:
        status_label.config(text=f"Error Code: {str(e)}")

def search(tree, search_entry, status_label):
    try:
        search_term = search_entry.get().lower()
        for row_id in tree.get_children():
            row_values = [tree.item(row_id, 'values')]
            if any(search_term in str(value).lower() for value in row_values[0]):
                tree.item(row_id, tags=('matched',))
            else:
                tree.item(row_id, tags=('not_matched',))
        
        for row_id in tree.get_children():
            if 'matched' in tree.item(row_id, 'tags'):
                tree.item(row_id, open=True)
            else:
                tree.detach(row_id)
    except Exception as e:
        print(f"오류 발생: {e}")
        status_label.config(text=f"오류 발생: {e}")

def change_value(book_path, target, value):
    with open(book_path, mode='r', newline='\n', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        
        rows = []
        for row in reader:
            if row['BOOK_ISBN'] == target:
                row['STATUS'] = value
            rows.append(row)

    with open(book_path, mode='w', newline='\n', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)