import re
import pdb
from Bio import SeqIO
from io import StringIO


class Parser():

    """Wrapper for integrating BioPython functionality with
    database"""

    def __init__(self, file_string, filetype: str in ('fasta', 'genbank')):
        self.file_string = file_string
        self.filetype = filetype
        self.records = self.parse()

    def parse(self):
        stream = StringIO(self.file_string)
        return list(SeqIO.parse(stream, self.filetype))
