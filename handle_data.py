
import re
import pandas as pd

class DataProcessor(object):
    """Processes data from a CSV file."""

    def __init__(self, file_path):
        """Initializes the DataProcessor with a file path."""
        self.file_path = file_path
        try:
            self.df = self.load_data_to_dataframe(file_path)
        except (FileNotFoundError, ValueError) as e:
            print(f"Error initializing DataProcessor: {e}")
            self.df = None


    def load_data_to_dataframe(self,file_path):
        try:
            df=pd.read_csv(file_path)
            return df
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found at path: {file_path}") 

        
    def get_info(self):
        print("Dataframe shape:", self.df.shape)
        print("Dataframe columns:", self.df.columns)
        print("Dataframe info:")
        print(self.df.info())
        
    def clean_column_names(self):
        """Removes leading/trailing whitespace from column names."""
        self.df=self.df.rename(columns=lambda x:x.strip())
       
    def remove_duplicates(self):
        """Removes duplicates from column product ID."""
        self.df=self.df.drop_duplicates(subset='Product ID') 

    def ensure_data_types(self):
        """Converts numeric columns to numeric data type. Handles errors gracefully."""
        numeric_columns=['Price', 'Discount (%)', 'Stock Quantity', 'Rating (out of 5)', 'Shipping Weight (lbs)']
        self.df[numeric_columns]=self.df[numeric_columns].apply(pd.to_numeric, errors='coerce')

    def drop_null_columns(self):
        """Drops columns with missing values."""
        self.df=self.df.dropna(subset=['Product ID', 'Product Name', 'Category', 'Price', 'Discount (%)', 'Stock Quantity', 'Rating (out of 5)', 'Shipping Weight (lbs)', 'Color', 'Material'])

    def sort_columns(self):
        """Sorts the dataframe by category and material."""
        self.df=self.df.sort_values(by=['Category', 'Material'])

    def groupby(self):
        """Groups the dataframe by category and material, calculates the mean price for each group, and resets the index."""
        self.df= self.df.groupby(['Category', 'Material']).agg({'Price': 'mean'}).reset_index()

    def rename_column_name(self):
        """Renames a specific column."""
        self.df=self.df.rename(columns={'Price': 'AveragePrice'})


    def remove_special_characters(self):
        """Removes special characters from column Category names."""
        def apply(column):
            cleaned_text = re.sub(r'[^\w]', '', column)
            return cleaned_text

        self.df['Category'] = self.df['Category'].apply(apply)