from Bio import SeqIO
import re
import pdb


class Parser():

    """Wrapper for integrating BioPython functionality with
    database"""

    def __init__(self, filepath, filetype: str in ('fasta', 'genbank')):
        self.raw_input = filepath
        self.filetype = filetype
        self.records = list(SeqIO.parse(filepath, filetype))

    def get_accession(self, header):
        regex = re.compile(r"(\W|\A)([A-Z]{1,2}_?\d+\.?\d*)")
        match = regex.search(header)
        pdb.set_trace()
        if match:
            return match[2]
        return None
