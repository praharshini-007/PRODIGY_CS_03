import re
import getpass

print("----------------Password Complexity Checking Tool----------------")

def assess_password_strength(password):
    #checking criteria
    has_numbers=any(char.isdigit()for char in password)
    has_upper_lower_case=any(char.isupper()or char.islower()for char in password)
    meets_length_requirement=len(password)>=8
    has_special_characters=bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]",password))

    #counts the number of met criteria
    met_criteria_count=sum([has_numbers,has_upper_lower_case,meets_length_requirement,has_special_characters])

    #classifies the password based on the number of met criteria
    if met_Criteria_count==4:
        return"password strength level:Very Strong(All Criteria are met)."
    elif met_criteria_count==3:
        return"password strength level:Moderately strong (Any 3 criteria are met)."
    elif met_criteria_count==2:
        return"password strength level:Strong(Any 2 criteria are met)."
    else:
        return"password strength level:Weak(none are only one criteria is met)."

    #gets user input for the password without displaying it on the screen
    password_input=getpass.getpass("Enter your password:")

    #Displayed characters as'#' except for the first and last character
    masked_password=password_input[0] + '#' * (len(password_input)-2)+password_input[-1]

    #Assesses the password strength
    result=assess_password_strength(password_input)

    #Provides more specific feedback to the user
    print("Entered password:{}".format(masked_password))
    print("")
    print(result)
    print("")
    tips=[
        "Here are some quick tips for creating a secure password:",
        "1.Length : Aim for atleast 12 characters.",
        "2.Mix characters:use a combination of uppercase,lowercase,numbersand symbols.",
        "3.Avoid common words:don't use easily gussable information.",
        "4.No personal info: Avoid using names,birthdays,or personal details.",
        "5.use passphrases: Consider combining multiple words or a sentence.",
        "6.unique for each account:Don't reuse passwords across multiple accounts.",
        "7.Regular updates:Chnage passwords periodically.",
        "8.Enable 2FA: Use Two-factor authentication where possible.",
        "9.Be wary of phishing :Avoid entering passwords on suspicious sites.",
        "10.password Manager:consider using one for secure and unique passwords."
    ]
   #Displays the tips
   for tip in tips:
       print(tip)
    