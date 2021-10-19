
s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"  # raw string
# \n \r \t \b \f

print(len(s1), len(s2))

print('Python is the "best" language')
print("Dad's present was a fishing rod")
print("Dad's \"present\" was a fishing rod")
# BAD: print(r"Dad's \"present\" was a fishing rod")
print("""Dad's "present" was a fishing rod""")

query = """
select *
from customers
where state = 'TX'
"""



