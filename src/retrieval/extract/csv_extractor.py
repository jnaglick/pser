import csv
import fnmatch

from .document_extractor import DocumentExtractor
from .filesys_extractor import FileExtractor

class CsvExtractor(DocumentExtractor):
    def extract(self, source, additional_metadata=None):
        results = []
        reader = csv.reader(source.splitlines())
        headers = next(reader, None)

        for rownum, row in enumerate(reader):
            document_dict = {headers[i]: value for i, value in enumerate(row)}
            document = '\n'.join(f'{key}: {value}' for key, value in document_dict.items())
            metadata = {'rownum': rownum}
            if additional_metadata is not None:
                metadata.update(additional_metadata)
            results.extend(super().extract(document, metadata))
        
        return results

class CsvFileExtractor(FileExtractor):
    def __init__(self):
        super().__init__([CsvExtractor()])

    def condition(self, file_path):
        return fnmatch.fnmatch(file_path, "*.csv")
