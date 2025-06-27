#Napraviti generator funkcije za ispis svih parnih i svih neparnih brojeva manjih od prosljeđenog parametra.
def parni_brojevi(n):
    """Generator za ispis svih parnih brojeva manjih od n."""
    for i in range(n):
        if i % 2 == 0:
            yield i
