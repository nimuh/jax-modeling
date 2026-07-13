


# the focus here is on protein LMs so should create a dataset specifically for amino acid sequences

# TODO tokenizer for protein sequences to amino acids -> amino acids to integers
# TODO make a load function from a csv file in case of data that is already processed


from dataclasses import dataclass
from typing import Optional
from .tokenizer import ProteinTokenizer
import pandas as pd
import grain




@dataclass
class Protein:
    seq: str
    label: Optional[str] = None



def read_df_to_dataobj(df, sequence_column: str = 'sequence'):
    all_sequences = df.sequence.tolist()
    records: list[Protein] = []
    for sequence in all_sequences:
        records.append(Protein(seq=sequence))
    return records


def _load_from_file(path: str, min_len: int, max_len: int, is_csv: bool = False ) -> list[Protein]:

    if is_csv:
        # process csv file here
        df = pd.read_csv(path)
        proteins = read_df_to_dataobj(df)
        return proteins


    # process fasta file here
    else:
        # TODO
        return None



class ProteinSequenceSource(grain.sources.RandomAccessDataSource):
    def __init__(self, path: str, min_len: int, max_len: int, is_csv: bool = False):
        self.proteins = _load_from_file(path, is_csv=is_csv, min_len=min_len, max_len=max_len)
        self.tokenizer = ProteinTokenizer()

    def __getitem__(self, idxs):
        return self.proteins[idxs]

    def __len__(self):
        return len(self.proteins)




        
