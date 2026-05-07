# 24. Calculate surface area of a cuboid 
# Formula: Surface Area=2(lb+bh+hl)
l = 4
b = 3
h = 2
print()
print(f"""Input:
area of a cuboid: l = {l}, b = {b}, h = {h}""")
print("="*35)
print()

surface_area = 2 * ((l*b)+(b*h)+(h*l))
print(f"""Output:
surface area of a cuboid: {surface_area}""")
print()