# H1) The Spam Detector (Search in Stream) — Linear Search
# A cybersecurity intern at a startup is building a basic spam filter.
# Incoming emails are checked against a blacklist of known spam sender IDs.
# The blacklist has no order.
blacklisters=["nnicrosoft@gmail.com","lotus365@gmail.com","1xbet@gmail.com"]
mailid=input()
flag=False
for i in  blacklisters:
    if mailid in blacklisters:
        flag=True
        break

if flag==True:
    print("this is a spam mail")
else:
    print("mail is not a spam")