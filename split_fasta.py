from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

# README
# This script will take a genome and break it into a set number of batches. 
#   Each batch will inclue the exact same number of nucleotides, except for the 
#   final batch which will only include the leftover nucleotides after all the 
#   splitting is complete. It uses iteration through sequences in a genome using
#   biopython. Each sequence in the output batch will have a renamed header to
#   include both the original header name, the beginning nucleotide position,
#   and the ending nucleotide position. It's hard to explain, and I'm tired...
#   just run it and see for yourself. 


# Set batch number
batch_number = 50

# Create a list of all the seq records inside of the genome
records = list(SeqIO.parse("aVan.fa", "fasta"))

# Define the chunk size
# Sum of all lengths of all records diveded by "batch_number"
chunk_size = sum(len(i) for i in records) // batch_number + 1


# Start creating batches
def create_batch(records, chunk_size):
    
	# Create an object out of each record and go through them iteratively
    record_it = iter(records)

    # The "next" object in the list of "records"... 
    # Basically going through each contig one at a time
    record = next(record_it)
    
    # Initiallize base pair counting
    current_base = 0

    # Create a dictionary for batches and initialize the batch size
    # "Batch" is defined as the output fasta file that has a collection of "chunks"
    batch = []
    batch_size = 0

    # While there are still records left in the list, keep creating new batches
    while record:

        # Loop over records untill the batch is full (i.e. reached the max chunk size), or there are no new records 
        while batch_size != chunk_size and record:

        	# Define the end... which sums up to the chunk size
            end = current_base + chunk_size - batch_size

            # Define the output sequence, which is the current base (beginning base), seperated by a ":" and the end base of the contig
            seq = record[current_base:end]

            # Define where to cut the contig off, which is the current base + the length of the output sequence defined above
            end_of_slice = current_base + len(seq) - 1

            # Create the fasta headers to match that of the original SGE script
            # <original_contig_name> ":" <beginning_base> "-" <end_base>
            fasta_header = record.id + ":{}-{}".format(current_base, end_of_slice)

            # Change the seq.id to the fasta header defined above. 
            seq.id = seq.name = fasta_header

            # Set a blank description for the sequence.
            # For some reason this throws off Biopython if there is nothing present in the description object. 
            seq.description = ''

            # Add the sequence to the current batch 
            batch.append(seq)

            # This is where we start doing the math. 
            # Add the lenth of the current sequence we are iterating through to the current base.
            # When doing this, we also need to keep track of the batch_size... we want to make everything as equal as possible.
            current_base += len(seq)
            batch_size += len(seq)

            # When we have "added" all of the bases from the current sequence we are iterating through, 
            # then we need to go and grab the next sequence in the list. 
            if current_base >= len(record):
                record = next(record_it, None)
                current_base = 0

        # Once we have a batch with the correct size, yield the batch.
        # OR... we have run out of sequences in the genome, so stop. 
        yield batch
        batch = []
        batch_size = 0

# Write out the batches as new fasta files. 
for i, batch in enumerate(create_batch(records, chunk_size)):

	#Name the filed and keep track of the numbering. 
    filename = "chunk{}.fasta".format(i)

    # Write all the batch'e's sequences and their appropriate headers to the output fasta file. 
    SeqIO.write(batch, filename, "fasta")

