s1 = int(input("Enter cyclist 1's speed: "))
s2 = int(input("Enter cyclist2's speed: "))
s3 = int(input("Enter cyclist3's speed: "))

avg = s1 + s2 + s3/3

if s1<avg :
    print(f"Cyclist 1 is slower than the average speed by {avg - s1} kph")

if s2<avg :
    print(f"Cyclist 2 is slower than the average speed by {avg - s2} kph")

if s3<avg :
    print(f"Cyclist 3 is slower than the average speed by {avg - s3} kph")
