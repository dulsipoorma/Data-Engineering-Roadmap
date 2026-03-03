def clean_name(raw_name):
    clean=raw_name.strip().title() #strip() removes the before and after spaces
                                   #title() make the first letter capital
    return clean

dirty_names=[" dulsi ","nimal "," KUMARA"," sAMAN"]

cleaned_names=[]

for name in dirty_names:
    formatted=clean_name(name)
    cleaned_names.append(formatted)

print("Original Names: ", dirty_names)
print("Cleaned Names: ",cleaned_names)