mydict = {
    "garam" : "hot",
    "thandh" : "cold",
    "bank" : "bank"

}
print("options are" , mydict.keys())
a = input ("enter the hindi word\n")
print("the meaning of your word is: ", mydict.get(a))