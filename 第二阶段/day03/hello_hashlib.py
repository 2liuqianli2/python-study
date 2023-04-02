import hashlib

s="谢老板"

a=hashlib.new("md5",s.encode("utf-8"))

b=a.hexdigest()
print(b)

print("-*"*50)

a1=hashlib.md5()
a1.update(s.encode("utf-8"))
b1=a1.hexdigest()
print(b1)
b11=a1.digest()
print(b11)