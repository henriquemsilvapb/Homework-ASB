# NCBI Sequence Retrieval using Entrez API (ESearch + EFetch)

## Program usage

```
python3 fetch_sequences.py «database» «query»
```

#Example
```
python3 fetch_sequences.py nucleotide "BRCA1[gene] AND Homo sapiens[orgn]"
```

This script was developed as part of the coursework for the ASB (Analise de Sequencias Biológicas) UC, taught by Professor Francisco Pina.

The goal of this assignment is to create a non-interactive Python script capable of retrieving biological sequences from the NCBI Entrez API. The program performs a search in a specified NCBI database using ESearch, stores the results in the Entrez History Server, and then retrieves the sequences in FASTA format using EFetch.

The script receives the database and the search query as command-line arguments and prints the resulting sequences to STDOUT.

## Requirements

The following software must be installed before running the script:

* Python 3
* requests Python library(used to perform HTTP requests to the NCBI API)


 Install Python dependency

```
pip install requests
```

---
## Input arguments

* database – NCBI database to search (e.g., `nucleotide`, `protein`)
* query – Entrez search query string

Example query syntax follows the **NCBI Entrez search format**.

## Output

The script prints the retrieved sequences in FASTA format to the standard output.

## Workflow

The script performs the following steps:

1. Parse command-line arguments.
2. Use **ESearch** to query the specified NCBI database.
3. Store search results in the **Entrez History Server**.
4. Retrieve the identifiers (`WebEnv` and `QueryKey`).
5. Use **EFetch** to download the sequences in **FASTA format**.
6. Print the sequences to **STDOUT**.

## Author

Student project developed for the ASB UC.
Instructor: Professor Francisco Pina

Students : Henrique Silva 2024151657


