import re

phone1="""my phone number is +91 1234567890 and another is
+91 9876543210 and  (0243)345-8767 """

match=re.findall(r"\+\d{2}\s\d{10}",phone1) + re.findall(r"\(\d{4}\)\d{3}\-\d{4}",phone1) 
for i in match:
    print(i)
