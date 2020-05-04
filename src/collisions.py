import random

def count_before_coll(buckets, loops=1):
    for i in range(loops):
        tries = 0
        tried = set()


        while True:
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets
            if hash_index not in tried:
                tried.add(hash_index)
                tries += 1
            else:
                break
        print(f"{buckets} Buckets, {tries} hashes before collision. ({tries/buckets * 100:.1f})%")

count_before_coll(100,10)