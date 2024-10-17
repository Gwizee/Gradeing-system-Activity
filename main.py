# 90-100 => A

# 80-89 => A-

# 70-79 => B

# 60-69 => B-

# 50-59 => C

# 40-49 => D

# 39 OR BELOW => FAIL

score = int(input("Enter Your Score"))

if score >= 90 and score <= 100 :
    print("Grade is A")
elif score >= 80 and score <= 89 :
    print("Grade is A-")
elif score >= 70 and score <= 79 :
    print("Grade is B")
elif score >= 60 and score <= 69 :
    print("Grade is B-")
elif score >= 50 and score <= 59 :
    print("Grade is C")
elif score >= 40 and score <= 49 :
    print("Grade is D")
elif score >= 0 and score <= 39 :
    print("Grade is F")
else :
    print("Invalid input")