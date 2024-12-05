
import re
email="""Education has made us a promise to provide all abc@gmail.com the above-mentioned abilities and skills. 
The truth kohli18@yahoo.com is that it has always kept its promise which is why rohit45@gmail.co many people count on it for the life they desire.
It is the enemy of poverty and friend virat456@outlook.com of peace and justice."""

e=re.findall(r"\w+@\w+.\w*",email)
for i in e:
    print(i.lower())

