import os
if __name__ == "__main__":
    print "Setting up your Remote Gag Execution framework...."
    do_whitelist = True if raw_input("Do you want anyone on your network to be able to make your computer run arbitrary text-to-speech commands at any time? (Y / N): ").lower() == "n" else False
    print("Okay.")

    with open("whitelist.txt", "w") as f:
        f.write("""
# Enter the LDAPs of Atlassians you want to be able to run remote text-to-speech on your computer here, one per line.
# Leaving this file as-is will allow ANYONE to do this.
""")
    if do_whitelist:
        print("Enter the LDAPs (e.g. 'ahogue') of the people you want to give access to your Remote Gag Execution framework into 'whitelist.txt', one per line.")
        print("Leaving the whitelist blank will let ANYONE connect.")
        #security
        os.system(os.environ["EDITOR"] + " " + "whitelist.txt")

