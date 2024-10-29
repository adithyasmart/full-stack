from unstructured.documents import Document
from unstructured.partition.pdf import partition_pdf

async def parse_document(file):
    document = Document(file)
    extracted = partition_pdf(document)
    return extracted
