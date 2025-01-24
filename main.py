from handle_data import DataProcessor
def main():
    file_path = "data.csv"
    try:
        processor = DataProcessor(file_path)  # Potential exceptions raised here
        if processor.df is not None:  # Check if DataFrame was loaded successfully
            processor.clean_column_names()
            processor.remove_duplicates()
            processor.ensure_data_types()
            processor.drop_null_columns()
            processor.sort_columns() 
            processor.remove_special_characters()
            processor.groupby()
            processor.rename_column_name()
            print(processor.df)
        else:
            print("Data loading failed. Exiting.")
    except (FileNotFoundError, ValueError,Exception) as e:
        print("File Error")

    
if __name__ == "__main__":
    main()