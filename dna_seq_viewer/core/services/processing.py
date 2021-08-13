import io


def parse_fasta(fasta_string):
    """Takes in string representation of FASTA-formatted text file and returns 
    2-tuple of (header, sequence)"""
    buf = io.StringIO(fasta_string)
    header, current_line, sequence = buf.readline().rstrip(), buf.readline().rstrip(), ""
    while len(current_line) > 0:
        sequence = sequence + current_line
        current_line = buf.readline().rstrip()
    buf.close()
    return (header, sequence)
