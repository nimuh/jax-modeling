




class ProteinTokenizer:
    def __init__(self, strategy: str = 'amino'):
        self.amino_acid     = "ARNDCQEGHILKMFPSTWYV"
        self.special_tokens = ['<pad>', "<eos>", "<mask>", "<cls>", "<unk>"]
        self.vocab = list(self.amino_acid) + self.special_tokens
        self.tok_to_int = {tok:i for i, tok in enumerate(self.vocab)}
        self.int_to_tok = dict(enumerate(self.vocab))

    def encode(self, sequence: list[str]):
        return [self.tok_to_int[tok] for tok in sequence]

    def decode(self, encoding: list[int]):
        return ''.join([self.int_to_tok[i] for i in encoding])





# implement dataset logic that follows PyTorch dataset logic
# TODO need to consider using JAX random seeds for indexing into dataset
# TODO masking and padding logic 
class ProteinSequenceDataset:
    pass