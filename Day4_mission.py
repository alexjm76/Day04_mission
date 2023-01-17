#7.10

start1 = ["fee", "fie","foe"]
rhymes = [
    ("flop","get a mop"),
    ("fope","turn the rope"),
    ("fa", " get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog","walk the dog"),
    ("fun","say we're done")

]
start2= "Someone better"

for i,j in rhymes:
    print(f"{start1[0]}! {start1[1]}! {start1[2]}! {i}!")
    print(f"{j} {start2}!")

