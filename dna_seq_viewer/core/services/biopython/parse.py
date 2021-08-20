from Bio import SeqIO
from io import StringIO
import re
import pdb


class Parser():

    """Wrapper for integrating BioPython functionality with
    database"""

    def __init__(self, file_string, filetype: str in ('fasta', 'genbank')):
        self.file_string = file_string
        self.filetype = filetype
        self.records = None

    def parse(self):
        stream = StringIO(self.file_string)
        self.records = list(SeqIO.parse(stream, self.filetype))

    def get_accession(self, header):
        regex = re.compile(r"(\W|\A)([A-Z]{1,2}_?\d+\.?\d*)")
        match = regex.search(header)
        return match[2] if match else None
